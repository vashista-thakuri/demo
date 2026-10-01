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
    # Normal input should return the correct product
    product = get_product_by_sku("SKU-100")
    assert product is not None
    assert product["sku"] == "SKU-100"
    # Malicious input attempting SQL injection should not succeed
    injection_sku = "' OR '1'='1" 
    result = get_product_by_sku(injection_sku)
    # Expecting None or no unauthorized product, confirming injection is prevented
    assert result is None
    # Additional check: ensure that executing the malicious input does not crash the system or return an unintended record
    result2 = get_product_by_sku("; DROP TABLE products;--")
    assert result2 is None
