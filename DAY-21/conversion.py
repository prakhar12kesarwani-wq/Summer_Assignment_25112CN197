string = input("Enter the string: ")

for i in string:
    if i >= 'a' and i <= 'z':
        print(chr(ord(i) - 32), end="")
    else:
        print(i, end="")