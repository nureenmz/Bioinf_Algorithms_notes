
def partition(arr, left, right):
      i = left
      j = right
      tmp = 0
      pivot = arr[int((i + j) / 2)]

      while i <= j:
            while arr[i] < pivot:
                i+=1
            while arr[j] > pivot:
                j-=1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
                j-=1
      return i

def quickSort(arr, left, right):

      index = partition(arr, left, right)
      if left < index -1:
            quickSort(arr, left, index - 1)
      if  index < right:
            quickSort(arr, index, right)

def quickSortS(arr):
      quickSort(arr,0,len(arr)-1)


# Driver code to test above
arr = [1, 12, 8, -3, 14]

print("Unsorted array:")
for i in range(len(arr)):
    print(arr[i],end=" ")

quickSort(arr,0,len(arr)-1)

print("")
print("Sorted array:")
for i in range(len(arr)):
    print(arr[i],end=" ")
print("")

