from promotion import Promotion

class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price <= 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self._name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def __str__(self):
        """Returns a readable string representation of the product."""
        promo_info = f" - Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self._name}, Price: ${self.price:.2f}, Quantity: {self.quantity}{promo_info}"

    def __repr__(self):
        """Returns a developer-friendly representation of the object."""
        return f"Product(name='{self._name}', price={self.price}, quantity={self.quantity})"

    def get_quantity(self):
        """Getter function for quantity. Returns the quantity (int)."""
        return self.quantity

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Getter function for active. Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def get_promotion(self):
        """Returns the current promotion of the product."""
        return self.promotion

    def set_promotion(self, promotion):
        from promotion import Promotion  # Import inside the method to avoid circular import
        if not isinstance(promotion, Promotion):
            raise TypeError("Invalid promotion type.")
        self.promotion = promotion

    def show(self):
        """Returns a string that represents the product."""
        promo_info = f"Promotion: {self.promotion.name}" if self.promotion else "Promotion: None"
        return f"{self._name}, Price: ${self.price}, Quantity: {self.quantity}, {promo_info}"


    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")

        # Apply promotion if available
        total_price = self.promotion.apply_promotion(self, quantity) if self.promotion else self.price * quantity

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price


# NonStockedProduct class: inherits from Product
class NonStockedProduct(Product):
    def __init__(self, name, price):
        # Always set quantity to 0 for non-stocked products
        super().__init__(name, price, quantity=0)

    def __str__(self):
        promo_info = f" - Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self._name}, Price: ${self.price:.2f}, This product is not stocked."


    def __repr__(self):
        return f"NonStockedProduct(name='{self._name}', price={self.price})"


    def show(self):
        """Override the show method to reflect unlimited purchase capability"""
        promo_info = f" - Promotion: {self.promotion.name}" if self.promotion else " - Promotion: None"
        return f"{self._name}, Price: ${self.price:.2f}, Quantity: Unlimited{promo_info}"

    def buy(self, quantity):
        """Allows purchasing without checking stock since it's a non-stocked product."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

# LimitedProduct class: inherits from Product
class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum  # Maximum purchase quantity per order

    def __str__(self):
        return f"{self._name}, Price: ${self.price:.2f}, Maximum per order: {self.maximum}"

    def __repr__(self):
        return f"LimitedProduct(name='{self._name}', price={self.price}, maximum={self.maximum})"

    def show(self):
        """Override the show method to reflect the maximum purchase limit"""
        promo_info = f"Promotion: {self.promotion.name}" if self.promotion else "Promotion: None"
        return f"{self._name}, Price: ${self.price}, Limited to {self.maximum} per order!, {promo_info}"

    def buy(self, quantity):
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