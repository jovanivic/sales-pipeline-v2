# pratice d5

from datetime import datetime, timedelta

# dan = datetime.strptime("2026-03-04","%Y-%m-%d")
# print(dan)

# today = datetime(2026, 11, 4)
# deadline = today + timedelta(days=30)
# print(today < deadline)
# print(today)
# print(deadline)

# print(dan.strftime("%b-%d-%Y"))

# try:
#     datetime.strptime("Mar 4, 2026", "%Y-%m-%d")
# except ValueError as e:
#     print("hell nah:", e)

import pandas as pd
from pathlib import Path

base = Path(__file__).parent.parent
df = pd.read_csv(base/"dumbledore"/"sales.csv")
print(df.columns.tolist())
print(df["order_date"].head(15))

DATE_FORMATS = ["%Y-%m-%d", "%m/%d/%Y", "%b %d %Y", "%Y/%m/%d"]

def parse_date(text):
    if text is None:
        return None
    text = str(text).strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    return None


print(parse_date("2026-09-01"))
print(parse_date("09/02/2026"))
print(parse_date("Sep 3 2026"))
print(parse_date("2026/09/05"))
print(parse_date("  2026-09-07  "))
print(parse_date(""))
print(parse_date("Sep 3, 2026"))


df["new_order_date"] = df["order_date"].apply(parse_date)
print(df["new_order_date"].head(15))
print("failed to parse:", df["new_order_date"].isna().sum())









from datetime import timedelta, datetime

DATE_FORMATS = ["%Y-%m-%d", "%m/%d/%Y", "%b %d %Y", "%Y/%m/%d"]

def parseit(t):
    if t is None:
        return None
    t = str(t).strip()
    for fmt in DATE_FORMATS:
        try:
            datetime.strptime(t, fmt)
        except ValueError:
            continue
    return None