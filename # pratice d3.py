rows = [
    {"order_id": "1001", "customer": "C001"},
    {"order_id": "1002", "customer": "C002"},
    {"order_id": "1002", "customer": "C002"},
]


# def dedupe(rows):
#     seen = set()
#     result = []
#     for row in rows:
#         order_id = row["order_id"]
#         if order_id not in seen:
#             seen.add(order_id)
#             result.append(row)
#     return result


# # print(rows)
# # # print(once)
# # # print(twice)
# # # print(once == twice)

# print(dedupe(rows))




import pandas as pd
from pathlib import Path

base = Path(__file__).parent.parent
df = pd.read_csv(base/"dumbledore"/"sales.csv")

print(df.duplicated().sum())

# print(df["order_id"])
# cistonje = df.drop_duplicates(subset="order_id").reset_index(drop=True)
# print(cistonje)


def dupe(rows):
    vision = set()
    result = []
    for r in rows:
        order_id = r["order_id"]
        if order_id not in vision:
            vision.add(order_id)
            result.append(r)
    return result


# print(dupe(df["order_id"]))

# df["order_id2"] = df["order_id"].apply(dupe)
# print(df["order_id2"])


rows = df.to_dict("records")    # the whole line, as a list
clean_rows = dupe(rows)         # one bouncer, one clipboard, everyone
clean = pd.DataFrame(clean_rows)



















