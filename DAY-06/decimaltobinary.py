n=int(input("Enter the Decimal Number:"))
binary=[]

while n>0:
    remainder=n%2                                     #taking remainder of the decimal number
    binary.append(str(remainder))                      #storing all remianders in a list
    n=n//2                       

binary.reverse()                       #reversing the string
print("binary of the number is: ", "".join(binary) )    

