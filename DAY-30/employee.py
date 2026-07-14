# Mini Employee Management System

emp_id = []
emp_name = []
department = []
salary = []

while True:
    print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Employee Summary")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        eid = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        dept = input("Enter Department: ")
        sal = float(input("Enter Salary: "))

        emp_id.append(eid)
        emp_name.append(name)
        department.append(dept)
        salary.append(sal)

        print("Employee Added Successfully!")

    elif choice == 2:
        if len(emp_id) == 0:
            print("No Employee Records Found!")
        else:
            print("\n================ EMPLOYEE RECORDS ================")
            print("{:<10} {:<20} {:<20} {:<12}".format(
                "ID", "Name", "Department", "Salary"))
            print("-" * 65)

            for i in range(len(emp_id)):
                print("{:<10} {:<20} {:<20} {:<12}".format(
                    emp_id[i],
                    emp_name[i],
                    department[i],
                    salary[i]
                ))

    elif choice == 3:
        search = int(input("Enter Employee ID to Search: "))
        found = False

        for i in range(len(emp_id)):
            if emp_id[i] == search:
                print("\nEmployee Found!")
                print("ID:", emp_id[i])
                print("Name:", emp_name[i])
                print("Department:", department[i])
                print("Salary:", salary[i])
                found = True
                break

        if not found:
            print("Employee Not Found!")

    elif choice == 4:
        search = int(input("Enter Employee ID: "))
        found = False

        for i in range(len(emp_id)):
            if emp_id[i] == search:
                new_salary = float(input("Enter New Salary: "))
                salary[i] = new_salary
                print("Salary Updated Successfully!")
                found = True
                break

        if not found:
            print("Employee Not Found!")

    elif choice == 5:
        search = int(input("Enter Employee ID to Delete: "))
        found = False

        for i in range(len(emp_id)):
            if emp_id[i] == search:
                del emp_id[i]
                del emp_name[i]
                del department[i]
                del salary[i]
                print("Employee Deleted Successfully!")
                found = True
                break

        if not found:
            print("Employee Not Found!")

    elif choice == 6:
        print("\n========== EMPLOYEE SUMMARY ==========")
        print("Total Employees:", len(emp_id))

        if len(emp_id) > 0:
            print("Highest Salary:", max(salary))
            print("Lowest Salary:", min(salary))
            print("Average Salary:", sum(salary) / len(salary))

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")