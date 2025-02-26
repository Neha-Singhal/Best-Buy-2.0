class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price <= 0:
            raise ValueError("price cannot be negative")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) :
        """Getter function for quantity.Returns the quantity (int)."""
        return self.quantity


    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        if quantity < 0:
            raise ValueError("quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        """Getter function for active.Returns True if the product is active, otherwise False."""
        return self.active


    def activate(self):
        """Activates the product."""
        self.active = True


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def show(self) :
        """Returns a string that represents the product"""
        return f"{self.name}, Price{self.price}, Quantity{self.quantity}"


    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("not enough stock available")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return quantity * self.price


# NonStockedProduct class: inherits from Product
class NonStockedProduct(Product):
    def __init__(self, name, price):
        # Always set quantity to 0 for non-stocked products
        super().__init__(name, price, quantity=0)


    def show(self):
        # Override the show method to reflect the maximum purchase limit
        return f"{self.name}, {self.price},This product is not stocked and quantity is always 0."


    def buy(self, quantity):
        """Allows purchasing without checking stock since it's a non-stocked product."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        return quantity * self.price  # No stock reduction, just price calculation


# LimitedProduct class: inherits from Product
class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum  # Maximum purchase quantity per order


    def show(self):
        # Override the show method to reflect the maximum purchase limit
        return f"{self.name}, Price: {self.price}, Maximum per order: {self.maximum}"


    def buy(self,quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot order more than {self.maximum} of this product.")
        # Call the parent class' buy method to handle quantity and price deduction
        return super().buy(quantity)


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    windows_license = NonStockedProduct("Windows License", price=125)
    shipping_fee = LimitedProduct("Shipping Fee", price=10, quantity=250, maximum=1)

    # Show initial product details
    print(bose.show())
    print(mac.show())
    print(windows_license.show())
    print(shipping_fee.show())

    # Testing the 'buy' method for a limited product
    try:
        print(shipping_fee.buy(2))  # This should raise an exception because maximum is 1
    except ValueError as e:
        print(e)

    # Testing the 'buy' method for a non-stocked product (should always have quantity 0)
    print(windows_license.buy(1))  # Should return 125 (price of one license)
    print(windows_license.show())  # Should show that the product is not stocked

    # Show updated product details
    print(bose.show())
    print(mac.show())
    print(windows_license.show())
    print(shipping_fee.show())


if __name__ == "__main__":
    main()
