string=input("Enter the word: ")
temp=""

for i in string:
    if i not in temp:
        count=0
        for j in string:
            if( j==i):
                count=count+1

        print(f"frequency of character {i} is :", count)
        temp=temp+i

