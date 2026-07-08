names = input("Enter names separated by space: ").split()

for i in range(len(names)):
    for j in range(len(names)-1-i):
        if names[j] > names[j+1]:
            temp = names[j]
            names[j] = names[j+1]
            names[j+1] = temp

print("Names in alphabetical order:")
for i in names:
    print(i)