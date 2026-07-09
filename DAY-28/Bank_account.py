accounts = {}

while True:
    print("\n----- Bank Account Management System -----")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Delete Account")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            print("Account already exists!")
        else:
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))

            accounts[acc_no] = {
                "Name": name,
                "Balance": balance
            }

            print("Account created successfully!")

    elif choice == 2:
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            print("Account Number:", acc_no)
            print("Account Holder:", accounts[acc_no]["Name"])
            print("Balance:", accounts[acc_no]["Balance"])
        else:
            print("Account not found.")

    elif choice == 3:
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            amount = float(input("Enter Amount to Deposit: "))

            accounts[acc_no]["Balance"] += amount

            print("Amount deposited successfully!")
            print("Current Balance:", accounts[acc_no]["Balance"])
        else:
            print("Account not found.")

    elif choice == 4:
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            amount = float(input("Enter Amount to Withdraw: "))

            if amount <= accounts[acc_no]["Balance"]:
                accounts[acc_no]["Balance"] -= amount
                print("Withdrawal successful!")
                print("Remaining Balance:", accounts[acc_no]["Balance"])
            else:
                print("Insufficient Balance.")
        else:
            print("Account not found.")

    elif choice == 5:
        acc_no = input("Enter Account Number to Delete: ")

        if acc_no in accounts:
            del accounts[acc_no]
            print("Account deleted successfully!")
        else:
            print("Account not found.")

    elif choice == 6:
        print("Thank you for using Bank Account Management System!")
        break

    else:
        print("Invalid choice! Please try again.")