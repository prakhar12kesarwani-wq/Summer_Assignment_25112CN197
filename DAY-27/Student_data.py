students = {}

while True:
    print("\n----- Student Record Management System -----")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            students[roll] = {"Name": name, "Marks": marks}
            print("Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No records found.")
        else:
            print("\nStudent Records:")
            for roll, details in students.items():
                print("Roll No:", roll)
                print("Name:", details["Name"])
                print("Marks:", details["Marks"])
                print("----------------------")

    elif choice == 3:
        roll = input("Enter Roll Number to search: ")

        if roll in students:
            print("Name:", students[roll]["Name"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student not found.")

    elif choice == 4:
        roll = input("Enter Roll Number to update: ")

        if roll in students:
            new_marks = float(input("Enter New Marks: "))
            students[roll]["Marks"] = new_marks
            print("Marks updated successfully!")
        else:
            print("Student not found.")

    elif choice == 5:
        roll = input("Enter Roll Number to delete: ")

        if roll in students:
            del students[roll]
            print("Student record deleted successfully!")
        else:
            print("Student not found.")

    elif choice == 6:
        print("Exiting Student Record Management System...")
        break

    else:
        print("Invalid choice! Please try again.")