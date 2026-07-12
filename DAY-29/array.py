# Menu-Driven Array Operations System

arr = []

while True:
    print("\n===== ARRAY OPERATIONS MENU =====")
    print("1. Add Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Delete Element")
    print("5. Update Element")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        element = int(input("Enter element to add: "))
        arr.append(element)
        print("Element added successfully.")

    elif choice == 2:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Array Elements:", arr)

    elif choice == 3:
        element = int(input("Enter element to search: "))
        if element in arr:
            print("Element found at index", arr.index(element))
        else:
            print("Element not found.")

    elif choice == 4:
        element = int(input("Enter element to delete: "))
        if element in arr:
            arr.remove(element)
            print("Element deleted successfully.")
        else:
            print("Element not found.")

    elif choice == 5:
        old = int(input("Enter element to update: "))
        if old in arr:
            new = int(input("Enter new value: "))
            index = arr.index(old)
            arr[index] = new
            print("Element updated successfully.")
        else:
            print("Element not found.")

    elif choice == 6:
        print("Program Closed.")
        break

    else:
        print("Invalid choice! Please try again.")