from products import Product

class Store:
    def __init__(self, products=None):
        """Initialize the store with a list of products."""
        self.products = products if products else []

    def add_product(self, product):
        """adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """remove the product to the store"""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Returns how many items are in the store in total."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
            return total_quantity

    def get_all_products(self):
        """Returns all products in the store that are active"""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """processes an order of multiple products and returns the total cost."""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    # Get all active product
    products = best_buy.get_all_products()
    print("Total quantity in store:", best_buy.get_total_quantity())
    order_cost = best_buy.order([(products[0], 1), (products[1], 2)])
    print(f"Order cost: {order_cost} ")


if __name__ == "__main__":
    main()







