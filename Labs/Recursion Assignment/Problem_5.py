def evaluate_polynomial(i, x, n):
    return pow(x, i) + evaluate_polynomial(i+1, n, x) if i < n else 0
    
print(evaluate_polynomial(0, int(input()), int(input())))