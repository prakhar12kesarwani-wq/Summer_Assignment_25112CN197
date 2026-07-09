salary_records = {}

while True:
    print("\n----- Salary Management System -----")
    print("1. Add Salary Record")
    print("2. View All Salary Records")
    print("3. Search Salary Record")
    print("4. Update Salary")
    print("5. Delete Salary Record")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")

        if emp_id in salary_records:
            print("Salary record already exists!")
        else:
            name = input("Enter Employee Name: ")
            basic_salary = float(input("Enter Basic Salary: "))
            bonus = float(input("Enter Bonus: "))
            total_salary = basic_salary + bonus

            salary_records[emp_id] = {
                "Name": name,
                "Basic Salary": basic_salary,
                "Bonus": bonus,
                "Total Salary": total_salary
            }

            print("Salary record added successfully!")

    elif choice == 2:
        if len(salary_records) == 0:
            print("No salary records found.")
        else:
            print("\nSalary Records:")
            for emp_id, details in salary_records.items():
                print("Employee ID:", emp_id)
                print("Name:", details["Name"])
                print("Basic Salary:", details["Basic Salary"])
                print("Bonus:", details["Bonus"])
                print("Total Salary:", details["Total Salary"])
                print("----------------------------")

    elif choice == 3:
        emp_id = input("Enter Employee ID to search: ")

        if emp_id in salary_records:
            print("Name:", salary_records[emp_id]["Name"])
            print("Basic Salary:", salary_records[emp_id]["Basic Salary"])
            print("Bonus:", salary_records[emp_id]["Bonus"])
            print("Total Salary:", salary_records[emp_id]["Total Salary"])
        else:
            print("Employee not found.")

    elif choice == 4:
        emp_id = input("Enter Employee ID to update salary: ")

        if emp_id in salary_records:
            basic_salary = float(input("Enter New Basic Salary: "))
            bonus = float(input("Enter New Bonus: "))
            total_salary = basic_salary + bonus

            salary_records[emp_id]["Basic Salary"] = basic_salary
            salary_records[emp_id]["Bonus"] = bonus
            salary_records[emp_id]["Total Salary"] = total_salary

            print("Salary updated successfully!")
        else:
            print("Employee not found.")

    elif choice == 5:
        emp_id = input("Enter Employee ID to delete: ")

        if emp_id in salary_records:
            del salary_records[emp_id]
            print("Salary record deleted successfully!")
        else:
            print("Employee not found.")

    elif choice == 6:
        print("Exiting Salary Management System...")
        break

    else:
        print("Invalid choice! Please try again.")