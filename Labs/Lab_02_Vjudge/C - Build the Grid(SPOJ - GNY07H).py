def grid(e):
    a = [1, 1, 5, 11]
    return a[e] if e<4 else grid(e-1) + 5*grid(e-2) + grid(e-3) - grid(e-4)

for t in range(int(input())):
    print(t+1, grid(int(input())))