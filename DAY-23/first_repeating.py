string = input("Enter a string: ")

for i in string:
    if string.count(i) >1 :
        print("First repeating character:", i)
        break
else:
    print("No repeating character found.")