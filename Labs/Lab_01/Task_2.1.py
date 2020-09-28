def heapify(arr, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify (arr, n, largest)
    return arr

def heapSort(arr):
    n = len(arr)

    for i in range( n//2, -1, -1):
        arr = heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        arr = heapify(arr, i, 0)
    return arr

arr = [0]*1000
for i in range(1000):
    arr[i] = int(input())
    arr2 = heapSort(arr[0:i+1])
    if len(arr2)%2 != 0:
        print(arr2[int(len(arr2)/2)])
    else:
        print(int((arr2[int(len(arr2)/2)]+arr2[int(len(arr2)/2)-1])/2))