inventory = 0
failed_entries = 0

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

while True:
    value = get_valid_input()

    if value == "quit":
        break

    elif value is None:
        failed_entries += 1
        continue

    else:
        inventory = process_delivery(inventory, value)
        tax = calculate_tax(value)
        print("Tax for this delivery:", tax)