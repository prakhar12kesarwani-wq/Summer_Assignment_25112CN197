x=int(input("Enter the number: "))
n=int(input("Enter the power: "))

power=1
if n>=0:                     #for positive power
    for i in range (1,n+1):
        power=power*x           #multiplying according to the power

          
    
else:                        #for negative power
    for i in range(-n):
        power=power*x
    power=1/power

print("answer is: ",power)        