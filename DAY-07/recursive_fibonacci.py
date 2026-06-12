n=int(input("Enter the range of the fibonacci series:"))

def fibonacci(n):
    if n==0:                                     #fibonacci(0)=0
        return 0
    
    elif n==1:                           #fibonacci(1)=1
        return 1
    
    else:
        return fibonacci(n-1)+fibonacci(n-2)                 #last term + secondlast term

print("Fibonacci series: ")    
for i in range(n):    
    print(fibonacci(i),end=" ")    
