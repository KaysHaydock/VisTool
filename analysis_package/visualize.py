"""
Module: visualize.py
Features:
    - Implemented: 
        1. `plot_histogram`: Plots a histogram of a column.
        2. `plot_scatter`: Creates a scatter plot of two columns.
        3. `plot_correlation_matrix`: Plots a heatmap of correlations between numeric columns.
        4. `plot_line`: Plots a line chart for time-series data.
        5. `option`: To save plots to a file.
    - Suggested:
        - Add support for time-series visualizations.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_histogram(data: pd.DataFrame, column: str, save_path: str = None) -> None:
    """
    Plots a histogram of the specified column.

    Args:
        data (pd.DataFrame): The input dataset.
        column (str): The column to plot.
        save_path (str): File path to save the plot (optional).

    Example:
        >>> plot_histogram(data, "age", save_path="histogram.png")
    """
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in the dataset.")
    
    data[column].hist()
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    
    # Show the plot only once
    if save_path is None:
        plt.show()

    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
        print(f"Histogram saved to {save_path}")
    
    # Close the plot to avoid <Figure> message
    plt.close()


def plot_scatter(data: pd.DataFrame, x_column: str, y_column: str, save_path: str = None) -> None:
    """
    Creates a scatter plot between two columns.

    Args:
        data (pd.DataFrame): The input dataset.
        x_column (str): The column for the x-axis.
        y_column (str): The column for the y-axis.
        save_path (str): File path to save the plot (optional).

    Example:
        >>> plot_scatter(data, "age", "income", save_path="scatter.png")
    """
    if x_column not in data.columns or y_column not in data.columns:
        raise ValueError(f"Columns '{x_column}' or '{y_column}' not found in the dataset.")
    
    plt.scatter(data[x_column], data[y_column])
    plt.title(f"Scatter Plot of {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    
    # Show the plot only once
    if save_path is None:
        plt.show()

    # If the user wants to save, save the plot without showing it again
    if save_path:
        plt.savefig(save_path)
        print(f"Scatter plot saved to {save_path}")
    
    # Close the plot to prevent it from showing again if the user chooses to save it
    plt.close()


def plot_correlation_matrix(data: pd.DataFrame, save_path: str = None) -> None:
    """
    Plots a heatmap of correlations between numeric columns.

    Args:
        data (pd.DataFrame): The input dataset.
        save_path (str): File path to save the plot (optional).

    Example:
         >>> plot_correlation_matrix(data, save_path="correlation_matrix.png")
    """
    correlation_matrix = data.corr()
    
    # Create the heatmap plot
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    
    # Show the plot only once
    if save_path is None:
        plt.show()

    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
        print(f"Correlation matrix saved to {save_path}")
    
    # Close the plot to avoid displaying it again
    plt.close()

def plot_line(data: pd.DataFrame, x_column: str, y_column: str, save_path: str = None) -> None:
    """
    Creates a line plot for time-series or sequential data.

    Args:
        data (pd.DataFrame): The input dataset.
        x_column (str): The column for the x-axis (time or sequence).
        y_column (str): The column for the y-axis (values).
        save_path (str): File path to save the plot (optional).

    Example:
        >>> plot_line(data, "date", "price", save_path="line_chart.png")
    """
    if x_column not in data.columns or y_column not in data.columns:
        raise ValueError(f"Columns '{x_column}' or '{y_column}' not found in the dataset.")
    
    plt.plot(data[x_column], data[y_column], marker='o')
    plt.title(f"Line Plot of {y_column} over {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    
    # Show the plot only once
    if save_path is None:
        plt.show()

    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
        print(f"Line plot saved to {save_path}")
    
    # Close the plot to avoid displaying it again
    plt.close()
