from products import Product, NonStockedProduct, LimitedProduct
from promotion import PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store


def main():
    """Main function to set up the store, add products, apply promotions, and process orders."""

    # Create products
    macbook = Product("MacBook Air M2", price=1450, quantity=100)
    earbuds = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel_phone = Product("Google Pixel 7", price=500, quantity=250)
    windows_license = NonStockedProduct("Windows License", price=125)
    shipping_fee = LimitedProduct("Shipping Fee", price=10, quantity=250, maximum=1)

    # Create promotions
    discount_10_percent = PercentDiscount("10% Off", percent=10)
    second_half_price = SecondHalfPrice("Second Item Half Price")
    buy_two_get_one = ThirdOneFree("Buy 2, Get 1 Free")

    # Apply promotions to products
    macbook.set_promotion(discount_10_percent)
    earbuds.set_promotion(second_half_price)
    pixel_phone.set_promotion(buy_two_get_one)
    windows_license.set_promotion(PercentDiscount("30% Off", percent=30))  # Apply promotion to NonStockedProduct

    # Initialize the store with products
    best_buy = Store([macbook, earbuds, pixel_phone, windows_license, shipping_fee])

    # Start the store menu
    start(best_buy)


def start(store_obj):
    """Displays the store menu and handles user interaction."""
    while True:
        print("\nStore Menu")
        print("------------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            continue

        if choice == 1:
            print("\n------ Available Products ------")
            available_products = store_obj.get_all_products()
            for idx, product in enumerate(available_products, start=1):
                print(f"{idx}. {product.show()}")  # __str__ method ensures readable output

        elif choice == 2:
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal amount of products in store: {total_quantity}")

        elif choice == 3:
            shopping_list = []
            available_products = store_obj.get_all_products()

            if not available_products:
                print("No products available for purchase.")
                continue

            print("\n------ Available Products ------")
            for idx, product in enumerate(available_products, start=1):
                print(f"{idx}. {product.show()}")

            while True:
                product_input = input("\nWhich product # do you want?").strip()
                if product_input == "":
                    break

                product = None

                # Check if the input is a number (numeric selection)
                if product_input.isdigit():
                    product_number = int(product_input)
                    if 1 <= product_number <= len(available_products):
                        product = available_products[product_number - 1]
                    else:
                        print("Invalid product number. Please enter a valid number.")
                        continue
                else:
                    # Check if input matches a product name
                    product = next((p for p in available_products if p._name.lower() == product_input.lower()), None)

                if not product:
                    print("Error: Product not found! Please enter a valid product name.")
                    continue

                try:
                    quantity = int(input("What amount do you want? "))
                    if quantity <= 0:
                        print("Error: Quantity must be greater than zero.")
                        continue

                    # Check for LimitedProduct restrictions
                    if isinstance(product, LimitedProduct) and quantity > product.maximum:
                        print(f"Error: Cannot order more than {product.maximum} of this product.")
                        continue
                    elif not isinstance(product, NonStockedProduct) and quantity > product.get_quantity():
                        print(f"Error: Not enough stock! Only {product.get_quantity()} available.")
                        continue

                    shopping_list.append((product, quantity))
                    print(f"Added {quantity} {product._name} to your cart.")
                except ValueError:
                    print("Error: Please enter a valid number for quantity.")

            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print(f"**********")
                    print(f"Order made! Total Payment: ${total_price:.2f}")
                except Exception as e:
                    print(f"Error processing order: {e}")


        elif choice == 4:
            print("Thank you for shopping with us! Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()