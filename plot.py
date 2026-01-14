"""Dieses Modul plottet die Grafik"""

import matplotlib.pyplot as plt

def plot_factorials(factorials):
    """Zeichnet ein Balkendiagramm für die Liste factorials"""
    k = list(range(1, len(factorials)+1))  # x-Achse: 1 bis n
    plt.bar(k, factorials)
    plt.xlabel("n")
    plt.ylabel("n!")
    plt.title("Fakultäten von 1 bis n")
    plt.show()

def plot_wahrscheinlichkeiten(wahrscheinlichkeiten):
    """Zeichnet ein Balkendiagramm für alle Wahrscheinlichkeiten"""
    k = list(range(0, len(wahrscheinlichkeiten)))
    plt.bar(k, wahrscheinlichkeiten)
    plt.xlabel("k")
    plt.ylabel("P(X=k)")
    plt.title("Binomialverteilte Wahrscheinlichkeit")
    plt.show()
