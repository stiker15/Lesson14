
from src.Product import Product


def test_product_init():
    p = Product("Телефон", "Смартфон", 10000, 5)
    assert p.name == "Телефон"
    assert p.quantity == 5
