"""
Module: wrangle.py
Features:
    - Implemented: 
        1. `clean_data`: Cleans the dataset by dropping NaN values.
        2. `filter_data`: Filters rows based on a condition.
        3. `rename_columns`: Renames columns in the dataset.
    - Suggested:
        - Add functionality to standardize column names.
        - Implement feature scaling and encoding.
"""

import pandas as pd

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the dataset by dropping NaN values and resetting the index.

    Args:
        data (pd.DataFrame): The input dataset.

    Returns:
        pd.DataFrame: The cleaned dataset.

    Example:
        >>> clean_data(data)
    """
    cleaned_data = data.dropna().reset_index(drop=True)
    print("Data cleaned successfully.")
    return cleaned_data

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