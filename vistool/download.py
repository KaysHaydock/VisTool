"""
Module: download.py
Features:
    - Implemented:
        1. `download_file`: Downloads a file from a given URL and saves it locally.
        2. `download_csv`: Downloads a CSV file from a URL and loads it into a Pandas DataFrame.
        3. load_csv file :  Loads a CSV file into a Pandas DataFrame from local path.
        4. load_excel : Load excel file into a Pandas DataFrame from local path. 
        5. summarize_data:   Summarizes key aspects of the dataset and provides an overview of its structure.
    - Suggested:
        - Add support for downloading multiple files simultaneously.
        - Add retry mechanism in case of failed downloads.
"""

import requests
import pandas as pd
from pathlib import Path

def download_file(url: str, save_path: str) -> None:
    """
    Downloads a file from the given URL and saves it to the specified path.

    Args:
        url (str): The URL of the file to download.
        save_path (str): The path where the file will be saved.

    Returns:
        None

    Example:
        >>> download_file("https://example.com/file.txt", "data/file.txt")
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"File downloaded successfully: {save_path}")

def download_csv(url: str) -> pd.DataFrame:
    """
    Downloads a CSV file from the given URL and loads it into a Pandas DataFrame.

    Args:
        url (str): The URL of the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.

    Example:
        >>> df = download_csv("https://example.com/data.csv")
    """
    response = requests.get(url)
    response.raise_for_status()
    from io import StringIO
    csv_data = StringIO(response.text)
    dataframe = pd.read_csv(csv_data)
    print("CSV downloaded and loaded into a DataFrame successfully.")
    return dataframe


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Loads a CSV file into a Pandas DataFrame.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the CSV data.

    Raises:
        ValueError: If the file cannot be loaded.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"File '{file_path}' loaded successfully!")
        return df
    except Exception as e:
        raise ValueError(f"Error loading CSV file: {e}")

def load_excel(file_path: str, sheet_name: str = None) -> pd.DataFrame:
    """
    Loads an Excel file into a Pandas DataFrame.

    Parameters:
        file_path (str): The path to the Excel file.
        sheet_name (str, optional): The sheet name to load. Loads the first sheet by default.

    Returns:
        pd.DataFrame: A DataFrame containing the Excel data.

    Raises:
        ValueError: If the file cannot be loaded.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"File '{file_path}' loaded successfully!")
        return df
    except Exception as e:
        raise ValueError(f"Error loading Excel file: {e}")


def summarize_data(df):
    """
    Summarizes key aspects of the dataset and provides an overview of its structure.

    Parameters:
    ----------
    df : pandas.DataFrame
        The dataset to be summarized.

    Prints:
    -------
    - Shape of the dataset (number of rows and columns)
    - Lists of numeric and non-numeric columns
    - Total number of missing values in the dataset
    - Count of duplicate rows
    - Categorical columns (non-numeric columns with fewer unique values)
    - Correlation matrix for numeric columns (if available)
    
    Example:
    --------
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=5),
        'Sales': [200, 220, 250, 270, 300],
        'Profit': [50, 60, 65, 70, 80],
        'Region': ['East', 'West', 'North', 'South', 'East'],
    }
    df = pd.DataFrame(data)
    
    summarize_data_overview(df)
    """
    
    # 1. Shape of the dataset (rows, columns)
    shape = df.shape
    rows, cols = shape[0], shape[1]

    # 2. Numeric and Non-Numeric Columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    non_numeric_cols = df.select_dtypes(exclude=['float64', 'int64']).columns

    # 3. Missing values per column
    missing_values = df.isnull().sum().sum()

    # 4. Duplicate rows
    duplicate_count = df.duplicated().sum()

    # 5. Categorical columns (non-numeric with fewer unique values)
    categorical_cols = df.select_dtypes(exclude=['float64', 'int64']).nunique()
    categorical_cols = categorical_cols[categorical_cols < 10].index  # Adjust threshold as needed

    # 6. Correlation summary for numerical columns
    correlation_matrix = df[numeric_cols].corr() if len(numeric_cols) > 0 else None

    # Summary
    summary = f"""
    --- Data Overview ---
    Shape: {rows} rows, {cols} columns

    Numeric Columns: {len(numeric_cols)} columns (e.g., {', '.join(numeric_cols[:3])}...)
    Non-Numeric Columns: {len(non_numeric_cols)} columns (e.g., {', '.join(non_numeric_cols[:3])}...)

    Missing Values: {missing_values} missing values in total
    Duplicate Rows: {duplicate_count} duplicate rows

    Categorical Columns: {len(categorical_cols)} columns (e.g., {', '.join(categorical_cols[:3])}...)

    Correlation between numeric columns:
    {correlation_matrix if correlation_matrix is not None else "No numeric columns to compute correlation."}
    """
    
    print(summary)
