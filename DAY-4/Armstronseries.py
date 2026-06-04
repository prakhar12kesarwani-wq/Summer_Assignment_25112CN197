n=int(input("Enter the range upto which you want armstrong numbers "))
temp1=temp2=temp3=n
print("armstrong numbers:")

for i in range(1,temp3+1):
    j=l=i

    count=0
    k=0
    while i>0:
        i=i//10
        count+=1 

    remainder=0
    while j>0:
        remainder=j%10
        k=k+(pow(remainder,count))
        j=j//10

    if(k==l):
        print(k)
