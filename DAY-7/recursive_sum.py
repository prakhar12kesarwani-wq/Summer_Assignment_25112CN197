n=int(input("Enter the Number: "))

def sum(n):            #recursive function
    if n==0:
        return 0
    
    else:
        return (n % 10) + sum( n // 10)           #adding remainder and then using recursive function

print("sum of the digits is:",sum(n))