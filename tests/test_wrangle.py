import pandas as pd
from analysis_package.wrangle import clean_data, filter_data, rename_columns

def test_clean_data():
    data = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, None]})
    cleaned = clean_data(data)
    assert len(cleaned) == 1  # Only one row with no NaN values
    assert cleaned.isnull().sum().sum() == 0

def test_filter_data():
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    filtered = filter_data(data, "A > 1")
    assert len(filtered) == 2  # Only rows with `A > 1` remain

def test_rename_columns():
    data = pd.DataFrame({"old_col": [1, 2]})
    renamed = rename_columns(data, {"old_col": "new_col"})
    assert "new_col" in renamed.columns