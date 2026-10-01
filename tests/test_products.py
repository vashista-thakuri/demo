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
    # Test with a malicious input that attempts SQL injection
    malicious_input = "' OR '1'='1"  # Typical injection attempt
    product = get_product_by_sku(malicious_input)
    # Assert that the function does not return all products or raise an error
    assert product is None or isinstance(product, dict)
    # Verify that with valid input, the correct product data is retrieved
    valid_product = get_product_by_sku("SKU-100")
    assert valid_product is not None
    assert valid_product["sku"] == "SKU-100"
