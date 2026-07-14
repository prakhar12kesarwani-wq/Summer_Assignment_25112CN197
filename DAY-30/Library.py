# Mini Library Management System

book_name = []
author = []
quantity = []
issued = []

while True:
    print("\n====== MINI LIBRARY SYSTEM ======")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Library Status")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        b = input("Enter Book Name: ")
        a = input("Enter Author Name: ")
        q = int(input("Enter Quantity: "))

        book_name.append(b)
        author.append(a)
        quantity.append(q)
        issued.append(0)

        print("Book Added Successfully!")

    elif choice == 2:
        if len(book_name) == 0:
            print("Library is Empty!")
        else:
            print("\n======================== LIBRARY BOOKS ========================")
            print("{:<20} {:<20} {:<12} {:<10}".format(
            "Book", "Author", "Available", "Issued"))
            print("-" * 65)

            for i in range(len(book_name)):
                print("{:<20} {:<20} {:<12} {:<10}".format(
                book_name[i],
                author[i],
                quantity[i],
                issued[i]
                ))
    elif choice == 3:
        s = input("Enter Book Name to Search: ")
        found = False

        for i in range(len(book_name)):
            if book_name[i].lower() == s.lower():
                print("\nBook Found!")
                print("Book:", book_name[i])
                print("Author:", author[i])
                print("Available:", quantity[i])
                print("Issued:", issued[i])
                found = True
                break

        if not found:
            print("Book Not Found!")

    elif choice == 4:
        s = input("Enter Book Name to Issue: ")
        found = False

        for i in range(len(book_name)):
            if book_name[i].lower() == s.lower():
                found = True
                if quantity[i] > 0:
                    quantity[i] -= 1
                    issued[i] += 1
                    print("Book Issued Successfully!")
                else:
                    print("Book Not Available!")
                break

        if not found:
            print("Book Not Found!")

    elif choice == 5:
        s = input("Enter Book Name to Return: ")
        found = False

        for i in range(len(book_name)):
            if book_name[i].lower() == s.lower():
                found = True
                if issued[i] > 0:
                    issued[i] -= 1
                    quantity[i] += 1
                    print("Book Returned Successfully!")
                else:
                    print("No Issued Copy to Return!")
                break

        if not found:
            print("Book Not Found!")

    elif choice == 6:
        s = input("Enter Book Name to Delete: ")
        found = False

        for i in range(len(book_name)):
            if book_name[i].lower() == s.lower():
                del book_name[i]
                del author[i]
                del quantity[i]
                del issued[i]
                print("Book Deleted Successfully!")
                found = True
                break

        if not found:
            print("Book Not Found!")

    elif choice == 7:
        total_books = sum(quantity)
        total_issued = sum(issued)

        print("\n===== LIBRARY STATUS =====")
        print("Total Different Books:", len(book_name))
        print("Available Copies:", total_books)
        print("Issued Copies:", total_issued)

    elif choice == 8:
        print("Thank You for Using Library System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")