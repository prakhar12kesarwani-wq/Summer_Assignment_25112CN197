n=int(input("Enter the number:"))

def prime(n):  #function definition
    count=0
    for i in range (1,n+1):
        if n%i==0:              #if remainder=0 then count is plus one
            count=count+1

    if count==2:
        return "no. is prime"
    else:
        return "No. is not prime"

print(prime(n))       #function calling