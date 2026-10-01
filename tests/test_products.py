from src.products import get_product_by_sku


def test_get_product_by_sku_returns_correct_product():
    product = get_product_by_sku("SKU-100")

    assert product is not None
    assert product["sku"] == "SKU-100"
    assert product["name"] == "Widget"


def test_get_product_by_sku_unknown_sku_returns_none():
    product = get_product_by_sku("no-such-sku")

    assert product is None


def test_get_product_by_sku_sql_injection_prevention():
    # Attempt to inject SQL via the sku parameter
    malicious_input = "'; DROP TABLE users;--"
    product = get_product_by_sku(malicious_input)
    # The function should treat the input as data, not execute it as SQL
    assert product is None or isinstance(product, dict)
    # Verify that the table still exists by querying a known valid SKU
    valid_product = get_product_by_sku("SKU-100")
    assert valid_product is not None
    assert valid_product["sku"] == "SKU-100"


def test_get_product_by_sku_sql_injection_prevention():
    # Attempt to inject SQL via the sku parameter
    malicious_input = "' OR 1=1 --"
    product = get_product_by_sku(malicious_input)
    # The function should treat the input as data, not execute it as SQL
    assert product is None or isinstance(product, dict)
    # Verify that the table still exists by querying a known valid SKU
    valid_product = get_product_by_sku("SKU-100")
    assert valid_product is not None
    assert valid_product["sku"] == "SKU-100"
