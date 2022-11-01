#In this example we load two example files
#"Oct4.pos.fasta" contains sequence enriched from ChIP-seq experiment (peak centres) using Oct4, a transcription factor
#"bground.fasta" contains the background (non-enriched) sequences from the same experiment
#This code reads these files and searches for enrichment using Python dictionaries
#Complete the analysis and output the results of sorted 8bp enriched sequences
#Note we use 8bp because Oct4 is an "Octamer binding protein", it is known to bind 8mers
#The most common known binding site for Oct4 is ATCGCAAAT

from operator import itemgetter
import re

def normaliseDict(mydict):
    count=0 # count total reads
    for myseq in mydict.keys():
        count = count + mydict[myseq]
    count = count/100 #express as percent total
    for myseq in mydict.keys():
        mydict[myseq] = mydict[myseq]/count

def processSeq(mydict,myline,kmer):
    p = re.compile('[^ATGC]',re.IGNORECASE) #pattern searched for
    for i in range(0, len(myline)-kmer): # number of possible kmers per line
        myword=myline[i:i+kmer] # break sequence into k-length words
        if myword.find("N")!=-1: # next loop if don't find N
            continue
        if len(myword)!=kmer: # next loop if word is too short
            continue
        if p.match(myword): # next loop if word matches pattern
            continue
        if myword not in mydict: # use dict as counter
            mydict[myword] = 1
        else:
            mydict[myword] += 1

def buildDictionary(fastafile,kmer):
    f1 = open(fastafile, 'r')
    f1lines = f1.readlines()
    readBody = False
    myline = ""
    mydict = {}
    for line in f1lines:
        line = line.rstrip()
        if line.startswith('>'):
            if readBody==True:
                processSeq(mydict,myline,kmer) #we are ending the processing of a seq
                readBody = False
        if readBody==False:
            myline = ""
            readBody = True
        else:
            if len(line)>0:
                myline = myline+line # Store the sequence in myline
    f1.close()
    if readBody==True: # now process the sequence
        processSeq(mydict, myline, kmer)
    return mydict

def compareDictionaries(kmer):
    #just load the two files and count each kmer
    dictforeground = buildDictionary("Oct4.pos.fasta", kmer)
    dictbackground = buildDictionary("bground.fasta", kmer)
    #normalise by size
    normaliseDict(dictforeground)
    normaliseDict(dictbackground)
    F = open("testfile_fg.txt", "w")
    # itemgetter groups key-value pairs by the value, here the sorting is done by the value?? 
    for myseq in sorted(dictforeground.items(), key=itemgetter(1), reverse=True):
        if(len(myseq[0])!=kmer):
            continue
        F.write(myseq[0])
        F.write("\t")
        F.write(str(myseq[1]))
        F.write("\n")
    F.close()

    F = open("testfile_bg.txt", "w")
    for myseq in sorted(dictbackground.items(), key=itemgetter(1), reverse=True):
        if (len(myseq[0]) != kmer):
            continue
        F.write(myseq[0])
        F.write("\t")
        F.write(str(myseq[1]))
        F.write("\n")
    F.close()

    dictcombined = {}
    for myseq in sorted(dictforeground.items(), key=itemgetter(1), reverse=True):
      if len(myseq[0]) != kmer:
        continue
      background = dictbackground.get(myseq[0], 1) # 1 is used when n seq of this type in bg
      dictcombined[myseq[0]] = myseq[1]/background # Combine the dictionaries
      
    F = open("testfile_combined.txt", "w")
    for myseq in sorted(dictcombined.items(), key=itemgetter(1), reverse=True):
      F.write(myseq[0])
      F.write("\t")
      F.write(str(myseq[-1]))
      F.write("\n")
    F.close()

#actually run the programme
compareDictionaries(8)
