string=input("Enter the string: ")
reverse=""

for i in string:
    reverse=i+reverse
if(reverse==string):
    print("The string is palindrome !!!") 

else:
    print("The string is not palindrome !!")       
