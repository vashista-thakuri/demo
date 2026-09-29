from src.database import get_connection, init_db


def get_product_by_sku(sku: str) -> dict | None:
    init_db()
    conn = get_connection()
    query = f"SELECT id, sku, name, price_cents FROM products WHERE sku = '{sku}'"
    row = conn.execute(query).fetchone()
    conn.close()
    return dict(row) if row else None
