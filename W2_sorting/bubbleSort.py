def bubbleSort(arr):
    swapped = 1
    n = len(arr)
    j = 0

    # Traverse through all array elements
    while bool(swapped):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True


# Driver code to test above
arr = [1, 12, 8, -3, 14]

print("Unsorted array:")
for i in range(len(arr)):
    print(arr[i],end=" ")

bubbleSort(arr)

print("")
print("Sorted array:")
for i in range(len(arr)):
    print(arr[i],end=" ")
print("")
