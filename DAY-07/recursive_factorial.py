n=int(input("Enter the number:"))

def factorial(n):              #recursive function to calculate factorial of the number

    if n==0 or n==1:         
        return 1

    else:
        return n*factorial(n-1)                  #case- n!=n*(n-1)!

print(f"factorial of {n} is: ",factorial(n))              #print by function calling