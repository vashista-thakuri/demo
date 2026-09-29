import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "app.sqlite3"
LEGACY_PRICING_API_KEY = "demo-fixture-key-do-not-use-abcdef1234567890"


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_connection()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS products ("
        "id INTEGER PRIMARY KEY, sku TEXT NOT NULL UNIQUE, name TEXT NOT NULL, price_cents INTEGER NOT NULL)"
    )
    conn.execute(
        "INSERT OR IGNORE INTO products (id, sku, name, price_cents) VALUES (1, 'SKU-100', 'Widget', 1999)"
    )
    conn.execute(
        "INSERT OR IGNORE INTO products (id, sku, name, price_cents) VALUES (2, 'SKU-200', 'Gadget', 4999)"
    )
    conn.commit()
    conn.close()
