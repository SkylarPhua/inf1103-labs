import json

from product import Product
from inventory import Inventory


def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

        for product_data in data:
            product = Product(
                product_data["id"],
                product_data["name"],
                product_data["price"],
                product_data["stock"],
            )

            inventory.add_product(product)
    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")

    return inventory


def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip().upper()

    if inventory.search_product(product_id):
        print("Product ID already exists")
        return

    product_name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

    except ValueError:
        print("Invalid input. Price must be a number and stock must be an integer.")
        return

    if price < 0 or stock < 0:
        print("Invalid input. Price and stock cannot be negative.")
        return

    product = Product(product_id, product_name, price, stock)

    inventory.add_product(product)

    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip().upper()

    product = inventory.search_product(product_id)

    if product:
        try:
            new_stock = int(input("New Stock Quantity: "))

        except ValueError:
            print("Invalid input. Stock quantity must be an integer.")
            return

        if new_stock < 0:
            print("Invalid input. Stock quantity cannot be negative.")
            return

        product.update_stock(new_stock)

        print("Stock updated successfully!")

    else:
        print("Product not found.")


def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip().upper()

    product = inventory.search_product(product_id)

    if product:
        print("\nProduct Found")
        print("------------------------------------------------")
        product.display_information()
        print("------------------------------------------------")
    else:
        print("Product not found.")


inventory = load_inventory()

while True:
    print("\n========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    option = input("Enter option: ")

    if option == "1":
        inventory.display_all()

    elif option == "2":
        add_product(inventory)

    elif option == "3":
        update_stock(inventory)

    elif option == "4":
        search_product(inventory)

    elif option == "5":
        print("Save inventory will be implemented next.")

    elif option == "6":
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please select an option from 1 to 6.")
