

class Category:
    categories_count = 0
    products_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.categories_count += 1
        Category.products_count += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.products_count += 1

    @property
    def products(self):
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    @property
    def product_count(self):
        return len(self.__products)

    def __repr__(self):
        return (
            f"Category(name={self.name!r}, "
            f"description={self.description!r},"
            f" products={self.products!r})"
        )
