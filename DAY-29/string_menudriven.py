# Menu-Driven String Operations System

text = input("Enter a string: ")

while True:
    print("\n===== STRING OPERATIONS MENU =====")
    print("1. Display String")
    print("2. Convert to Uppercase")
    print("3. Convert to Lowercase")
    print("4. Find Length")
    print("5. Reverse String")
    print("6. Check Palindrome")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        print("String:", text)

    elif choice == 2:
        print("Uppercase:", text.upper())

    elif choice == 3:
        print("Lowercase:", text.lower())

    elif choice == 4:
        print("Length of String:", len(text))

    elif choice == 5:
        print("Reversed String:", text[::-1])

    elif choice == 6:
        if text == text[::-1]:
            print("The string is a Palindrome.")
        else:
            print("The string is not a Palindrome.")

    elif choice == 7:
        print("Program Closed.")
        break

    else:
        print("Invalid choice! Please try again.")