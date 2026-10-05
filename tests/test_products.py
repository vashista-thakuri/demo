from src.products import get_product_by_sku


def test_get_product_by_sku_returns_correct_product():
    product = get_product_by_sku("SKU-100")

    assert product is not None
    assert product["sku"] == "SKU-100"
    assert product["name"] == "Widget"


def test_get_product_by_sku_unknown_sku_returns_none():
    product = get_product_by_sku("no-such-sku")

    assert product is None


def test_get_product_by_sku_prevents_sql_injection():
    malicious_input = "' OR '1'='1"
    product = get_product_by_sku(malicious_input)
    
    # Ensure that no product is returned for malicious input
    assert product is None
