

class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, "
            f"description={self.description!r}, "
            f"price={self.price}, quantity={self.quantity})"
        )
