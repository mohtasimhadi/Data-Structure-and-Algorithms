def merge(left, right):
    mergedArray = [0] * (len(left) + len(right))
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            mergedArray[k] = left[i]
            i += 1
        else:
            mergedArray[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        mergedArray[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        mergedArray[k] = right[j]
        j += 1
        k += 1
    return mergedArray


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        arr = merge(left, right)
    return arr


array = [5, 2, 4, 6, 1, 3, 7, 8, 10, 9, 0]
print(mergeSort(array))
