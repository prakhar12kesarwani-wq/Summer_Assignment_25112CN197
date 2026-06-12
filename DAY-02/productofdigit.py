n=int(input("Enter the number:"))

remainder=0
product=1
while n>0:
    remainder=n%10
    product=product*remainder
    n=n//10

print("Multiplication of the digits is:",product)
