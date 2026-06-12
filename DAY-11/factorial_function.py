n=int(input("enter the no.:"))

def factorial(n):    #funct. definition
    total=1
    for i in range (1,n+1):
        total=total*i

    return total

print(f"Factorial of {n} is: ",factorial(n))   #funct. calling