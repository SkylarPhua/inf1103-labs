inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity or Enter 'quit' to exit: ")

    if user_input.lower() == "quit":
        break