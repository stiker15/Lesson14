import pytest

from src.Product import Product, Smartphone, LawnGrass




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

def test_add_product_typeerror():
    p1 = Product("Товар1", "Описание", 100, 2)
    class Another(Product):
        pass
    p2 = Another("Товар2", "Описание", 200, 1)
    with pytest.raises(TypeError):
        p1+p2

def test_smartphone_creation():
    s = Smartphone("iPhone 13", "Смартфон", 90000, 5, 98.5, "iPhone 13", 128, "Черный")
    assert s.name == "iPhone 13"
    assert s.description == "Смартфон"
    assert s.price == 90000
    assert s.quantity == 5
    assert s.efficiency == 98.5
    assert s.model == "iPhone 13"
    assert s.memory == 128
    assert s.color == "Черный"

def test_lawngrass_creation():
    g = LawnGrass("Элитная", "Трава", 600, 10, "Россия", 7, "Зеленый")
    assert g.name == "Элитная"
    assert g.description == "Трава"
    assert g.price == 600
    assert g.quantity == 10
    assert g.country == "Россия"
    assert g.germination_period == 7
    assert g.color == "Зеленый"

#Проверка функции str

def test_smartphone_str():
    s = Smartphone("iPhone 13", "Смартфон", 90000, 5, 98.5, "iPhone 13", 128, "Черный")
    assert "iPhone 13" in str(s)
    assert "128ГБ" in str(s)
    assert "Черный" in str(s)

def test_lawngrass_str():
    g = LawnGrass("Элитная", "Трава", 600, 10, "Россия", 7, "Зеленый")
    assert "Элитная" in str(g)
    assert "Россия" in str(g)
    assert "7 дн." in str(g)
    assert "Зеленый" in str(g)

#Проверка метода сложения

def test_smartphone_add():
    s1 = Smartphone("Model1", "Desc", 100, 2, 90, "M1", 128, "Grey")
    s2 = Smartphone("Model2", "Desc", 200, 1, 92, "M2", 256, "Black")
    assert s1 + s2 == 100 * 2 + 200 * 1

def test_lawngrass_add():
    g1 = LawnGrass("G1", "Grass", 10, 2, "RU", 7, "Green")
    g2 = LawnGrass("G2", "Grass", 20, 3, "KZ", 8, "Dark Green")
    assert g1 + g2 == 10 * 2 + 20 * 3