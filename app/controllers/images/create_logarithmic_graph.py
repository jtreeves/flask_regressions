from matplotlib.figure import Figure
from numpy import arange, log

def create_logarithmic_graph():
    fig = Figure(figsize=(5, 5))
    fig.set_tight_layout(True)
    graph = fig.add_subplot(1, 1, 1)
    xs = arange(0.1, 10.0, 0.1)
    ys = [(2 * log(x) + 3) for x in xs]
    graph.plot(xs, ys)
    graph.grid()
    return fig