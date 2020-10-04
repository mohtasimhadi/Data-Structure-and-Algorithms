def print_polynomial(i, n):
    if i == 0 and i < n:
        print("1 + ", end='')
        print_polynomial(i+1, n)
    if i < n:
        print("x^"+str(i+1), end='')
        if i+1 != n:
            print(" + ", end='')
        print_polynomial(i+1, n)
    
print_polynomial(0, int(input()))