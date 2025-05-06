import json
from src.Category import Category
from src.Product import Product


def load_categories_from_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    categories = []
    for cat in data:
        products = [
            Product(p["name"],
                    p["description"],
                    p["price"],
                    p["quantity"])
            for p in cat["products"]
        ]
        category = Category(cat["name"], cat["description"], products)
        categories.append(category)
    return categories


cats = load_categories_from_json("../data/products.json")
print(cats)

