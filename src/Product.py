

class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, "
            f"description={self.description!r}, "
            f"price={self._price}, quantity={self.quantity})"
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None):
        # Извлекаем параметры из словаря по ключам
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")

        if products_list is not None:
            for product in products_list:

                if product.name == name:
                    product.quantity += quantity
                    product.price = max(product.price, price)
                return product

            new_product = cls(name, description, price, quantity)
            products_list.append(new_product)
            return new_product

        else:
            return cls(name, description, price, quantity)
