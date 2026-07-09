tickets = {}

while True:
    print("\n----- Ticket Booking System -----")
    print("1. Add Ticket")
    print("2. View Tickets")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. Delete Ticket")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ticket_id = input("Enter Ticket ID: ")

        if ticket_id in tickets:
            print("Ticket already exists!")
        else:
            event = input("Enter Event/Movie Name: ")
            price = float(input("Enter Ticket Price: "))
            quantity = int(input("Enter Number of Tickets: "))

            tickets[ticket_id] = {
                "Event": event,
                "Price": price,
                "Quantity": quantity
            }

            print("Ticket added successfully!")

    elif choice == 2:
        if len(tickets) == 0:
            print("No tickets available.")
        else:
            print("\nAvailable Tickets:")
            for ticket_id, details in tickets.items():
                print("Ticket ID:", ticket_id)
                print("Event:", details["Event"])
                print("Price:", details["Price"])
                print("Available Tickets:", details["Quantity"])
                print("----------------------------")

    elif choice == 3:
        ticket_id = input("Enter Ticket ID to book: ")

        if ticket_id in tickets:
            qty = int(input("How many tickets do you want to book? "))

            if qty <= tickets[ticket_id]["Quantity"]:
                tickets[ticket_id]["Quantity"] -= qty
                total = qty * tickets[ticket_id]["Price"]

                print("Booking Successful!")
                print("Total Amount:", total)
                print("Remaining Tickets:", tickets[ticket_id]["Quantity"])
            else:
                print("Not enough tickets available.")
        else:
            print("Ticket not found.")

    elif choice == 4:
        ticket_id = input("Enter Ticket ID to cancel: ")

        if ticket_id in tickets:
            qty = int(input("Enter number of tickets to cancel: "))
            tickets[ticket_id]["Quantity"] += qty

            print("Ticket cancellation successful!")
            print("Available Tickets:", tickets[ticket_id]["Quantity"])
        else:
            print("Ticket not found.")

    elif choice == 5:
        ticket_id = input("Enter Ticket ID to delete: ")

        if ticket_id in tickets:
            del tickets[ticket_id]
            print("Ticket deleted successfully!")
        else:
            print("Ticket not found.")

    elif choice == 6:
        print("Exiting Ticket Booking System...")
        break

    else:
        print("Invalid choice! Please try again.")       