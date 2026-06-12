num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))

def max(num1, num2):       #function definition
    if num1>num2:
        return num1
    
    elif num1<num2:
        return num2
    
    else:
        print("same number")
    
print("Maximum is: ",max(num1,num2))    #function calling