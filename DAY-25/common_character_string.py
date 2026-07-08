str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Common characters are:")

for ch in str1:
    if ch in str2:
        print(ch, end=" ")