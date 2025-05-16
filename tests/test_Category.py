
from src.Category import Category
from src.Product import Product


def test_category_init_and_counts():
    start_cat = Category.categories_count
    start_prod = Category.products_count
    p1 = Product("Телефон", "Смартфон", 18000, 5)
    p2 = Product("Планшет", "Android", 10000, 3)
    cat = Category("Электроника", "Гаджеты", [p1, p2])
    assert cat.name == "Электроника"
    assert Category.categories_count == start_cat + 1
    assert Category.products_count >= start_prod + 2
    assert cat.product_count == 2


def test_category_products_count():
    before = Category.products_count
    p = Product("Ноутбук", "Рабочий", 30000, 2)
    cat2 = Category("Компьютеры", "Всё для работы", [p])
    assert Category.products_count == before + 1


def test_add_product_and_count():
    cat = Category("Техника", "Разное")
    p = Product("Утюг", "Паровой", 2500, 1)
    cat.add_product(p)
    assert cat.product_count == 1
    assert "Утюг" in cat.products


def test_products_string_format():
    p = Product("Мышка", "Офисная", 500, 10)
    cat = Category("Периферия", "Комплектующие", [p])
    assert "Мышка, 500 руб. Остаток: 10 шт." in cat.products


def test_repr_contains_category_name():
    p = Product("Экран", "LED", 8000, 2)
    cat = Category("Дисплеи", "Техника", [p])
    assert "Category(name='Дисплеи'" in cat.__repr__()
