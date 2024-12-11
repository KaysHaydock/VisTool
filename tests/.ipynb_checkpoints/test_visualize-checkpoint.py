import pandas as pd
from analysis_package.visualize import plot_histogram, plot_scatter, plot_correlation_matrix

def test_plot_histogram():
    data = pd.DataFrame({"A": [1, 2, 2, 3, 3, 3]})
    plot_histogram(data, "A")  # Should plot a histogram successfully

def test_plot_scatter():
    data = pd.DataFrame({"X": [1, 2, 3], "Y": [3, 2, 1]})
    plot_scatter(data, "X", "Y")  # Should plot a scatterplot successfully

def test_plot_correlation_matrix():
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    plot_correlation_matrix(data)  # Should plot a heatmap successfully