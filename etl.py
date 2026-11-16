from datetime import datetime
import pandas as pd
from checks import check_schema, check_quality
from pathlib import Path
import logging
import sqlite3


BASE = Path(__file__).parent        # the folder that holds etl.py

DATE_FORMATS = ["%Y-%m-%d", "%m/%d/%Y", "%b %d %Y", "%Y/%m/%d"]


def clean_up(v):
    if v is None or str(v).strip() == "":
        return None
    try:
        return float(str(v).replace("$", "").replace(",", ""))
    except ValueError:
        return None


def parseit(t):
    if t is None:
        return None
    t = str(t).strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(t, fmt)
        except ValueError:
            continue
    return None


def dupe(rows):
    seen = set()
    result = []
    for r in rows:
        order_id = r["order_id"]
        if order_id not in seen:
            seen.add(order_id)
            result.append(r)
    return result


def load_to_sqlite(df, db_path):
    conn = sqlite3.connect(db_path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS sales (order_id INTEGER PRIMARY KEY, price REAL)"
    )
    rows = [(int(o), float(p)) for o, p in zip(df["order_id"], df["new_price"])]
    conn.executemany("INSERT OR REPLACE INTO sales VALUES (?, ?)", rows)
    conn.commit()
    total = conn.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
    conn.close()
    return total

def build_summary(df):
    return pd.DataFrame({
        "orders": [len(df)],
        "total_revenue": [df["new_price"].sum()],
        "avg_order_value": [df["new_price"].mean()],
    })

if __name__ == "__main__":
    logging.basicConfig(
        filename=BASE / "etl.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    try:
        logging.info("pipeline started")

        df = pd.read_csv(BASE / "sales.csv")
        rows_read = len(df)
        check_schema(df)
        df["new_price"] = df["price"].apply(clean_up)
        df = df.drop_duplicates(subset="order_id", keep="last")
        dupes_removed = rows_read - len(df)

        bad = df[df["new_price"].isna()]
        good = df[df["new_price"].notna()]
        bad.to_csv(BASE / "rejected_sales.csv", index=False)
        if len(bad) > 0:
            logging.warning(f"{len(bad)} rows rejected, see rejected_sales.csv")

        check_quality(good)
        good.to_csv(BASE / "cleaned_sales.csv", index=False)
        total = load_to_sqlite(good, BASE / "pipeline.db")
        logging.info(f"loaded {len(good)} rows, table now has {total} rows")
        logging.info(
            f"read {rows_read}, duplicates removed {dupes_removed}, "
            f"rejected {len(bad)}, wrote {len(good)}"
        )
        summary = build_summary(good)
        summary.to_csv(BASE / "summary.csv", index=False)
        logging.info(f"summary: {summary.iloc[0].to_dict()}")

    except Exception:
        logging.exception("pipeline failed")
        raise