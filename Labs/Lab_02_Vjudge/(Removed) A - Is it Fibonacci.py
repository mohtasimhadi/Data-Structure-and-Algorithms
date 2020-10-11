def firstDigits(a, b, n):
    return a if n == 1 else b

def fibonacci(a, b, n):
    return fibonacci(a, b, n-2) + fibonacci(a, b, n-1)**2 if n > 2 else firstDigits(a, b, n)
    
x = input().split()
print(fibonacci(int(x[0]), int(x[1]), int(x[2])))