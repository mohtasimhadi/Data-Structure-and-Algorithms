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

n = int(input())
k = int(input())

arr = []
arr2 = []

for i in range(n):
    arr.append(int(input()))

x = 0
for i in range(n):
    for j in range(n):
        arr2.append(str(arr[i])+" "+str(arr[j]))
        x += 1
arr2 = mergeSort(arr2)

print(arr2[k-1])