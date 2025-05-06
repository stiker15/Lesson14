

class Category:
    categories_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.categories_count += 1
        Category.products_count += len(products)

    def __repr__(self):
        return (
            f"Category(name={self.name!r}, "
            f"description={self.description!r},"
            f" products={self.products!r})"
        )
