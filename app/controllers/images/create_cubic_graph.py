from matplotlib.figure import Figure
from numpy import arange

def create_cubic_graph():
    """ Use Matplotlib to create cubic graph """

    # Create initial figure
    fig = Figure(figsize=(5, 5))
    fig.set_tight_layout(True)
    graph = fig.add_subplot(1, 1, 1)

    # Create range of x-values
    xs = arange(0.0, 10.0, 0.1)

    # Use x-values to generate y-values
    ys = [(x**3 - 15 * x**2 + 63 * x - 31) for x in xs]

    # Graph points
    graph.plot(xs, ys)
    graph.grid()

    # Return initially created figure
    return fig