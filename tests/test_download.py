import os
import pytest
from analysis_package.download import download_file, download_csv
import pandas as pd

def test_download_file(tmp_path):
    """
    Test the functionality of downloading a file and saving it locally.
    """
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    save_path = tmp_path / "airtravel.csv"
    download_file(url, save_path)
    
    # Assert file exists and is not empty
    assert save_path.exists(), "File was not downloaded successfully"
    assert os.path.getsize(save_path) > 0, "Downloaded file is empty"

def test_download_csv():
    """
    Test the functionality of downloading a CSV and loading it into a DataFrame.
    """
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    df = download_csv(url)
    
    # Preprocess column names to strip leading/trailing spaces and remove quotes
    df.columns = df.columns.str.strip().str.replace('"', '')
    
    # Assert the DataFrame is not empty and has expected structure
    assert isinstance(df, pd.DataFrame), "Returned object is not a DataFrame"
    assert not df.empty, "Downloaded DataFrame is empty"

    # Validate the column names
    expected_columns = ["Month", "1958", "1959", "1960"]
    assert list(df.columns) == expected_columns, f"Unexpected columns: {df.columns}"

    # Check for specific data within the 'Month' column
    assert "JAN" in df["Month"].values, "Expected value 'JAN' not found in 'Month' column"

def test_download_invalid_url():
    """
    Test behavior when an invalid URL is provided.
    """
    invalid_url = "https://invalid-url.com/nonexistent.csv"
    with pytest.raises(Exception):
        download_file(invalid_url, "data/fake.csv")
