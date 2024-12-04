"""
Module: download.py
Features:
    - Implemented:
        1. `download_file`: Downloads a file from a given URL and saves it locally.
        2. `download_csv`: Downloads a CSV file from a URL and loads it into a Pandas DataFrame.
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