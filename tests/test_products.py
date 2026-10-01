from src.products import get_product_by_sku


def test_get_product_by_sku_returns_correct_product():
    product = get_product_by_sku("SKU-100")

    assert product is not None
    assert product["sku"] == "SKU-100"
    assert product["name"] == "Widget"


def test_get_product_by_sku_unknown_sku_returns_none():
    product = get_product_by_sku("no-such-sku")

    assert product is None


def test_malicious_sql_injection_prevention():
    malicious_sku = "' OR '1'='1"  # typical injection attempt
    product = get_product_by_sku(malicious_sku)
    
    # Expect no product returned for malicious input if query is properly parameterized
    assert product is None
