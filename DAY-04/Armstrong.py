n=int(input("Enter the number you want to check wheater it is armstrong or not: "))
temp1=temp2=n

count=0
k=0
while n>0:
    n=n//10
    count+=1 

remainder=0
while temp1>0:
    remainder=temp1%10
    k=k+(pow(remainder,count))
    temp1=temp1//10

if(k==temp2):
    print("Number is Armstrong!!!")

else:
    print("Number is not Armstrong!!!")        
