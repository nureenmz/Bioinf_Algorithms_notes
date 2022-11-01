def selectionSort(a):
    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j

        # swap the elements
        a[i], a[min] = a[min], a[i]

arr = [1, 12, 8, -3, 14]

print("Unsorted array:")
for i in range(len(arr)):
    print(arr[i],end=" ")
# Driver code to test above

selectionSort(arr)

print("")
print("Sorted array:")
for i in range(len(arr)):
    print(arr[i],end=" ")
print("")
