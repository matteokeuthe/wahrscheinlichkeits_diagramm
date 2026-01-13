def factorial(n):
    """Berechnet n! (Fakultät von n)"""
    if n < 0:
        raise ValueError("n muss >= 0 sein")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(6))