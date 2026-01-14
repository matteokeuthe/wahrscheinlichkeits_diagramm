"""Testet binomial.py"""

from binomial import array_factorials, factorial, binomial_verteilung, array_binomial_verteilung

def test_array_factorials():
    """Testet array_factorials()"""
    n = 1
    result = array_factorials(n)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result == [1]

def test_factorial():
    """Testet factorial()"""
    n = 6
    result = factorial(n)
    assert result == 720

def test_binomial_verteilung():
    """Testet binomial_verteilung"""
    n = 10
    k = 3
    p = 0.3
    result = round(binomial_verteilung(n, k, p), 5)
    assert result == 0.26683

def test_array_binomial_verteilung():
    """Testet array_binomial_verteilung.py"""
    n = 2
    p = 0.5
    result = array_binomial_verteilung(n, p)
    assert isinstance(result, list)
    assert len(result) == n + 1
    assert result == [0.25, 0.5, 0.25]
