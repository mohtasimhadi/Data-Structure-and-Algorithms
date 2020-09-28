def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr

n = int(input())
k = int(input())

arr = [0]*n
arr2 = [0]*n*n

for i in range(n):
    arr[i] = int(input())

x = 0
for i in range(n):
    for j in range(n):
        arr2[x] = str(arr[i])+" "+str(arr[j])
        x += 1
arr2 = insertionSort(arr2)

print(arr2[k-1])