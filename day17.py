products = []


# Add Product
def add_product():
    try:
        product_id = int(input("Enter product ID: "))

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

        print("Product added successfully.")

    except ValueError:
        print("Invalid input. Please enter the correct data type.")


# View Products
def view_products():
    if not products:
        print("No products available.")
        return

    print("\n--- Product List ---")

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
                    print("Product price updated successfully.")

                elif choice == "2":
                    new_quantity = int(input("Enter new quantity: "))

                    if new_quantity < 0:
                        print("Quantity cannot be negative.")
                        return

                    product["quantity"] = new_quantity
                    print("Product quantity updated successfully.")

                else:
                    print("Invalid choice.")

                return

        print("Product not found.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Main Menu
while True:

    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        update_product()

    elif choice == "4":
        print("Exiting Inventory Management System.")
        break

    else:
        print("Invalid choice. Please try again.")