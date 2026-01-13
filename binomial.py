def factorial(n):
    """Berechnet n! (Fakultät von n)"""
    if n < 0:
        raise ValueError("n muss >= 0 sein")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def plotFactorials(n):
    """Gibt eine Liste mit n Fakultäten aus (von 1 bis n)"""
    if n < 1:
        raise ValueError("n muss mindestens 1 sein")
    
    factorials = []
    result = 1
    for i in range(1, n + 1):
        result *= i  # Fakultät berechnen
        factorials.append(result)
    
    return factorials

for i in plotFactorials(6):
    print(i)