n=int(input("Enter the binary Number: "))
import math
temp=n

count=0
while n>0:                # To count the digit 
    n=n//10
    count+=1

remainder=0
decimal=0
for i in range (0,count):
    remainder=temp%10                    #seperating remainder
    decimal=decimal+remainder*(2**i)       #adding all digits in the form (remainder*2^i)
    temp=temp//10

print( "Decimal of this number is :", decimal)

