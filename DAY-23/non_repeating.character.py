string = input("Enter a string: ")

for i in string:
    if string.count(i) == 1:
        print("First non-repeating character:", i)
        break
else:
    print("No non-repeating character found.")