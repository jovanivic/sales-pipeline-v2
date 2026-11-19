import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from etl import clean_up, parseit, dupe

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

df = pd.read_csv("sales_original.csv", dtype=str, keep_default_na=False)
rows = df.to_dict("records")
print("read:", len(rows))

rows = dupe(rows)
print("after dedupe:", len(rows))
print(rows[0])

clean = []
rejected = 0
for r in rows:
    order_date = parseit(r["order_date"])
    if r["order_id"] == "" or r["customer_id"] == "" or order_date is None:
        rejected += 1
        continue
    clean.append({
        "order_id": int(r["order_id"]),
        "customer_id": r["customer_id"],
        "order_date": order_date.date(),
        "product": r["product"] or None,
        "quantity": int(r["quantity"]) if r["quantity"] else None,
        "price": clean_up(r["price"]),
    })

print("clean:", len(clean), "rejected:", rejected)
print(clean[0])

upsert = text("""
    INSERT INTO sales_clean (order_id, customer_id, order_date, product, quantity, price)
    VALUES (:order_id, :customer_id, :order_date, :product, :quantity, :price)
    ON CONFLICT (order_id) DO UPDATE SET
        customer_id = EXCLUDED.customer_id,
        order_date  = EXCLUDED.order_date,
        product     = EXCLUDED.product,
        quantity    = EXCLUDED.quantity,
        price       = EXCLUDED.price
""")

with engine.begin() as conn:
    conn.execute(upsert, clean)

with engine.connect() as conn:
    total = conn.execute(text("SELECT COUNT(*) FROM sales_clean")).scalar()
print("rows in sales_clean:", total)
