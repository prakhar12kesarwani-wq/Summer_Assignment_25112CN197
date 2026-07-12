# Menu-Driven Calculator

while True:
    print("\n===== MENU DRIVEN CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 6:
        print("Calculator Closed.")
        break

    if choice >= 1 and choice <= 5:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", num1 + num2)

        elif choice == 2:
            print("Result =", num1 - num2)

        elif choice == 3:
            print("Result =", num1 * num2)

        elif choice == 4:
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Error! Division by zero is not allowed.")

        elif choice == 5:
            if num2 != 0:
                print("Result =", num1 % num2)
            else:
                print("Error! Modulus by zero is not allowed.")

    else:
        print("Invalid Choice! Please select a number between 1 and 6.")