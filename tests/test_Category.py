
from src.Category import Category
from src.Product import Product


def test_category_init_and_counts():
    start_cat = Category.categories_count
    start_prod = Category.products_count
    p1 = Product("Телефон", "Смартфон", 18000, 5)
    p2 = Product("Планшет", "Android", 10000, 3)
    cat = Category("Электроника", "Гаджеты", ([p1], [p2]))
    assert cat.name == "Электроника"
    assert len(cat.products) == 2
    assert Category.categories_count == start_cat + 1
    assert Category.products_count >= start_prod + 2


def test_category_products_count():
    before = Category.products_count
    p = Product("Ноутбук", "Рабочий", 30000, 2)
    cat2 = Category("Компьютеры", "Всё для работы", [p])
    assert Category.products_count == before + 1
