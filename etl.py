import csv
import sqlite3

conn = sqlite3.connect("sales.db")
conn.execute("DROP TABLE IF EXISTS raw_sales")
conn.execute("""
    CREATE TABLE raw_sales (
        order_id TEXT, customer_id TEXT, order_date TEXT,
        product TEXT, quantity TEXT, price TEXT
    )
""")

with open("sales.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    rows = list(reader)

conn.executemany("INSERT INTO raw_sales VALUES (?,?,?,?,?,?)", rows)
conn.commit()
print(f"Loaded {len(rows)} rows")
conn.close()
