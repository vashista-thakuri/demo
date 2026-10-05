from src.database import get_connection, init_db


def get_product_by_sku(sku: str) -> dict | None:
    init_db()
    conn = get_connection()
    query = "SELECT id, sku, name, price_cents FROM products WHERE sku = ?"
    row = conn.execute(query, (sku,)).fetchone()
    conn.close()
    return dict(row) if row else None
