string = input("Enter a string: ")

max_char = ""
max_count = 0

for i in string:
    count = string.count(i)
    if count > max_count:
        max_count = count
        max_char = i

print("Maximum occurring character is:", max_char)
print("Frequency:", max_count)