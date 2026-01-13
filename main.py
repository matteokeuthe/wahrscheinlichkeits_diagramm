from binomial import array_factorials
from plot import plot_factorials

n = int(input("Geben Sie n ein!"))
factorials = array_factorials(n)

# Diagramm anzeigen
plot_factorials(factorials)
