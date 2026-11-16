# pratice d6


import pandas as pd

# df = pd.DataFrame({
#     "order_id": [1, 2, 3],
#     "price": [19.99, 5.00, -3.50],
# })


# # print(len(df))

# assert len(df) > 0, "dataframe is empty"
# # print("passed 1")

# # assert df["order_id"].is_unique, "duplicate found"
# # print("passed 2")

# # assert (df["price"] >= 0).all(), "negative"
# # print("passed 3")




# df1 = pd.DataFrame({"prices": [10.0, -3.5]})

# def check_prices(df):
#     assert (df["prices"] >= 0).all(), "negative prices found"

# check_prices(df1)
# print("prices ok")


# def has_negative_prices(df):
#     return (df["price"] < 0).any()


# def test_detects_negative_price():
#     df = pd.DataFrame({"price": [10.0, -3.5]})
#     assert has_negative_prices(df)


# def test_clean_data_passes():
#     df = pd.DataFrame({"price": [10.0, 3.5]})
#     assert not has_negative_prices(df)


# def test_zero_price_counts_as_negative():
#     df = pd.DataFrame({"price": [0.0, 3.5]})
#     assert has_negative_prices(df)

from datetime import datetime, timedelta

def clean_up(v):
    if v is None or str(v).strip() == "":
        return None
    return float(str(v).replace("$", "").replace(",", ""))

def test_comma_clean_up():
    assert clean_up("$1,234.50") == 1234.5
    print("ran")

DATE_FORMATS = ["%Y-%m-%d", "%m/%d/%Y", "%b %d %Y", "%Y/%m/%d"]

def parseit(t):
    if t is None:
        return None
    t = str(t).strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(t, fmt)
        except ValueError:
            continue
    return None

def test_two_formats():
    assert parseit("2026-01-05") == datetime(2026, 1, 5)
    assert parseit("01/05/2026") == datetime(2026, 1, 5)