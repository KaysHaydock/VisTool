import pytest
import pandas as pd
from vistool.wrangle import(
    clean_data, 
    filter_data, 
    rename_columns,
    label_encode
)

def test_clean_data():
    data = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, None]})
    cleaned = clean_data(data)
    assert len(cleaned) == 1  # Only one row with no NaN values
    assert cleaned.isnull().sum().sum() == 0

    cleaned_mean = clean_data(data, fill_with="mean")
    assert cleaned_mean.isnull().sum().sum() == 0
    assert cleaned_mean.loc[1, "A"] == 2  # Mean of column A

    with pytest.raises(ValueError):
        clean_data(data, apply_to="invalid")    
        
        
def test_filter_data():
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

    # Valid filter condition
    filtered = filter_data(data, "A > 1")
    assert len(filtered) == 2  # Only rows with `A > 1` remain
    assert filtered["A"].min() > 1

    # Test invalid condition (edge case)
    # Ensure the function raises a pandas.errors.UndefinedVariableError when the condition references a non-existent column
    with pytest.raises(pd.errors.UndefinedVariableError):
        filter_data(data, "C > 1")  # Column 'C' does not exist
    
def test_rename_columns():
    # Valid column renaming
    data = pd.DataFrame({"old_col": [1, 2]})
    renamed = rename_columns(data, {"old_col": "new_col"})
    assert "new_col" in renamed.columns
    assert "old_col" not in renamed.columns
    
    # Test invalid column name in columns_mapping
    data_invalid = pd.DataFrame({"old_col": [1, 2]})
    renamed_invalid = rename_columns(data_invalid, {"invalid_col": "new_col"})
    
    # Ensure the original dataframe is unchanged when invalid column is provided
    assert "invalid_col" not in renamed_invalid.columns
    assert "old_col" in renamed_invalid.columns


def test_label_encode():
    # Sample DataFrame with categorical data
    data = pd.DataFrame({
        'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue']
    })
    
    # Test: Apply label encoding on 'Color' column
    encoded_data = label_encode(data, 'Color')
    assert set(encoded_data['Color'].unique()) == {0, 1, 2}, "Label encoding failed"   
