

class Product:

    __products = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.__products.append(self)



    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @property
    def products(self):
        info = ''
        for product in Product.__products:
            info += f"{product.name}, {product.__price} руб. Остаток: {product.quantity} шт.\n"
        return info

    @classmethod
    def new_product(cls, product_data: dict):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")

        for product in cls.__products:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

            new_product = cls(name, description, price, quantity)
            return new_product

        else:
            return cls(name, description, price, quantity)

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, "
            f"description={self.description!r}, "
            f"price={self.__price}, quantity={self.quantity})"
        )

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price*self.quantity + other.price*other.quantity


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."