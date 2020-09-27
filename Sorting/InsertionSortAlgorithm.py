def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr
array = [5, 2, 4, 6, 1, 3, 7, 8, 10, 9]
array = insertionSort(array)
print(array)

# Complexity O(n^2)
