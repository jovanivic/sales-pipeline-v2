# pratice d2

# import pandas as pd
# from pathlib import Path

# base = Path(__file__).parent.parent
# df = pd.read_csv(base/"dumbledore"/"sales.csv")

# print(df.head(5))
# print(df.dtypes)
# print(df.isna().sum())

# df["new_price"] = (df["price"].str.replace("$","",regex=False).str.replace(",","",regex=False).astype(float))

# print(df[["new_price","price"]].head(5))


# def c_p(v):
#     if v is None or str(v).strip() == "":
#         return None
#     return float(str(v).replace("$","").replace(",",""))

# df["n_p"] = df["price"].apply(c_p)
# print(df["n_p"].head(5))

import pandas as pd
from pathlib import Path

base = Path(__file__).parent.parent
df = pd.read_csv(base/"dumbledore"/"sales.csv")

print(df.dtypes)
print(df.isna().sum())
print(df.duplicated().sum())

# df["new_kanye"] = df["price"].str.replace("$","").str.replace(",","").astype(float)
# print(df["new_kanye"].head(5))


def clean_up(v):
    if v is None or str(v).strip() == "":
        return None
    return float(str).replace("$","").replace(",","")

df["new_price"] = df["price"].apply(clean_up)
print(df["price"].head(5))
