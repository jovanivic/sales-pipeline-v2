import pandas as pd
import pytest
from checks import check_quality, check_schema


def test_check_quality_rejects_duplicate_order_ids():
    df = pd.DataFrame({"order_id": [1, 1, 2], "new_price": [5.0, 7.0, 3.0]})
    with pytest.raises(AssertionError):
        check_quality(df)


def test_check_schema_rejects_renamed_column():
    df = pd.DataFrame({"order_id": [1], "unit_price": [5.0]})
    with pytest.raises(AssertionError):
        check_schema(df)