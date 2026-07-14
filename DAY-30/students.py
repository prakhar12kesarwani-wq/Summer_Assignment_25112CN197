roll = []
name = []
marks = []

n = int(input("Enter number of students: "))

# Add student records
for i in range(n):
    print(f"\nStudent {i+1}")

    r = int(input("Enter Roll Number: "))
    roll.append(r)

    nm = input("Enter Name: ")
    name.append(nm)

    m = float(input("Enter Marks: "))
    marks.append(m)

# Display all records
print("\n----- Student Records -----")
print("Roll No\tName\tMarks")

for i in range(n):
    print(roll[i], "\t", name[i], "\t", marks[i])

# Search student
search = int(input("\nEnter Roll Number to Search: "))
found = False

for i in range(n):
    if roll[i] == search:
        print("\nStudent Found!")
        print("Roll Number:", roll[i])
        print("Name:", name[i])
        print("Marks:", marks[i])
        found = True
        break

if not found:
    print("Student Record Not Found.")