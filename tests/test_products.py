from src.products import get_product_by_sku


def test_get_product_by_sku_returns_correct_product():
    product = get_product_by_sku("SKU-100")

    assert product is not None
    assert product["sku"] == "SKU-100"
    assert product["name"] == "Widget"


def test_get_product_by_sku_unknown_sku_returns_none():
    product = get_product_by_sku("no-such-sku")

    assert product is None


def test_get_product_by_sku_sql_injection_protection():
    malicious_sku = "' OR '1'='1"  # Typical injection payload
    product = get_product_by_sku(malicious_sku)

    # Assert that the injection payload does not return an arbitrary product
    # or cause an error; expecting None or no results.
    assert product is None
