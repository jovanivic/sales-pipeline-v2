import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
url = os.getenv("DATABASE_URL")
engine = create_engine(url)

with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM orders"))
    print(result.scalar())

    result = conn.execute(text("SELECT COUNT(*) FROM customers"))
    print(result.scalar())
