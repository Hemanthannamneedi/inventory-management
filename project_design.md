# Inventory Management System

## 1. Project Objective

The objective of this project is to develop a Python-based Inventory Management System that allows users to manage product information and keep track of available stock.

The system will provide operations such as adding, viewing, searching, updating, and deleting products. It will also allow users to increase or decrease product stock.

The project will use Object-Oriented Programming, file handling, JSON storage, and exception handling.

---

## 2. Features

The system will provide the following features:

1. Add Product
2. View All Products
3. Search Product
4. Update Product
5. Delete Product
6. Add Stock
7. Remove Stock
8. Save Product Data
9. Load Product Data
10. Input Validation and Exception Handling
11. Exit

---

## 3. Product Data Structure

Each product will contain the following information:

- Product ID
- Product Name
- Category
- Price
- Quantity

Example:

{
    "product_id": 101,
    "name": "Laptop",
    "category": "Electronics",
    "price": 55000,
    "quantity": 10
}

---

## 4. Data Storage

The product records will be stored in a JSON file.

File name:

products.json

The program will load existing product data when it starts and save updated data whenever changes are made.

---

## 5. Program Flow

1. Start the application.
2. Load product data from the JSON file.
3. Display the main menu.
4. Ask the user to select an operation.
5. Perform the selected operation.
6. Validate user input.
7. Handle any errors using exception handling.
8. Save changes to the JSON file.
9. Return to the main menu.
10. Exit the application when the user selects Exit.

---

## 6. Main Menu

===== Inventory Management System =====

1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Add Stock
7. Remove Stock
8. Exit

---

## 7. Classes and Modules

### Product Class

The Product class will store product information such as:

- product_id
- name
- category
- price
- quantity

### InventorySystem Class

The InventorySystem class will manage all products and provide methods for:

- add_product()
- view_products()
- search_product()
- update_product()
- delete_product()
- add_stock()
- remove_stock()
- save_products()
- load_products()

---

## 8. Exception Handling

The system will handle incorrect inputs and file-related errors.

Examples:

- Non-numeric product ID
- Invalid price
- Invalid quantity
- Duplicate product ID
- Product not found
- Missing JSON file
- Invalid JSON data

---

## 9. Project Flow

Start
  |
Load product data
  |
Display Menu
  |
Select Operation
  |
  +--> Add Product
  |
  +--> View Products
  |
  +--> Search Product
  |
  +--> Update Product
  |
  +--> Delete Product
  |
  +--> Add Stock
  |
  +--> Remove Stock
  |
  +--> Exit
          |
         End
