import pytest

from src.Product import Product




def test_product_init():
    p = Product("Телефон", "Смартфон", 10000, 5)
    assert p.name == "Телефон"
    assert p.quantity == 5


def test_product_creation():
    p = Product("Книга", "Детектив", 500, 10)
    assert p.name == "Книга"
    assert p.description == "Детектив"
    assert p.price == 500
    assert p.quantity == 10


def test_price_setter_positive():
    p = Product("Товар", "Описание", 1000, 2)
    p.price = 2000
    assert p.price == 2000


def test_price_setter_negative_or_zero(capsys):
    p = Product("Товар", "Описание", 1000, 2)
    p.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 1000
    p.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 1000


def test_repr_format():
    p = Product("Мяч", "Футбольный", 300, 5)
    result = p.__repr__()
    assert "Product(name='Мяч'" in result
    assert "description='Футбольный'" in result
    assert "price=300" in result
    assert "quantity=5" in result


def test_new_product_creates_new():
    # Очищаем список продуктов перед запуском теста
    if hasattr(Product, "_Product__products"):
        Product._Product__products.clear()
    else:
        Product.products.clear()

    data = {"name": "Велосипед", "description": "Горный", "price": 15000, "quantity": 1}
    p = Product.new_product(data)
    products = Product._Product__products if hasattr(Product, "_Product__products") else Product.products
    assert p in products
    assert p.name == "Велосипед"
    assert p.quantity == 1


def test_new_product_updates_existing():
    # Очищаем список продуктов перед запуском теста
    if hasattr(Product, "_Product__products"):
        Product._Product__products.clear()
    else:
        Product.products.clear()

    # Добавляем первый продукт
    product = Product("Часы", "Умные", 2000, 3)
    data = {"name": "Часы", "description": "Умные", "price": 2500, "quantity": 2}
    p = Product.new_product(data)
    products = Product._Product__products if hasattr(Product, "_Product__products") else Product.products
    assert len(products) == 1
    assert p.quantity == 5  # Было 3, добавили 2
    assert p.price == 2500  # price становится больше


def test_new_product_without_list():
    data = {"name": "Ручка", "description": "Синяя", "price": 50, "quantity": 12}
    p = Product.new_product(data)
    assert p.name == "Ручка"
    assert p.quantity == 12



@pytest.fixture
def product1():
    return Product("Товар 1", "Описание 1", 100, 5)

@pytest.fixture
def product2():
    return Product("Товар 2", "Описание 2", 200, 2)

def test_str(product1):
    assert str(product1) == "Товар 1, 100 руб. Остаток: 5 шт."

def test_add(product1, product2):
    # 100 * 5 + 200 * 2 = 500 + 400 = 900
    assert product1 + product2 == 900

def test_add_wrong_type(product1):
    with pytest.raises(TypeError):
        _ = product1 + 10  # 10 — не Product

