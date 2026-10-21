import pandas as pd

raw = {
    "order_id":   [101, 102, 102, 103, 104],
    "customer":   ["Ana", "Ben", "Ben", None, "Dee"],
    "price":      ["$1,299.50", "$20.00", "$20.00", "$15.25", None],
    "order_date": ["2026-01-05", "01/07/2026", "01/07/2026", "2026-01-09", ""],
}
df = pd.DataFrame(raw)

# print(df)
# print(df.shape)
# print(df.dtypes)
# print(df.isna().sum())

df["price_num"] = df["price"].str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)
print(df[["price", "price_num"]])
print(df.dtypes)
print(df["price_num"].sum())

deduped = df.drop_duplicates(subset="order_id")
print(len(df), len(deduped))
print(deduped["price_num"].sum())