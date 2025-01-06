"""
Module: wrangle.py
Features:
    - Implemented: 
        1. `clean_data`: Cleans the dataset by dropping NaN values 
            or filling with mean.
        2. `filter_data`: Filters rows based on a condition.
        3. `rename_columns`: Renames columns in the dataset.
        4. `label_encode`: Perform label encoding on a categorical column using Pandas and NumPy.
    - Suggested:
        - Add functionality to standardise column names.
        - Implement feature scaling and encoding.
"""

import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output



def clean_data(
    data: pd.DataFrame, 
    remove_columns: list = None, 
    fill_with: str = None, 
    apply_to: str = "columns"
) -> pd.DataFrame:
    """
    Cleans the dataset by either:
        - Dropping all rows with NaN values in specific columns.
        - Filling NaN values with the column mean for numeric columns.

    Args:
        data (pd.DataFrame): The input dataset.
        remove_columns (list, optional): Columns to drop rows with NaN values.
        fill_with (str, optional): Strategy to fill NaN values. Options: 
            'mean' or 'average'. If selected, NaN values are replaced with 
            the column mean.
        apply_to (str, optional): Specifies whether to apply the operation to 
            'columns' or 'rows'. Default is 'columns'.

    Returns:
        pd.DataFrame: The cleaned dataset.

    Example:
        >>> clean_data(data, remove_columns=['A'], apply_to='columns')
        >>> clean_data(data, fill_with='mean', apply_to='rows')
    """
    if apply_to == "columns":
        if remove_columns:
            # Drop rows with NaN in specific columns
            data = data.dropna(subset=remove_columns).reset_index(drop=True)
            print(f"Rows with NaN in columns {remove_columns} were dropped.")
                   
        elif fill_with == "mean" or fill_with == "average":
            # Fill NaN values with column mean
            data = data.fillna(data.mean(numeric_only=True))
            print(f"NaN values filled with column mean.")
        
        else:
            # Default behavior: Drop rows with any NaN values in the columns
            data = data.dropna().reset_index(drop=True)
            print("Rows with any NaN values were dropped.")
    
    elif apply_to == "rows":
        if fill_with == "mean" or fill_with == "average":
            # Fill NaN values row-wise using the row mean
            data = data.apply(lambda row: row.fillna(row.mean()), axis=1)
            print(f"NaN values filled with row mean.")
        else:
            # Default behavior: Drop rows that contain NaN values
            data = data.dropna(axis=0).reset_index(drop=True)
            print("Rows with any NaN values were dropped.")
    
    else:
        raise ValueError("Invalid value for 'apply_to'. Use 'columns' or 'rows'.")
    
    return data


def filter_data(
    data: pd.DataFrame, 
    condition: str
) -> pd.DataFrame:
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


def rename_columns(
    data: pd.DataFrame, 
    columns_mapping: dict
) -> pd.DataFrame:
    """
    Renames columns in the dataset using the provided mapping.

    Args:
        data (pd.DataFrame): The input dataset.
        columns_mapping (dict): Dictionary with old column names as keys and 
            new names as values.

    Returns:
        pd.DataFrame: The dataset with renamed columns.

    Example:
        >>> rename_columns(data, {"old_col": "new_col"})
    """
    renamed_data = data.rename(columns=columns_mapping)
    print("Columns renamed successfully.")
    return renamed_data

def label_encode(data, column):
    """
    Perform label encoding on a categorical column using Pandas and NumPy.

    Args:
        data (pd.DataFrame): The dataset containing the categorical column.
        column (str): The name of the column to encode.

    Returns:
        pd.DataFrame: The dataset with the encoded column.
    """
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in the dataset.")

    # Label Encoding: Convert categories to integer labels
    data[column] = data[column].astype('category').cat.codes
    print(f"Label encoding applied to column: {column}")
    return data

def clean_data_interactive(data: pd.DataFrame):
    """
    Interactive function for cleaning a DataFrame using widgets.

    Features:
    - Allows users to select columns to remove.
    - Offers the option to fill NaN values with mean or average.
    - Provides control over whether operations are applied to columns or rows.

    Parameters:
    - data (pd.DataFrame): The input dataset.

    Example:
    ```python
    clean_data_interactive(data)
    ```
    Usage:
    - Choose columns to remove using the dropdown.
    - Select "mean" or "average" to fill NaN values.
    - Specify whether to apply cleaning to columns or rows.
    """
    remove_columns = widgets.SelectMultiple(
        options=data.columns.tolist(),
        description='Remove Columns:',
    )
    fill_with = widgets.Dropdown(
        options=['None', 'mean', 'average'],
        description='Fill With:',
    )
    apply_to = widgets.Dropdown(
        options=['columns', 'rows'],
        description='Apply To:',
    )

    def apply_cleaning(b):
        clear_output(wait=True)
        updated_data = clean_data(
            data,
            remove_columns=list(remove_columns.value),
            fill_with=fill_with.value if fill_with.value != 'None' else None,
            apply_to=apply_to.value
        )
        display(updated_data)

    button = widgets.Button(description="Apply Cleaning")
    button.on_click(apply_cleaning)
    display(remove_columns, fill_with, apply_to, button)


def filter_data_interactive(data: pd.DataFrame):
    """
    Interactive function for filtering a DataFrame using widgets.

    Features:
    - Allows users to specify a condition to filter rows.

    Parameters:
    - data (pd.DataFrame): The input dataset.

    Example:
    ```python
    filter_data_interactive(data)
    ```
    Usage:
    - Enter a filter condition (e.g., "Age > 30").
    - Click the "Apply Filter" button to view the filtered dataset.
    """
    condition = widgets.Text(
        placeholder='Enter condition (e.g., Age > 30)',
        description='Condition:',
    )

    def apply_filter(b):
        clear_output(wait=True)
        updated_data = filter_data(data, condition.value)
        display(updated_data)

    button = widgets.Button(description="Apply Filter")
    button.on_click(apply_filter)
    display(condition, button)



def filter_data_interactive(data: pd.DataFrame):
    """
    Interactive function for filtering a DataFrame using widgets.

    Features:
    - Allows users to specify a condition to filter rows.

    Parameters:
    - data (pd.DataFrame): The input dataset.

    Example:
    ```python
    filter_data_interactive(data)
    ```
    Usage:
    - Enter a filter condition (e.g., "Age > 30").
    - Click the "Apply Filter" button to view the filtered dataset.
    """
    condition = widgets.Text(
        placeholder='Enter condition (e.g., Age > 30)',
        description='Condition:',
    )

    def apply_filter(b):
        clear_output(wait=True)
        updated_data = filter_data(data, condition.value)
        display(updated_data)

    button = widgets.Button(description="Apply Filter")
    button.on_click(apply_filter)
    display(condition, button)      


def rename_columns_interactive(data: pd.DataFrame):
    """
    Interactive function for renaming columns in a DataFrame using widgets.

    Features:
    - Allows users to map old column names to new ones.

    Parameters:
    - data (pd.DataFrame): The input dataset.

    Example:
    ```python
    rename_columns_interactive(data)
    ```
    Usage:
    - Enter column mappings in the format: "old_name:new_name,old_name2:new_name2".
    - Click the "Apply Rename" button to rename the columns.
    """
    column_mapping = widgets.Text(
        placeholder='Enter mappings (e.g., old:new,age:years)',
        description='Mappings:',
    )

    def apply_rename(b):
        clear_output(wait=True)
        mappings = dict(item.split(':') for item in column_mapping.value.split(','))
        updated_data = rename_columns(data, mappings)
        display(updated_data)

    button = widgets.Button(description="Apply Rename")
    button.on_click(apply_rename)
    display(column_mapping, button)      


def label_encode_interactive(data: pd.DataFrame):
    """
    Interactive function for label encoding a column in a DataFrame using widgets.

    Features:
    - Allows users to select a column to encode as numeric labels.

    Parameters:
    - data (pd.DataFrame): The input dataset.

    Example:
    ```python
    label_encode_interactive(data)
    ```
    Usage:
    - Select a categorical column from the dropdown.
    - Click the "Apply Encoding" button to view the encoded dataset.
    """
    column = widgets.Dropdown(
        options=data.columns.tolist(),
        description='Column:',
    )

    def apply_encoding(b):
        clear_output(wait=True)
        updated_data = label_encode(data, column.value)
        display(updated_data)

    button = widgets.Button(description="Apply Encoding")
    button.on_click(apply_encoding)
    display(column, button)    



