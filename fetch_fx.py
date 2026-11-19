import os
import requests
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

resp = requests.get(
    "https://api.frankfurter.dev/v2/rates",
    params={"base": "USD", "quotes": "EUR,GBP,CAD"},
    timeout=10,
)
resp.raise_for_status()
data = resp.json()
print("fetched:", len(data))

rows = [
    {"rate_date": d["date"], "base": d["base"], "quote": d["quote"], "rate": d["rate"]}
    for d in data
]

upsert = text("""
    INSERT INTO fx_rates (rate_date, base, quote, rate)
    VALUES (:rate_date, :base, :quote, :rate)
    ON CONFLICT (rate_date, base, quote) DO UPDATE SET rate = EXCLUDED.rate
""")

with engine.begin() as conn:
    conn.execute(upsert, rows)

with engine.connect() as conn:
    total = conn.execute(text("SELECT COUNT(*) FROM fx_rates")).scalar()
print("rows in fx_rates:", total)

