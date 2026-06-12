n=int(input("Enter the number:"))

def perfect(n):
    temp=n

    sum=0
    for i in range (1,n):               
        if n%i==0:                    #taking factors
            sum=sum+i                   #adding them

    if sum==temp:
        return "it is a Perfect Number!!!"
    else :
        return "It is not a perfect number!!!"
    
print (perfect(n))    

        