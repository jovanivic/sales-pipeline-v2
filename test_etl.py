from datetime import datetime
from etl import clean_up, parseit, dupe


def test_clean_up():
    assert clean_up("$1,234.50") == 1234.5


def test_parseit():
    assert parseit("2026-01-05") == datetime(2026, 1, 5)
    assert parseit("01/05/2026") == datetime(2026, 1, 5)


def test_dupe():
    rows = [
        {"order_id": 1, "price": 5},
        {"order_id": 1, "price": 9},
        {"order_id": 2, "price": 7},
    ]
    result = dupe(rows)
    assert len(result) == 2
    assert result[0]["price"] == 5