string=input("Enter the string: ")

count_vowel=0
count_consonant=0


for i in string:
    if i=="a" or i== "e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        count_vowel = count_vowel + 1

    elif (i>="a" and i<="z") or (i>="A" and i<="Z"):
        count_consonant = count_consonant + 1 

print("No. of vowels: ",count_vowel)
print("No. of consonants: ",count_consonant)

