import json

products = []
FILE_NAME = "inventory.json"


# Save products to JSON
def save_inventory():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(products, file, indent=4)

        print("Inventory saved successfully.")

    except IOError as e:
        print("Error while saving inventory:", e)


# Load products from JSON
def load_inventory():
    global products

    try:
        with open(FILE_NAME, "r") as file:
            products = json.load(file)

        print("Inventory loaded successfully.")

    except FileNotFoundError:
        products = []
        print("No existing inventory found. Starting with empty inventory.")

    except json.JSONDecodeError:
        products = []
        print("Error: Inventory file contains invalid JSON data.")


# Add Product
def add_product():
    try:
        product_id = int(input("Enter product ID: "))

        # Check duplicate product ID
        for product in products:
            if product["product_id"] == product_id:
                print("Product ID already exists.")
                return

        name = input("Enter product name: ").strip()

        if not name:
            print("Product name cannot be empty.")
            return

        # Check duplicate product name
        for product in products:
            if product["name"].lower() == name.lower():
                print("Product with this name already exists.")
                return

        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        price = float(input("Enter price: "))

        if price < 0:
            print("Price cannot be negative.")
            return

        quantity = int(input("Enter quantity: "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        product = {
            "product_id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }

        products.append(product)

        save_inventory()

        print("Product added successfully.")

    except ValueError:
        print("Invalid input. Please enter valid values.")


# View Products
def view_products():
    if not products:
        print("No products available.")
        return

    print("\n--- Inventory ---")

    for product in products:
        print(
            "ID:", product["product_id"],
            "| Name:", product["name"],
            "| Category:", product["category"],
            "| Price:", product["price"],
            "| Quantity:", product["quantity"]
        )


# Update Product
def update_product():
    try:
        product_id = int(input("Enter product ID to update: "))

        for product in products:

            if product["product_id"] == product_id:

                print("\n1. Update Price")
                print("2. Update Quantity")

                choice = input("Enter your choice: ")

                if choice == "1":
                    new_price = float(input("Enter new price: "))

                    if new_price < 0:
                        print("Price cannot be negative.")
                        return

                    product["price"] = new_price
                    print("Price updated successfully.")

                elif choice == "2":
                    new_quantity = int(input("Enter new quantity: "))

                    if new_quantity < 0:
                        print("Quantity cannot be negative.")
                        return

                    product["quantity"] = new_quantity
                    print("Quantity updated successfully.")

                else:
                    print("Invalid choice.")
                    return

                save_inventory()
                return

        print("Product not found.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Sell Product
def sell_product():
    try:
        product_id = int(input("Enter product ID to sell: "))
        sell_quantity = int(input("Enter quantity to sell: "))

        if sell_quantity <= 0:
            print("Sale quantity must be greater than 0.")
            return

        for product in products:

            if product["product_id"] == product_id:

                if sell_quantity > product["quantity"]:
                    print(
                        "Insufficient stock. Available stock:",
                        product["quantity"]
                    )
                    return

                product["quantity"] -= sell_quantity

                save_inventory()

                print("\nSale completed successfully.")
                print("Product:", product["name"])
                print("Quantity sold:", sell_quantity)
                print("Current stock:", product["quantity"])

                return

        print("Product not found.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


# Main Program

load_inventory()

while True:

    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Sell Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        update_product()

    elif choice == "4":
        sell_product()

    elif choice == "5":
        save_inventory()
        print("Exiting Inventory Management System.")
        break

    else:
        print("Invalid choice. Please try again.")