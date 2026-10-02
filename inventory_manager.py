inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]


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


