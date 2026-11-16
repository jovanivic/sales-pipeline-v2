# p_d10

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "customer": ["ana", "ben", "ana", "ben"],
    "price": [5.0, 12.25, 20.0, 99.0],
})

# print(orders.groupby("customer")["price"].sum())
# print(orders.groupby("customer")["price"].count())



customers = pd.DataFrame({
    "customer": ["ana", "ben", "cara"],
    "membership": ["gold", "free", "silver"],
})

# joined = orders.merge(customers, on="customer")
# print(joined)
# print(joined.groupby("membership")["price"].sum())

left = customers.merge(orders, on="customer", how="left")
print(left)