# ================== MINI TRAIN TICKET BOOKING SYSTEM ==================

train_no = []
train_name = []
destination = []
fare = []
available = []
booked = []

# ---------------- Add Train ----------------
def add_train():
    no = int(input("Enter Train Number: "))
    name = input("Enter Train Name: ")
    dest = input("Enter Destination: ")
    f = float(input("Enter Ticket Fare: "))
    seats = int(input("Enter Total Seats: "))

    train_no.append(no)
    train_name.append(name)
    destination.append(dest)
    fare.append(f)
    available.append(seats)
    booked.append(0)

    print("\nTrain Added Successfully!")

# ---------------- Display Trains ----------------
def display_trains():
    if len(train_no) == 0:
        print("\nNo Train Available!")
        return

    print("\n========================================== TRAIN LIST ==========================================")
    print("{:<10} {:<25} {:<30} {:>10} {:>10} {:>10}".format(
        "No", "Train Name", "Destination", "Fare", "Seats", "Booked"))
    print("-" * 100)

    for i in range(len(train_no)):
        print("{:<10} {:<25} {:<30} {:>10.2f} {:>10} {:>10}".format(
            train_no[i],
            train_name[i],
            destination[i],
            fare[i],
            available[i],
            booked[i]
        ))

# ---------------- Search Train ----------------
def search_train():
    no = int(input("Enter Train Number: "))

    for i in range(len(train_no)):
        if train_no[i] == no:
            print("\n========== Train Found ==========")
            print("Train Number :", train_no[i])
            print("Train Name   :", train_name[i])
            print("Destination  :", destination[i])
            print("Fare         : ₹", fare[i])
            print("Available    :", available[i])
            print("Booked       :", booked[i])
            return

    print("Train Not Found!")

# ---------------- Book Ticket ----------------
def book_ticket():
    no = int(input("Enter Train Number: "))

    for i in range(len(train_no)):
        if train_no[i] == no:

            tickets = int(input("Enter Number of Tickets: "))

            if tickets <= available[i]:
                available[i] -= tickets
                booked[i] += tickets

                total = tickets * fare[i]

                print("\nBooking Successful!")
                print("Tickets Booked :", tickets)
                print("Total Amount   : ₹", total)

            else:
                print("Sorry! Only", available[i], "Seats Available.")

            return

    print("Train Not Found!")

# ---------------- Cancel Ticket ----------------
def cancel_ticket():
    no = int(input("Enter Train Number: "))

    for i in range(len(train_no)):
        if train_no[i] == no:

            tickets = int(input("Enter Tickets to Cancel: "))

            if tickets <= booked[i]:
                booked[i] -= tickets
                available[i] += tickets
                print("Ticket Cancelled Successfully!")
            else:
                print("Invalid Number of Tickets!")

            return

    print("Train Not Found!")

# ---------------- Delete Train ----------------
def delete_train():
    no = int(input("Enter Train Number to Delete: "))

    for i in range(len(train_no)):
        if train_no[i] == no:
            del train_no[i]
            del train_name[i]
            del destination[i]
            del fare[i]
            del available[i]
            del booked[i]

            print("Train Deleted Successfully!")
            return

    print("Train Not Found!")

# ---------------- Railway Summary ----------------
def railway_summary():

    total_revenue = 0
    total_booked = 0
    total_available = 0

    for i in range(len(train_no)):
        total_revenue += booked[i] * fare[i]
        total_booked += booked[i]
        total_available += available[i]

    print("\n============== RAILWAY SUMMARY ==============")
    print("Total Trains        :", len(train_no))
    print("Available Seats     :", total_available)
    print("Booked Seats        :", total_booked)
    print("Total Revenue (₹)   :", total_revenue)

# ================= MAIN MENU =================

while True:

    print("\n")
    print("=" * 50)
    print("        MINI TRAIN TICKET BOOKING SYSTEM")
    print("=" * 50)
    print("1. Add Train")
    print("2. Display Trains")
    print("3. Search Train")
    print("4. Book Ticket")
    print("5. Cancel Ticket")
    print("6. Delete Train")
    print("7. Railway Summary")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_train()

    elif choice == 2:
        display_trains()

    elif choice == 3:
        search_train()

    elif choice == 4:
        book_ticket()

    elif choice == 5:
        cancel_ticket()

    elif choice == 6:
        delete_train()

    elif choice == 7:
        railway_summary()

    elif choice == 8:
        print("\nThank You for Using Train Ticket Booking System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")