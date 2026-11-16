# p9

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE sales (order_id INTEGER PRIMARY KEY, price REAL)")

conn.execute("INSERT INTO sales VALUES (1, 5.0)")
conn.execute("INSERT INTO sales VALUES (2, 12.25)")
print(conn.execute("SELECT * FROM sales").fetchall())

conn.execute("INSERT OR REPLACE INTO sales VALUES (1, 9.0)")
conn.execute("INSERT OR REPLACE INTO sales VALUES (3, 7.5)")
print(conn.execute("SELECT * FROM sales").fetchall())