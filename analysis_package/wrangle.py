"""
Module: wrangle.py
Features:
    - Implemented: 
        1. `clean_data`: Cleans the dataset by dropping NaN values/filling with mean.
        2. `filter_data`: Filters rows based on a condition.
        3. `rename_columns`: Renames columns in the dataset.
    - Suggested:
        - Add functionality to standardize column names.
        - Implement feature scaling and encoding.
"""

import pandas as pd

def clean_data(data: pd.DataFrame, remove_columns: list = None, fill_with: str = None) -> pd.DataFrame:
    """
    Cleans the dataset by either:
        - Dropping all rows with NaN values in specific columns.
        - Filling NaN values with the column mean or average for all numeric columns or specific columns.

    Args:
        data (pd.DataFrame): The input dataset.
        remove_columns (list, optional): List of column names to drop rows with NaN values in those columns.
        fill_with (str, optional): Strategy to fill NaN values. Options: 'mean' or 'average'. 
            If 'mean' or average' is selected, NaN values will be replaced with the column's mean value.

    Returns:
        pd.DataFrame: The cleaned dataset.

    Example:
        >>> clean_data(data, remove_columns=['A'])
        >>> clean_data(data, fill_with='mean')
    """

    if remove_columns:
        # Drop rows with NaN in specific columns
        data = data.dropna(subset=remove_columns).reset_index(drop=True)
        print(f"Rows with NaN in columns {remove_columns} were dropped.")
    
    elif fill_with == "mean" or fill_with == "average":
        # Fill NaN values with column mean
        data = data.fillna(data.mean(numeric_only=True))
        print(f"NaN values filled with column mean.")

    else:
        # Default behavior: Drop all rows with any NaN values
        data = data.dropna().reset_index(drop=True)
        print("Rows with any NaN values were dropped.")

    return data

def filter_data(data: pd.DataFrame, condition: str) -> pd.DataFrame:
    """
    Filters the dataset based on a specified condition.

    Args:
        data (pd.DataFrame): The input dataset.
        condition (str): A valid pandas query string to filter the data.

    Returns:
        pd.DataFrame: The filtered dataset.

    Example:
        >>> filter_data(data, "age > 30")
    """
    filtered_data = data.query(condition)
    print("Data filtered successfully.")
    return filtered_data

def rename_columns(data: pd.DataFrame, columns_mapping: dict) -> pd.DataFrame:
    """
    Renames columns in the dataset using the provided mapping.

    Args:
        data (pd.DataFrame): The input dataset.
        columns_mapping (dict): Dictionary with old column names as keys and new names as values.

    Returns:
        pd.DataFrame: The dataset with renamed columns.

    Example:
        >>> rename_columns(data, {"old_col": "new_col"})
    """
    renamed_data = data.rename(columns=columns_mapping)
    print("Columns renamed successfully.")
    return renamed_data
