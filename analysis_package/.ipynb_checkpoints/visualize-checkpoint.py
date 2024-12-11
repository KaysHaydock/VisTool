"""
Module: visualize.py
Features:
    - Implemented: 
        1. `plot_histogram`: Plots a histogram of a column.
        2. `plot_scatter`: Creates a scatter plot of two columns.
        3. `plot_correlation_matrix`: Plots a heatmap of correlations between numeric columns.
    - Suggested:
        - Add support for time-series visualizations.
        - Add an option to save plots to a file.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_histogram(data: pd.DataFrame, column: str) -> None:
    """
    Plots a histogram of the specified column.

    Args:
        data (pd.DataFrame): The input dataset.
        column (str): The column to plot.

    Example:
        >>> plot_histogram(data, "age")
    """
    data[column].hist()
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_scatter(data: pd.DataFrame, x_column: str, y_column: str) -> None:
    """
    Creates a scatter plot between two columns.

    Args:
        data (pd.DataFrame): The input dataset.
        x_column (str): The column for the x-axis.
        y_column (str): The column for the y-axis.

    Example:
        >>> plot_scatter(data, "age", "income")
    """
    plt.scatter(data[x_column], data[y_column])
    plt.title(f"Scatter Plot of {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def plot_correlation_matrix(data: pd.DataFrame) -> None:
    """
    Plots a heatmap of correlations between numeric columns.

    Args:
        data (pd.DataFrame): The input dataset.

    Example:
        >>> plot_correlation_matrix(data)
    """
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()