import time # a library needed fo timing functions

#import the scripts
exec(open('bubbleSort.py').read())
exec(open('quickSort.py').read())
exec(open('selectionSort.py').read())


#This reads a file...
def readFile(fle):
    f = open(fle, 'r')
    x = f.readlines()
    f.close()
    results = [int(i) for i in x]
    return results


#This can be passed a file to sort and the sort algorithm
def testPerformance(filename,algorithm):
    arr2 = readFile(filename)
    start = time.time()
    algorithm(arr2)
    elapsed = time.time()-start

    #how to print the elapsed time
    print(f"Sorted big array: {elapsed} secs")
    for i in range(10):
        print(arr2[i],end=" ")
    return elapsed 


def quickSortW(arr):
    quickSort(arr, 0, len(arr)-1)


dataset = ["random5000sorted.txt", "random5000.txt", "random20000.txt"]
functions = [selectionSort, bubbleSort, quickSort]

for method in functions:
    for data in dataset:
            print(f"\nSorting using {method.__name__} and {data}")
            testPerformance(data,method)
