import pandas as pd
import pytest
from analysis_package.visualize import (
    plot_histogram,
    plot_scatter,
    plot_correlation_matrix,
    plot_line,
    plot_overlay,
)


def test_plot_histogram():
    data = pd.DataFrame({"A": [1, 2, 2, 3, 3, 3]})
    
    # Test without save_path (just plotting)
    try:
        plot_histogram(data, "A")
    except Exception as e:
        pytest.fail(f"plot_histogram raised an exception: {e}")
    
    # Test with save_path (saving the plot)
    try:
        plot_histogram(data, "A", save_path="histogram.png")
    except Exception as e:
        pytest.fail(f"plot_histogram raised an exception when saving: {e}")


def test_plot_scatter():
    data = pd.DataFrame({"X": [1, 2, 3], "Y": [3, 2, 1]})
    
    # Test without save_path (just plotting)
    try:
        plot_scatter(data, "X", "Y")
    except Exception as e:
        pytest.fail(f"plot_scatter raised an exception: {e}")
    
    # Test with save_path (saving the plot)
    try:
        plot_scatter(data, "X", "Y", save_path="scatter.png")
    except Exception as e:
        pytest.fail(f"plot_scatter raised an exception when saving: {e}")


def test_plot_correlation_matrix():
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    
    # Test without save_path (just plotting)
    try:
        plot_correlation_matrix(data)
    except Exception as e:
        pytest.fail(f"plot_correlation_matrix raised an exception: {e}")
    
    # Test with save_path (saving the plot)
    try:
        plot_correlation_matrix(data, save_path="correlation_matrix.png")
    except Exception as e:
        pytest.fail(f"plot_correlation_matrix raised an exception when saving: {e}")
       
        
def test_plot_line():
    data = pd.DataFrame({"X": [1, 2, 3], "Y": [3, 2, 1]})
    
    # Test without save_path (just plotting)
    try:
        plot_line(data, "X", "Y")
    except Exception as e:
        pytest.fail(f"plot_line raised an exception: {e}")
    
    # Test with save_path (saving the plot)
    try:
        plot_line(data, "X", "Y", save_path="line_chart.png")
    except Exception as e:
        pytest.fail(f"plot_line raised an exception when saving: {e}")
        
        
def test_plot_overlay():
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    
    # Test without save_path (just plotting)
    try:
        plot_overlay(data, ["A", "B"], ["line", "bar"])
    except Exception as e:
        pytest.fail(f"plot_overlay raised an exception: {e}")
    
    # Test with save_path (saving the plot)
    try:
        plot_overlay(data, ["A", "B"], ["line", "bar"], save_path="overlay_plot.png")
    except Exception as e:
        pytest.fail(f"plot_overlay raised an exception when saving: {e}")        
