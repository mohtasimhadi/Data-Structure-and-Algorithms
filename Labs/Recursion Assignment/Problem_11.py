def findMax(arr): 
    return arr[0] if (len(arr) == 1) else max(arr[len(arr) - 1], findMax(arr[0:len(arr)-1]))

arr = []
for i in range(int(input())):
    arr.append(int(input()))

print(findMax(arr))