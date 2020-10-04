def factorial(n):
    return n*factorial(n-1) if n > 0 else 1
print(factorial(int(input())))