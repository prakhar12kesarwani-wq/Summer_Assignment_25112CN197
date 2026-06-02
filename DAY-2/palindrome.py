n=int(input("Enter the Number:"))

temp=n
remainder=0
reverse=0
while n>0:
    remainder=n%10
    reverse=reverse*10+remainder
    n=n//10

if temp==reverse:
    print(f"The number {temp} is palindrome")    

else:
    print(f"The number {temp} is not palindrome")    
