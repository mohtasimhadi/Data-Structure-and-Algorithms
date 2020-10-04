def print_fun(i, arr):
    if i < len(arr):
        print_fun(i+1, arr)
        print(arr[i], end=" ")

arr = []
for i in range(int(input())):
    arr.append(int(input()))
print_fun(0, arr)