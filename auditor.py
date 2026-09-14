inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity or Enter 'quit' to exit: ")

    if user_input.lower() == "quit":
        break

    if not user_input.lstrip("-").isdigit():
        print("Invalid input. Please enter a valid stock quantity (Integer).")
        failed_entries += 1
        continue

    quantity = int(user_input)

    if quantity < 0:
        print("Invalid input. Do not put in negative numbers for stock quantity.")
        failed_entries += 1
        continue

    inventory += quantity