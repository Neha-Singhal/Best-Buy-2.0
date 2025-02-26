import products
import store


def main():
    """ setup initial stock of inventory"""
    product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)

    ]

    best_buy = store.Store(product_list)
    start(best_buy)


def start(store_obj):
    """Displays the store menu and handles user interaction."""
    while True:
        print("Store Menu")
        print("------------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("Invalid choice.please choose a valid option")
            continue

        if choice == 1:
            print("\n------ Available Products ------")
            available_products = store_obj.get_all_products()
            for idx, product in enumerate(available_products, start=1):
                print(f"{idx}. {product.name}, Price: ${product.price:.2f}, Quantity: {product.quantity}")

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
                print(f"{idx}. {product.name}, Price: ${product.price:.2f}, Quantity: {product.quantity}")

            print("\nWhen you want to finish ordering, enter empty text.")

            while True:
                product_name = input("\nWhich product do you want? ").strip().lower()
                if product_name == "":
                    break

                product = next((p for p in available_products if p.name.lower() == product_name), None)

                if not product:
                    print(f"Error: Product not found! Please enter a valid product name.")
                    continue

                try:
                    quantity = int(input(f"Enter quantity of {product.name}: "))

                    #check enough stock is available

                    if quantity > product.get_quantity():
                        print(f"Error: Not enough stock! Only {product.get_quantity()} available.")
                        continue

                    shopping_list.append((product, quantity))
                    print(f"Added {quantity} {product_name} to your cart.")
                except ValueError:
                    print("Error: Please enter a valid number for quantity.")

            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print(f"\nTotal price of your order: ${total_price:.2f}")
                except Exception as e:
                    print(f"Error processing order: {e}")

            # Ask user if they want to continue ordering or return to the menu
            cont = input("\nWould you like to order more items? (yes/no): ").strip().lower()
            if cont != "yes":
                break

        elif choice == 4:
            print("Thank you for shopping with us! Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()






