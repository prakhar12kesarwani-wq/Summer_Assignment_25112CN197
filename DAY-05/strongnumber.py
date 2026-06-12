n=int(input("Enter the number:"))
temp=n

remainder=0
sum=0
while n>0:
    remainder=n%10            #seperating digits from the original number
    factorial=1
    for i in range(1,remainder+1):   
        factorial=factorial*i         #taking factorial of each digit
    sum=sum+factorial                 #adding all factorials
    n=n//10

if sum==temp:
    print("It is a STRONG NUMBER!!!!") 

else:
    print("It is not a STRONG NUMBER!!!")
      