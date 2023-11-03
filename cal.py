while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mul' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "sub", "mul", "div"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print(f"Result: {num1 + num2}")
        elif user_input == "sub":
            print(f"Result: {num1 - num2}")
        elif user_input == "mul":
            print(f"Result: {num1 * num2}")
        elif user_input == "div":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid input")
    else:
        print("Invalid input")