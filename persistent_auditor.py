def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            if len(lines) == 0:
                return 0, []

            inventory = int(lines[0].strip())
            transaction_history = []

            for line in lines[1:]:
                transaction_history.append(int(line.strip()))

            return inventory, transaction_history

    except FileNotFoundError:
        return 0, []


inventory, transaction_history = load_inventory()
failed_entries = 0
deliveries_processed = 0

orders = []


def display_orders(orders):
    print("\nCurrent Orders:")

    if len(orders) == 0:
        print("No orders found.")
    else:
        for order in orders:
            print(order[0], order[1], order[2], sep=", ")


def get_valid_input():
    user_input = input("Enter stock quantity or Enter 'quit' to exit: ")

    if user_input.lower() == "quit":
        return "quit"

    if not user_input.lstrip("-").isdigit():
        print("Invalid input. Please enter a valid stock quantity (Integer).")
        return None

    quantity = int(user_input)

    if quantity < 0:
        print("Invalid input. Do not put in negative numbers for stock quantity.")
        return None

    return quantity


def process_delivery(current_total, new_value):
    new_total = current_total + new_value

    return new_total


def calculate_tax(amount):
    tax = amount * 0.10

    return tax


def generate_report(total_units, failed_attempts, deliveries_processed):
    print("\nTotal Units Processed:", total_units)
    print("Total Deliveries Processed:", deliveries_processed)
    print("Number of Failed/Rejected Entries:", failed_attempts)


display_orders(orders)


def get_product_name():
    product_name = input("\nEnter Product Name or 'quit' to exit: ")

    if product_name.lower() == "quit":
        return "quit"

    if product_name.strip() == "":
        print("Invalid input. Product name cannot be empty.")
        return None

    return product_name.strip()


def get_next_order_id(orders):
    if len(orders) == 0:
        return 1001

    order_ids = []

    for order in orders:
        order_ids.append(order[0])

    return max(order_ids) + 1


while True:
    product_name = get_product_name()

    if product_name == "quit":
        generate_report(inventory, failed_entries, deliveries_processed)
        break

    elif product_name is None:
        failed_entries += 1
        continue

    value = get_valid_input()

    if value == "quit":
        generate_report(inventory, failed_entries, deliveries_processed)
        break

    elif value is None:
        failed_entries += 1
        continue

    else:
        order_id = get_next_order_id(orders)

        new_order = [order_id, product_name, value]

        orders.append(new_order)
        transaction_history.append(value)

        inventory = process_delivery(inventory, value)

        tax = calculate_tax(value)
        deliveries_processed += 1

        print("\nNew Order Added:")
        print(new_order[0], new_order[1], new_order[2], sep=", ")

        print("Tax for this delivery:", round(tax, 2))
        print("Current Inventory Total:", inventory)

        display_orders(orders)

        if inventory > 500:
            print("Overstock Alert! Inventory has exceeded 500 units.")
            break
