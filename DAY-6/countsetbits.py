n=int(input("Enter the integer to count set bits:"))

remainder=0
count=0
while n>0:
    remainder=n%2             #converting integer to binary
    if remainder==1:              
        count=count+1
    n=n//2    
    
print("set bits in the number is:",count)        