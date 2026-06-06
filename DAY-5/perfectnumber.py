n=int(input("Enter the number:"))
temp=n

sum=0
for i in range (1,n):               
    if n%i==0:                    #taking factors
        sum=sum+i                   #adding them

if sum==temp:
    print("it is a Perfect Number!!!")
else :
    print("It is not a perfect number!!!")    