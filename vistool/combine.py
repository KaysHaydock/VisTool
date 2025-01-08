"""
Module: combine.py
Features:
    - Implemented: 
        1. `merge_datasets`: Merges two datasets on a specified column.
        2. `concat_datasets`: Concatenates multiple datasets along rows or columns.
    - Suggested:
        - Add support for different join methods (inner, outer, etc.) in `merge_datasets`.
        - Implement a function to handle overlapping column names during concatenation.
"""

import pandas as pd

def merge_datasets(data1: pd.DataFrame, data2: pd.DataFrame, on: str, how: str = "inner") -> pd.DataFrame:
    """
    Merges two datasets on a specified column.

    Args:
        data1 (pd.DataFrame): The first dataset.
        data2 (pd.DataFrame): The second dataset.
        on (str): The column name to merge on.
        how (str): Type of merge to be performed ('inner', 'outer', 'left', 'right').

    Returns:
        pd.DataFrame: The merged dataset.

    Example:
        >>> merge_datasets(df1, df2, "id", how="outer")
    """
    merged_data = pd.merge(data1, data2, on=on, how=how)
    print(f"Datasets merged successfully using {how} join.")
    return merged_data

def concat_datasets(datasets: list[pd.DataFrame], axis: int = 0) -> pd.DataFrame:
    """
    Concatenates a list of datasets along a specified axis.

    Args:
        datasets (list[pd.DataFrame]): List of datasets to concatenate.
        axis (int): The axis to concatenate along (0 for rows, 1 for columns).

    Returns:
        pd.DataFrame: The concatenated dataset.

    Example:
        >>> concat_datasets([df1, df2], axis=1)
    """
    concatenated_data = pd.concat(datasets, axis=axis)
    print(f"Datasets concatenated successfully along axis {axis}.")
    return concatenated_data