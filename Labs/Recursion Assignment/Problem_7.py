def Fibonacci(n):
    return Fibonacci(n-1)+Fibonacci(n-2) if n > 2 else 1
print(Fibonacci(int(input())))