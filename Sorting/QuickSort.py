def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        left = []
        right = []
        pivot = array[len(array)-1]
        for i in range(0, len(array)-1):
            if array[i] <= pivot:
                left.append(array[i])
            else:
                right.append(array[i])
        return quickSort(left) + [pivot] + quickSort(right)

arr = [3, 0, 2, 5, -1, 4, 1 ]
print(quickSort(arr))