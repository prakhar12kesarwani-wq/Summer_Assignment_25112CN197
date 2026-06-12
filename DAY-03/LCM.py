n=int(input("Enter the 1st number"))
m=int(input("Enter the 2nd number"))

greater=max(n,m)
 
while True:
    if greater%n==0 and greater%m==0:
        print("LCM of these number is:",greater)
        break

    greater=greater+1    

