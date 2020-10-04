def print_fun(i, j, arr):
    if i <= j:
        print(arr[i], arr[j])
        print_fun(i+1, j-1, arr)

arr = []
for i in range(int(input())):
    arr.append(int(input()))
print_fun(0, len(arr)-1, arr)