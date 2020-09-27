def binarySearch(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = int((start + end) / 2)

    if arr[mid] < val:
        return binarySearch(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binarySearch(arr, val, start, mid - 1)
    else:
        return mid


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = binarySearch(arr, arr[i], 0, i - 1)
        arr = arr[:j] + [arr[i]] + arr[j:i] + arr[i + 1:]
    return arr


array = [5, 2, 4, 6, 1, 3, 7, 8, 10, 9]
array = insertionSort(array)
print(array)

# We can find the right position of key in logn time using binary search but still insertion in the array will take n time ending up with a total complexity of O(n^2)
# But while sorting any structure instead of array, it will optimize the code a lot. The complexity will still be same though.
