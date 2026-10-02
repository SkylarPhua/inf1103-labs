import json


def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

        return inventory

    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")

        return []


def save_inventory(inventory):
    print("\nSaving inventory...")

    with open("inventory.json", "w") as file:
        json.dump(inventory, file)

    print("Inventory saved successfully to inventory.json.")


inventory = load_inventory()


def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")

    for product in inventory:
        print(
            "ID:",
            product["id"],
            "| Name:",
            product["name"],
            "| Price: $" + format(product["price"], ".2f"),
            "| Stock:",
            product["stock"],
        )

    print("------------------------------------------------")


def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip().upper()

    for product in inventory:
        if product["id"] == product_id:
            print("Product ID already exists.")
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

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock,
    }

    inventory.append(new_product)

    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip().upper()

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print("\nName:", product["name"])
            print("Current Stock:", product["stock"])

            try:
                new_stock = int(input("New Stock Quantity: "))

            except ValueError:
                print("Invalid input. Stock quantity must be an integer.")
                return

            if new_stock < 0:
                print("Invalid input. Stock quantity cannot be negative.")
                return

            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")


def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip().upper()

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found")
            print("------------------------------------------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price: $" + format(product["price"], ".2f"))
            print("Stock:", product["stock"])
            print("------------------------------------------------")
            return

    print("Product not found.\n")


display_all(inventory)