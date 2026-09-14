inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity or Enter 'quit' to exit: ")

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Invalid input. Please enter a valid stock quantity (Integer).")
        failed_entries += 1
        continue

    quantity = int(user_input)