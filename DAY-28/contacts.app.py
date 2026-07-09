contacts = {}

while True:
    print("\n----- Contact Management System -----")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        phone = input("Enter Phone Number: ")

        if phone in contacts:
            print("Contact already exists!")
        else:
            name = input("Enter Name: ")
            email = input("Enter Email: ")

            contacts[phone] = {
                "Name": name,
                "Email": email
            }

            print("Contact added successfully!")

    elif choice == 2:
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for phone, details in contacts.items():
                print("Phone Number:", phone)
                print("Name:", details["Name"])
                print("Email:", details["Email"])
                print("--------------------------")

    elif choice == 3:
        phone = input("Enter Phone Number to search: ")

        if phone in contacts:
            print("Name:", contacts[phone]["Name"])
            print("Email:", contacts[phone]["Email"])
        else:
            print("Contact not found.")

    elif choice == 4:
        phone = input("Enter Phone Number to update: ")

        if phone in contacts:
            name = input("Enter New Name: ")
            email = input("Enter New Email: ")

            contacts[phone]["Name"] = name
            contacts[phone]["Email"] = email

            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == 5:
        phone = input("Enter Phone Number to delete: ")

        if phone in contacts:
            del contacts[phone]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == 6:
        print("Exiting Contact Management System...")
        break

    else:
        print("Invalid choice! Please try again.")