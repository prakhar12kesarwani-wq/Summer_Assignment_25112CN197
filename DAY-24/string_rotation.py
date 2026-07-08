str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("String is a rotation")
else:
    print("String is not a rotation")