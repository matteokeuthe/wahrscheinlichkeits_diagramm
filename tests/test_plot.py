import matplotlib
matplotlib.use("Agg")  # verhindert Plot-Fenster

from plot import plot_factorials, plot_wahrscheinlichkeiten

# von ChatGPT
def test_plot_factorials_runs():
    data = [1, 2, 6, 24]
    plot_factorials(data)

def test_plot_wahrscheinlichkeiten():
    data = [0.25, 0.5, 0.25]
    plot_wahrscheinlichkeiten(data)
    