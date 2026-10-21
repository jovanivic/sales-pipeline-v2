def clean_price(vaule):
    if vaule is None or vaule == "":
        return None
    if isinstance(vaule, (int, float)):
        return float(vaule)
    cleaned = vaule.replace("$", "").replace(",","").strip()
    if cleaned == "":
        return None
    return float(cleaned)

print(clean_price("$1,299.50"))
print(clean_price("  $20.00 "))
print(clean_price(15.25))
print(clean_price(""))
print(clean_price(None))
print(clean_price(clean_price("$1,299.50")))

first = clean_price("$1,299.50")   # runs the function, stores 1299.5 in `first`, prints nothing
second = clean_price(first)        # runs it again on 1299.5, stores 1299.5 in `second`, prints nothing
print(second)                      # this line is what shows 1299.5 on screen

import pandas as pd

def dedupe(df, key):
    return df.drop_duplicates(subset=key)

sample = pd.DataFrame({"order_id": [101, 102, 102], "customer": ["Ana", "Ben", "Ben"]})

print(len(sample), len(dedupe(sample, "order_id")))

from datetime import datetime

def parse_date(value):
    if value is None or value == "":
        return None
    for fmt in ("%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(value.strip(),fmt).date()
        except ValueError:
            continue
    return None

print(parse_date("2026-01-05"))
print(parse_date("01/07/2026"))
print(parse_date(""))
print(parse_date("not a date"))
print(parse_date(None))