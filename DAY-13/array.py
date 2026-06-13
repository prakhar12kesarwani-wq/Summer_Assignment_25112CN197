n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

print("array elements: ")   
   
for i in arr:                          #output of the array
     print(i)
  