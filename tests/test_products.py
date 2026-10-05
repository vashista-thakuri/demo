from src.products import get_product_by_sku


def test_get_product_by_sku_returns_correct_product():
    product = get_product_by_sku("SKU-100")

    assert product is not None
    assert product["sku"] == "SKU-100"
    assert product["name"] == "Widget"


def test_get_product_by_sku_unknown_sku_returns_none():
    product = get_product_by_sku("no-such-sku")

    assert product is None


def test_sql_injection_prevention_with_malicious_sku():
    malicious_input = "' OR '1'='1"  # Typical SQL injection attempt
    product = get_product_by_sku(malicious_input)
    # Assert that the injection does not return a valid product
    assert product is None
