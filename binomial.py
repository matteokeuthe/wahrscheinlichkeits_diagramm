"""Dieses Modul fuehrt die Mathematik aus"""

def factorial(n):
    """Berechnet n! (Fakultät von n)"""
    if n < 0:
        raise ValueError("n muss >= 0 sein")    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def array_factorials(n):
    """Gibt eine Liste mit n Fakultäten aus (von 1 bis n)"""
    if n < 1:
        raise ValueError("n muss mindestens 1 sein")    
    factorials = []
    result = 1
    for i in range(1, n + 1):
        result *= i  # Fakultät berechnen
        factorials.append(result)
    return factorials

def binomial_verteilung(n, k, p):
    """Gibt eine Zahl der Binomialverteilung aus"""
    if not isinstance(n, int):
        raise TypeError("n muss natürlich sein")
    if n < 1:
        raise ValueError("n muss mindestens 1 sein")    
    return round(factorial(n) / (factorial(k) * factorial(n - k)) * p**k * (1 - p)**(n - k), 5)

def array_binomial_verteilung(n, p):
    """Gibt eine Liste mit allen Wahrscheinlichkeiten der Binomialverteilung aus"""
    wahrscheinlichkeiten = []
    for i in range(0, n + 1):
        wahrscheinlichkeiten.append(binomial_verteilung(n, i, p))
    return wahrscheinlichkeiten
