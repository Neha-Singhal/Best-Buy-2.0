from abc import ABC, abstractmethod

#Abstract Promotion class
class Promotion(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def apply_promotion(self,product,quantity):
        """Applies promotion and returns discounted price."""
        pass

# Percentage Discount Promotion
class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity

# Second item at half price
class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)

# Buy 2, get 1 free
class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        # For every set of 3 items, 1 is free
        paid_items = quantity - (quantity // 3)
        return paid_items * product.price

