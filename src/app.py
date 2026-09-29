import sys

from src.products import get_product_by_sku


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m src.app <sku>")
        return 1
    product = get_product_by_sku(argv[1])
    if product is None:
        print("product not found")
        return 0
    print(f"{product['sku']} {product['name']} price_cents={product['price_cents']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
