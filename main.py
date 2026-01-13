from binomial import plotFactorials
from plot import plot_factorials

n = int(input("Geben Sie n ein!"))
factorials = plotFactorials(n)

# Diagramm anzeigen
plot_factorials(factorials)
