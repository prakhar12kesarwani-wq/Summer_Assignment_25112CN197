n=int(input("Enter 1st number"))
m=int(input("Enter 2nd number"))
gcd=1

for i in range (1,min(n,m)+1):
    if n%i==0 and m%i==0:
        gcd=i

print("GCD of these number is",gcd)        
