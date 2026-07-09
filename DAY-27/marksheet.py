while True:
    print("\n----- Marksheet Generation System -----")
    print("1. Generate Marksheet")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")

        m1 = float(input("Enter Marks of Subject 1: "))
        m2 = float(input("Enter Marks of Subject 2: "))
        m3 = float(input("Enter Marks of Subject 3: "))
        m4 = float(input("Enter Marks of Subject 4: "))
        m5 = float(input("Enter Marks of Subject 5: "))

        total = m1 + m2 + m3 + m4 + m5
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        print("\n----- MARKSHEET -----")
        print("Student Name :", name)
        print("Roll Number  :", roll)
        print("Total Marks  :", total, "/500")
        print("Percentage   :", percentage, "%")
        print("Grade        :", grade)

    elif choice == 2:
        print("Exiting Marksheet Generation System...")
        break

    else:
        print("Invalid choice! Please try again.")