import pandas as pd
from vistool.combine import merge_datasets, concat_datasets

def test_merge_datasets():
    data1 = pd.DataFrame({"id": [1, 2, 3], "value1": [10, 20, 30]})
    data2 = pd.DataFrame({"id": [2, 3, 4], "value2": [40, 50, 60]})
    merged = merge_datasets(data1, data2, on="id", how="inner")
    assert len(merged) == 2  # Only rows with matching `id` values should remain
    assert "value2" in merged.columns

def test_concat_datasets():
    data1 = pd.DataFrame({"A": [1, 2]})
    data2 = pd.DataFrame({"B": [3, 4]})
    concatenated = concat_datasets([data1, data2], axis=1)
    assert concatenated.shape == (2, 2)  # 2 rows, 2 columns
    assert "B" in concatenated.columns