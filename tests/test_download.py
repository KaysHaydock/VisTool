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
    
    # Assert the DataFrame is not empty and has expected columns
    assert isinstance(df, pd.DataFrame), "Returned object is not a DataFrame"
    assert not df.empty, "Downloaded DataFrame is empty"
    assert "JAN" in df.columns, "Expected column 'JAN' not found in DataFrame"

def test_download_invalid_url():
    """
    Test behavior when an invalid URL is provided.
    """
    invalid_url = "https://invalid-url.com/nonexistent.csv"
    with pytest.raises(Exception):
        download_file(invalid_url, "data/fake.csv")