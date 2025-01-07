import os
import pytest
import pandas as pd
from vistool.download import (
    download_file,
    download_csv, 
    load_csv,
    load_excel, 
    summarize_data
)


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


# Test load_csv
def test_load_csv(tmp_path):
    """
    Test the functionality of loading a CSV file into a DataFrame.
    """
    # Create a sample CSV file
    csv_content = "Name,Age,Score\nAlice,25,85\nBob,30,90\nCharlie,35,95"
    csv_path = tmp_path / "test_data.csv"
    with open(csv_path, "w") as f:
        f.write(csv_content)

    # Load the CSV
    df = load_csv(csv_path)

    # Assertions
    assert isinstance(df, pd.DataFrame), "Returned object is not a DataFrame"
    assert df.shape == (3, 3), f"Unexpected shape: {df.shape}"
    assert "Name" in df.columns, "Column 'Name' is missing"

def test_load_csv_invalid_file():
    """
    Test behavior when an invalid CSV file is provided.
    """
    invalid_path = "nonexistent.csv"
    with pytest.raises(ValueError, match="Error loading CSV file"):
        load_csv(invalid_path)

# Test load_excel
def test_load_excel(tmp_path):
    """
    Test the functionality of loading an Excel file into a DataFrame.
    """
    # Create a sample Excel file
    excel_path = tmp_path / "test_data.xlsx"
    sample_data = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30], "Score": [85, 90]})
    sample_data.to_excel(excel_path, index=False, sheet_name="Sheet1")
    
    # Load the Excel file
    df = load_excel(excel_path, sheet_name="Sheet1")
    
    # Assertions
    assert isinstance(df, pd.DataFrame), "Returned object is not a DataFrame"
    assert not df.empty, "Loaded DataFrame is empty"
    assert list(df.columns) == ["Name", "Age", "Score"], f"Unexpected columns: {df.columns}"
    assert df["Name"].iloc[0] == "Alice", "First row 'Name' value is incorrect"
    
    
def test_load_excel_invalid_file():
    """
    Test behavior when an invalid Excel file is provided.
    """
    invalid_path = "nonexistent.xlsx"
    with pytest.raises(ValueError, match="Error loading Excel file"):
        load_excel(invalid_path)

# Test summarize_data
def test_summarize_data(capsys):
    """
    Test the summarize_data function to ensure it outputs the correct summary.
    """
    sample_data = {
        "Name": ["Alice", "Bob", "Alice", None],
        "Age": [25, 30, 25, None],
        "Score": [85, 90, 85, None],
        "Region": ["East", "West", "East", None]
    }
    df = pd.DataFrame(sample_data)

    # Call summarize_data and capture its output
    summarize_data(df)
    captured = capsys.readouterr()

    # Assertions on the output
    assert "Shape: 4 rows, 4 columns" in captured.out
    assert "Numeric Columns: 2 columns" in captured.out
    assert "Missing Values: 4 missing values in total" in captured.out
    assert "Duplicate Rows: 1 duplicate rows" in captured.out
