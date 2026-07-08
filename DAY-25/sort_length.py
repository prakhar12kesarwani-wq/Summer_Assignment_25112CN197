words = input("Enter words separated by space: ").split()

for i in range(len(words)):
    for j in range(len(words)-1-i):
        if len(words[j]) > len(words[j+1]):
            temp = words[j]
            words[j] = words[j+1]
            words[j+1] = temp

print("Words sorted by length:")
for i in words:
    print(i)