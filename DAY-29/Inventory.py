# Inventory Management System with Billing

inventory = {}

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Display Inventory")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Generate Bill")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        inventory[product] = {"quantity": quantity, "price": price}
        print("Product added successfully.")

    elif choice == 2:
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("\nProduct\tQuantity\tPrice")
            print("-------------------------------------")
            for product, details in inventory.items():
                print(product, "\t", details["quantity"], "\t\t", details["price"])

    elif choice == 3:
        product = input("Enter product name to search: ")
        if product in inventory:
            print("Product:", product)
            print("Quantity:", inventory[product]["quantity"])
            print("Price:", inventory[product]["price"])
        else:
            print("Product not found.")

    elif choice == 4:
        product = input("Enter product name: ")
        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory[product]["quantity"] = quantity
            inventory[product]["price"] = price
            print("Product updated successfully.")
        else:
            print("Product not found.")

    elif choice == 5:
        product = input("Enter product name to delete: ")
        if product in inventory:
            del inventory[product]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    elif choice == 6:
        total = 0
        print("\n========== CUSTOMER BILL ==========")

        while True:
            product = input("Enter product name (or 'done' to finish): ")

            if product.lower() == "done":
                break

            if product in inventory:
                qty = int(input("Enter quantity: "))

                if qty <= inventory[product]["quantity"]:
                    amount = qty * inventory[product]["price"]
                    total += amount
                    inventory[product]["quantity"] -= qty

                    print(product, "x", qty, "=", amount)
                else:
                    print("Insufficient stock!")
            else:
                print("Product not found.")

        print("----------------------------------")
        print("Total Bill = ₹", total)
        print("Thank You! Visit Again.")

    elif choice == 7:
        print("Program Closed.")
        break

    else:
        print("Invalid choice! Please try again.")