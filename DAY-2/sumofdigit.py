n=int(input("Enter the number:"))

remainder=0
sum=0
while n>0:
    remainder=n%10
    sum=sum+remainder
    n=n//10

print("Sum of digits is:",sum)    
