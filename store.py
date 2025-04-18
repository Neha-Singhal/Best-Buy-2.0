from products import Product, NonStockedProduct, LimitedProduct
from promotion import PercentDiscount
from collections import defaultdict

class Store:
    def __init__(self, products=None):
        """Initialize the store with a list of products."""
        self.products = products if products else []

    def add_product(self, product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes the product from the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Returns how many items are in the store in total."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """Returns all products in the store that are active."""
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list):
        """Processes an order of multiple products and returns the total cost."""
        total_price = 0
        for product, quantity in shopping_list:
            if not isinstance(product, NonStockedProduct):
                """Ensure enough stock is available before processing the order"""
                if product.get_quantity() < quantity:
                    print(
                        f"Error: Not enough stock for {product._name}. Available: {product.get_quantity()}, Requested: {quantity}"
                    )
                    continue

            """ Process the order and calculate price with promotion"""
            total_price += product.buy(quantity)

        return total_price

def merge_cart_items(cart_items):
    """Merge quantities of the same product in the shopping cart."""
    merged = defaultdict(int)
    for product, quantity in cart_items:
        merged[product] += quantity
    return list(merged.items())

def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    # Get all active products
    products = best_buy.get_all_products()
    print("Total quantity in store:", best_buy.get_total_quantity())

    # Add duplicate items intentionally
    raw_cart = [(products[0], 1), (products[1], 1), (products[1], 1)]  # Bose added twice
    merged_cart = merge_cart_items(raw_cart)

    # Test the order functionality
    order_cost = best_buy.order([(products[0], 1), (products[1], 2)])
    print(f"Order cost: ${order_cost:.2f}")



if __name__ == "__main__":
    main()