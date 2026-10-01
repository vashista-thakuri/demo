from src.products import get_product_by_sku


def test_get_product_by_sku_returns_correct_product():
    product = get_product_by_sku("SKU-100")

    assert product is not None
    assert product["sku"] == "SKU-100"
    assert product["name"] == "Widget"


def test_get_product_by_sku_unknown_sku_returns_none():
    product = get_product_by_sku("no-such-sku")

    assert product is None


def test_sql_injection_prevention_in_get_product_by_sku():
    malicious_input = "' OR '1'='1"  # malicious input
    product = get_product_by_sku(malicious_input)
    
    # Verify that the function does not return any product for malicious input
    assert product is None
