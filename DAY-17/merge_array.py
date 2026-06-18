n1=int(input("Enter the size of the array: "))

arr1=[]                 #array1 

for i in range(n1):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr1.append(value)


n2=int(input("Enter the size of the array: "))

arr2=[]                 #array2

for i in range(n2):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr2.append(value)

#to merge
arr3=[0]*(n1+n2)   #taking third array with the size cobine of given array's

for i in range(n1):      #copy arr1
    arr3[i]=arr1[i]

for i in range(n2):    #copy arr2
    arr3[n1+i]=arr2[i]

print(arr3)

