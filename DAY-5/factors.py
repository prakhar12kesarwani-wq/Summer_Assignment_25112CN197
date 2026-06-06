n=int(input("Enterthe number:"))
factors=[]

print(f"factors of {n}:-")
for i in range (1,n+1):
    if n%i==0:            #taking factors
        factors.append(str(i))              # making a list of factors
print(",".join(factors))                #print them all 