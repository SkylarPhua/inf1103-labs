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
    print("Total Units Processed:", total_units)
    print("Total Deliveries Processed:", deliveries_processed)
    print("Number of Failed/Rejected Entries:", failed_attempts)

while True:
    value = get_valid_input()

    if value == "quit":
        generate_report(inventory, failed_entries, deliveries_processed)
        break

    elif value is None:
        failed_entries += 1
        continue

    else:
        inventory = process_delivery(inventory, value)
        tax = calculate_tax(value)
        deliveries_processed += 1
        print("Tax for this delivery:", tax)

        if inventory > 500:
                print("Overstock Alert! Inventory has exceeded 500 units.")
                break