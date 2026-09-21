import json

FILE_NAME = "inventory.json"


class InventorySystem:
    def __init__(self):
        self.products = []
        self.load_inventory()

    # Save inventory to JSON
    def save_inventory(self):
        try:
            with open(FILE_NAME, "w") as file:
                json.dump(self.products, file, indent=4)

        except IOError as e:
            print("Error saving inventory:", e)

    # Load inventory from JSON
    def load_inventory(self):
        try:
            with open(FILE_NAME, "r") as file:
                self.products = json.load(file)

        except FileNotFoundError:
            self.products = []

        except json.JSONDecodeError:
            print("Error: Invalid inventory file.")
            self.products = []

    # Add product
    def add_product(self):
        try:
            product_id = int(input("Enter product ID: "))

            # Check duplicate ID
            for product in self.products:
                if product["product_id"] == product_id:
                    print("Product ID already exists.")
                    return

            name = input("Enter product name: ").strip()

            if not name:
                print("Product name cannot be empty.")
                return

            # Check duplicate name
            for product in self.products:
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

            self.products.append(product)
            self.save_inventory()

            print("Product added successfully.")

        except ValueError:
            print("Invalid input. Please enter valid values.")

    # View products
    def view_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\n========== INVENTORY ==========")

        for product in self.products:
            print(f"ID       : {product['product_id']}")
            print(f"Name     : {product['name']}")
            print(f"Category : {product['category']}")
            print(f"Price    : ₹{product['price']:.2f}")
            print(f"Quantity : {product['quantity']}")
            print("-" * 30)

    # Update product
    def update_product(self):
        try:
            product_id = int(input("Enter product ID to update: "))

            for product in self.products:
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
                        new_quantity = int(
                            input("Enter new quantity: ")
                        )

                        if new_quantity < 0:
                            print("Quantity cannot be negative.")
                            return

                        product["quantity"] = new_quantity
                        print("Quantity updated successfully.")

                    else:
                        print("Invalid choice.")
                        return

                    self.save_inventory()
                    return

            print("Product not found.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Sell product
    def sell_product(self):
        try:
            product_id = int(input("Enter product ID to sell: "))
            sell_quantity = int(input("Enter quantity to sell: "))

            if sell_quantity <= 0:
                print("Sale quantity must be greater than 0.")
                return

            for product in self.products:

                if product["product_id"] == product_id:

                    if sell_quantity > product["quantity"]:
                        print(
                            "Insufficient stock. "
                            f"Available stock: {product['quantity']}"
                        )
                        return

                    product["quantity"] -= sell_quantity

                    self.save_inventory()

                    print("\nSale completed successfully.")
                    print(f"Product       : {product['name']}")
                    print(f"Quantity sold : {sell_quantity}")
                    print(f"Current stock : {product['quantity']}")

                    return

            print("Product not found.")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # Main menu
    def run(self):
        while True:
            print("\n================================")
            print("   INVENTORY MANAGEMENT SYSTEM")
            print("================================")
            print("1. Add Product")
            print("2. View Products")
            print("3. Update Product")
            print("4. Sell Product")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_product()

            elif choice == "2":
                self.view_products()

            elif choice == "3":
                self.update_product()

            elif choice == "4":
                self.sell_product()

            elif choice == "5":
                self.save_inventory()
                print("Thank you for using the Inventory Management System.")
                break

            else:
                print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    system = InventorySystem()
    system.run()