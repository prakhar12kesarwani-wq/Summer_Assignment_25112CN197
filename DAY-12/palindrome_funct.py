n=int(input("Enter the Number:"))

def palindrome(n):   #function definition

    temp=n
    remainder=0
    reverse=0
    while n>0:
        remainder=n%10
        reverse=reverse*10+remainder
        n=n//10

    if temp==reverse:
        return f"The number {temp} is palindrome" 

    else:
        return f"The number {temp} is not palindrome"

print(palindrome(n))       #function calling
