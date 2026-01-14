"""main"""

from binomial import array_binomial_verteilung
from plot import plot_wahrscheinlichkeiten

n = int(input("Wie viele Versuche n? "))
p = float(input("Mit welcher Wahrscheinlichkeit pro Versuch p? "))
plot_wahrscheinlichkeiten(array_binomial_verteilung(n, p))
