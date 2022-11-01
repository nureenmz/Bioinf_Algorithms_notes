#This is a simple implementation of a MapReduce algorithm in Python
import random
import string
import time
import timeit
from multiprocessing import Pool

#A simple Map Reduce Application to find the most common sequence in a random set of sequence

# Generates random strings of length 4
def createRandomStrings(count, seqlen=4):
  mylist = []
  for x in range(count):
    letters = "ATCG"
    str = ''.join(random.choice(letters) for i in range(seqlen))
    mylist.append(str)
  return mylist

# Chop strings in a list into N sets of elements ie. the number of cores
def chunk_alist(data, chunk_size):
  mylist_chunks = []
  sze = int((len(data)-1)/(chunk_size))
  stopp = len(data)
  for i in range(0, stopp, sze):
      mylist_chunks.append(list(data[i:i + sze]))
  return mylist_chunks

# Count the occurrence of each string using a dictionary
def getStringCounts(alist):
  strCounts = {}
  for x in alist:
    if x in strCounts:
      strCounts[x]=strCounts.get(x)+1
    else:
      strCounts[x]=1
  return strCounts

# Iterate key value pairs to find the seq with the highest count
def findMostFrequent(mappedv):
  fullset = {}
  for i in range(0, len(mappedv)):
    #fullset.update(mappedv[i])- add manually as merge does not seem to work
    mkeys=mappedv[i].keys()
    for x in mkeys:
      if x in fullset:
        fullset[x] = fullset.get(x) + mappedv[i].get(x)
      else:
        fullset[x] = mappedv[i].get(x)
  # get the key values
  mykeys = list(fullset.keys())
  bestkey = ""
  bestvalue = 0
  for ky in mykeys:
    if(fullset[ky]>bestvalue):
      bestvalue = fullset[ky]
      bestkey = ky
  return bestkey,bestvalue


# This finds the elements of interest
def runMapReduce(count=50,cores=2,seq_length=2):
  print(f"Running MapReduce for {count} random ATCG sequences with sequence length {seq_length} using {cores} thread(s)")
  # Parse the cores argument to specify number of worker processess to create
  pool = Pool(cores)
  # First build some strings and start the timer
  mystrings = createRandomStrings(count,seq_length)
  starttime = timeit.default_timer()
  # Chop strings into N sets of elements
  mystrings_chunked = chunk_alist(mystrings,cores)
  # Analyse the job for each core
  mappedv = pool.map(getStringCounts, mystrings_chunked)
  # Combine the results
  best = findMostFrequent(mappedv)
  endtime = timeit.default_timer()
  # Output final results
  #print(mystrings_chunked)
  print(f"### RESULTS ###\nBest key: {best[0]}\nBest value: {best[-1]}\nTime taken: {endtime-starttime} seconds")

# This ensures the threads will work correctly with the main
# Call to run the program
if __name__ == '__main__':
  run_custom = input("Run own parameters? ")
  if run_custom == "Yes" or run_custom == "yes":
    seq_count = int(input("Enter number of sequences to generate: "))
    thread_count = int(input("Enter number of thread: "))
    seq_length = int(input("Enter sequence length to process: "))
    random.seed(time.time())
    runMapReduce(seq_count,thread_count,seq_length)
  else:
    # Run using default (program test)
    random.seed(time.time())
    runMapReduce()
  
  
