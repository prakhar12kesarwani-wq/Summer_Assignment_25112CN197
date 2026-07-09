library = {}

while True:
    print("\n----- Library Management System -----")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = input("Enter Book ID: ")

        if book_id in library:
            print("Book already exists!")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            quantity = int(input("Enter Quantity: "))

            library[book_id] = {
                "Title": title,
                "Author": author,
                "Quantity": quantity
            }

            print("Book added successfully!")

    elif choice == 2:
        if len(library) == 0:
            print("No books available.")
        else:
            print("\nLibrary Books:")
            for book_id, details in library.items():
                print("Book ID:", book_id)
                print("Title:", details["Title"])
                print("Author:", details["Author"])
                print("Quantity:", details["Quantity"])
                print("---------------------------")

    elif choice == 3:
        book_id = input("Enter Book ID to search: ")

        if book_id in library:
            print("Title:", library[book_id]["Title"])
            print("Author:", library[book_id]["Author"])
            print("Quantity:", library[book_id]["Quantity"])
        else:
            print("Book not found.")

    elif choice == 4:
        book_id = input("Enter Book ID to issue: ")

        if book_id in library:
            if library[book_id]["Quantity"] > 0:
                library[book_id]["Quantity"] -= 1
                print("Book issued successfully!")
                print("Remaining Quantity:", library[book_id]["Quantity"])
            else:
                print("Book is out of stock.")
        else:
            print("Book not found.")

    elif choice == 5:
        book_id = input("Enter Book ID to return: ")

        if book_id in library:
            library[book_id]["Quantity"] += 1
            print("Book returned successfully!")
            print("Available Quantity:", library[book_id]["Quantity"])
        else:
            print("Book not found.")

    elif choice == 6:
        book_id = input("Enter Book ID to delete: ")

        if book_id in library:
            del library[book_id]
            print("Book deleted successfully!")
        else:
            print("-----------------")
            print("Book not found.")

    elif choice == 7:
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice! Please try again.")