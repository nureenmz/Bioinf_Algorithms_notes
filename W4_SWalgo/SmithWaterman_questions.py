#This class uses the Smith Waterman Algorithm as an example of how to implement an algorithm in Python.
#In this  class we review key Python features and then modify an existing Smith-Waterman implementation
#In this example we index a Python list and treat it like an array, we make a list of list and this is a matrix



#Q1: Indexing Strings
testsequence="AGCGATDTTT"
#Q1a: How do you obtain the third character of testsequence and print it to screen?
print(testsequence[2])
#Q1B: How do you return the second and third characters?
testsequence[1:3]
#Q1C: How do you change the last character of "testsequence" to an "A" using Python code?
newseq = list(testsequence)
newseq[-1] = "A"
#Q1D: What value does testsequence[-1] equal?
	#A
#Q1E: Will "testsequence[len(testsequence)]" (without quotes)  generate an error?  If so why?
	#Yes, list index OOR



#Q2 Change counters
x=1
x+1
print(x) 
#Q2A: What is the value of x printed?  Why?
	#1, we didn't change the variable




#Q3: Define Functions
y=1
def myfunction(aval):
    aval=4
    return (y+1)
#Q3A: Call this function with "myfunction(y)", what is the value of y after this call
	# Ans: y is still 1, but function returns value of 2
#Q3B: What is the value of "aval" after the call to myfunction?
	# Ans: no value returned as it's a local variable, not global



#Q4: Passing and returning values
#Q4A Define a function that is passed  an integer and returns this integer incremented by one
def increment(val):
	return(val+1)



#Q5: Assignment and equivalence
z=4
if(z==True):
    print(z)
#Q5A: Will "z" print in this code?
	# Ans: No




#Q6: Simple loops
count=0
for i in range(1, 10):
         for j in range(1, 2):
             count=count+1
#What is the value of count?
	# Ans: 9 (9x1)




# Q7: Printing out formatted text
# "water" is the SW implementation
# This prints out some useful header information
# Change the header of this programme to print out a better summary of the programme (ie similar to the one from water)
import os
os.system("water -gapopen 10 -gapextend 0.5 afile.fasta bfile.fasta -outfile seq1_water")




#Q8: Parse a file
#Modify the code below to write a function that reads a fasta file
#and returns the sequence, ignoring the header
#Use Biopython for real projects that read fasta!!!
def read_fasta_filename(filename):
	seq=""
	with open(filename, 'r') as filehandle:
		for line in filehandle:
			if line[0]==">":
				continue
			print(line)
		return

read_fasta_filename("afile.fasta")




#Q9: Command line
#Below is a code example of how to parse the command line using argparse.  
#Modify this code so that you can pick up the settings for SmithWaterman as parameter passed to the application
#Build a modified SmithWaterman.py Python programme

import argparse

parser = argparse.ArgumentParser(description='Aligning sequences...')
parser.add_argument('seq1',action="store",help="First sequence")
parser.add_argument('seq2',action="store",help="Second sequence")
parser.add_argument('anum',action="store",help="A number",type =int)

args = parser.parse_args()
print(args)
print(args.seq1)

#see for help- https://docs.python.org/3/library/argparse.html
#Write code to pick up the command line so we can run command lines like "python3 SmithWaterman seq1 seq2"  
os.system("python3 SmithWaterman.py seq1 seq2")





#Q10: SmithWaterman.py Code Questions

#Q10A: Read the code of SmithWaterman.py and identify how the matix is initialised, where is the recurrence relationship defined?
	# Ans: By calc_score, the loop in the function build_matrix

#Q10B: What does the "range" command specify?
	# Ans: builds a list of integers of length specified for the "for" loop to traverse through

#Q10C: In the line 30 "sc = seqmatch if sequence1[y - 2] == sequence2[x - 2] else seqmismatch", why x-2 and y-2 and not x-1 or y-1 ?
	# Ans: Because we are mapping the matrix index to the sequence index- sequences are not padded by the gap insertion/deletion first row/column

#Q10D: Why "mymatrix[0]" in the code from line 46  "cols=len(mymatrix[0])"?
	# Ans: Data structure is a lsit of rows. Number of cols is the length of each row

#Q10E: What does the command at line 71 do  "return [mrow,mcol]"?
	# Ans: Returns the index of the max value

#Q10F: Line 85 "print("\n",end="")" what does "\n" specify?
	# carriage new line added to end of string

#Q10G: Line 91 "print("%02d\t" % (mymatrix[i][j]),end="")" what does the "%" specify?
	# Ans: print format the variable, in 2 decimal places
	# This represents the element mymatrix[i][j] in the string that will be inserted

#Q10H: Line 159 "global  seqmatch" why "global"?
	# Ans: so that the variable can be used outside of the function

#Q10I Could you remove the call to  "perform_smith_waterman()", line 188, and still run the code?
	# Ans: No. because that function encapsulates all the other functions in the code, and functions need to be called to actually run. otherwise it's just defined.
	# Alternatively, import code as a library, then run the function:
		import SmithWaterman
		SmithWaterman.perform_smith_waterman()
