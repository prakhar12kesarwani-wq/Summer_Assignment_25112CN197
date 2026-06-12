n=int(input("Enter the number: "))

def reverse(n):
    if n==0:
        return 
    
    else:
        print(n%10 ,end="")    
    
    reverse(n//10)

print(f"Reverse of {n} is: ")
reverse(n) 
    