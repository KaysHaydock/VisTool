"""
Module: visualize.py
Features:
    - Implemented: 
        1. `plot_histogram`: Plots a histogram of a column.
        2. `plot_scatter`: Creates a scatter plot of two columns.
        3. `plot_correlation_matrix`: Plots a heatmap of correlations between 
            numeric columns.
        4. `plot_line`: Plots a line chart for time-series data.
        5. `plot_overlay`: Overlays multiple columns with different plot types.
    - Suggested:
        - Add support for time-series visualisations.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_histogram(
    data: pd.DataFrame, 
    column: str, 
    save_path: str = None
) -> None:
    """
    Plots a histogram of the specified column.

    Args:
        data (pd.DataFrame): The input dataset.
        column (str): The column to plot.
        save_path (str): File path to save the plot (optional).

    Example:
        >>> plot_histogram(data, "age", save_path="histogram.png")
    """
    column = column.lower() 
    
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in the dataset.")
    
    plt.figure(figsize=(16, 10))
    data[column].hist()
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    
    # Rotate X-axis labels if they are categorical
    plt.xticks(rotation=90) 
    plt.tight_layout()  
    
    # Show the plot only once
    if save_path is None:
        plt.show()

    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
        print(f"Histogram saved to {save_path}")
    
    # Close the plot to avoid <Figure> message
    plt.close()


def plot_scatter(
    data: pd.DataFrame, 
    x_column: str, 
    y_column: str, 
    save_path: str = None
) -> None:
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
    x_column = x_column.lower()  
    y_column = y_column.lower() 
    
    if x_column not in data.columns:
        raise ValueError(f"Column '{x_column}' not found in the dataset.")
    elif y_column not in data.columns:
        raise ValueError(f"Column '{y_column}' not found in the dataset.")
    
    plt.figure(figsize=(16, 10))
    plt.scatter(data[x_column], data[y_column])
    plt.title(f"Scatter Plot of {x_column} vs. {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    
    # Rotate X-axis labels if they are categorical
    plt.xticks(rotation=90) 
    plt.tight_layout()      
    
    # Show the plot only once
    if save_path is None:
        plt.show()

    # If the user wants to save, save the plot without showing it again
    elif save_path:
        plt.savefig(save_path)
        print(f"Scatter plot saved to {save_path}")
    
    # Close the plot to avoid <Figure> message
    plt.close()


def plot_correlation_matrix(
    data: pd.DataFrame, 
    save_path: str = None
) -> None:
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
    plt.figure(figsize=(16, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    
    # Rotate X-axis labels if they are categorical
    plt.xticks(rotation=90) 
    plt.tight_layout()      
    
    # Show the plot only once
    if save_path is None:
        plt.show()

    # Save the plot if save_path is provided
    elif save_path:
        plt.savefig(save_path)
        print(f"Correlation matrix saved to {save_path}")
    
    # Close the plot to avoid displaying it again
    plt.close()

def plot_line(
    data: pd.DataFrame, 
    x_column: str, 
    y_column: str, 
    save_path: str = None
) -> None:
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
    x_column = x_column.lower()
    y_column = y_column.lower() 
    
    if x_column not in data.columns or y_column not in data.columns:
        raise ValueError(
            f"Columns '{x_column}' or '{y_column}' not found in the dataset."
        )
    
    plt.figure(figsize=(16, 10))
    plt.plot(data[x_column], data[y_column], marker='o')
    plt.title(f"Line Plot of {y_column} over {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    
    # Rotate X-axis labels if they are categorical
    plt.xticks(rotation=90) 
    plt.tight_layout()      
    
    # Show the plot only once
    if save_path is None:
        plt.show()

    # Save the plot if save_path is provided
    elif save_path:
        plt.savefig(save_path)
        print(f"Line plot saved to {save_path}")
    
    # Close the plot to avoid displaying it again
    plt.close()
    
def plot_overlay(
    data: pd.DataFrame,
    columns: list,
    plot_types: list,
    line_colours = None,  
    bar_colours = None,  
    save_path: str = None,
    title: str = "Overlay Plot"
) -> None:
    """
    Plots multiple columns with specified plot types on a single graph.

    Args:
        data (pd.DataFrame): The input dataset.
        columns (list): List of column names to plot.
        plot_types (list): List of plot types ("line", "bar") corresponding 
            to the columns.
        save_path (str): File path to save the plot (optional).
        title (str): Title of the plot (default is "Overlay Plot").

    Example:
        >>> plot_overlay(
                data, ["A", "B"], ["line", "bar"], save_path="overlay_plot.png"
            )
    """
    columns = [col.lower() for col in columns] 
    plot_types = [pt.lower() for pt in plot_types] 
    
    if line_colours is None:
        line_colours = ["blue", "green", "purple"]
    if bar_colours is None:
        bar_colours = ["red", "orange", "pink"]
        
    if len(columns) != len(plot_types):
        raise ValueError("Length of 'columns' and 'plot_types' must match.")

    # Plot types to lowercase to ensure case insensitivity
    plot_types = [pt.lower() for pt in plot_types]
    
    plt.figure(figsize=(16, 10))

    for i, (col, plot_type) in enumerate(zip(columns, plot_types)):
        if col not in data.columns:
            raise ValueError(f"Column '{col}' not found in the dataset.")
        
        if plot_type == "line":
            plt.plot(
                data.index, 
                data[col], 
                label=f"{col} (Line)", 
                marker='o', 
                color=line_colours[i % len(line_colours)]  
            )
        elif plot_type == "bar":
            plt.bar(
                data.index, 
                data[col], 
                label=f"{col} (Bar)", 
                color=bar_colours[i % len(bar_colours)],  
                alpha=0.7
            )
        else:
            raise ValueError(
                f"Unsupported plot type '{plot_type}'. Use 'line' or 'bar'."
            )

    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
        print(f"Overlay plot saved to {save_path}")
    else:
        plt.show()

    plt.close()
