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

while True:
    value = get_valid_input()

    if value == "quit":
        break

    elif value is None:
        failed_entries += 1
        continue