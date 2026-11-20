import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from api_client import get_json

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

users = get_json("https://jsonplaceholder.typicode.com/users")
print("fetched:", len(users))


def flatten_user(u):
    return {
        "user_id": u["id"],
        "name": u["name"],
        "email": u["email"],
        "city": u["address"]["city"],
        "lat": float(u["address"]["geo"]["lat"]),
        "lng": float(u["address"]["geo"]["lng"]),
        "company": u["company"]["name"],
    }


rows = [flatten_user(u) for u in users]
print(rows[0])

upsert = text("""
    INSERT INTO api_users (user_id, name, email, city, lat, lng, company)
    VALUES (:user_id, :name, :email, :city, :lat, :lng, :company)
    ON CONFLICT (user_id) DO UPDATE SET
        name = EXCLUDED.name, email = EXCLUDED.email, city = EXCLUDED.city,
        lat = EXCLUDED.lat, lng = EXCLUDED.lng, company = EXCLUDED.company
""")
with engine.begin() as conn:
    conn.execute(upsert, rows)
with engine.connect() as conn:
    total = conn.execute(text("SELECT COUNT(*) FROM api_users")).scalar()
print("rows in api_users:", total)

