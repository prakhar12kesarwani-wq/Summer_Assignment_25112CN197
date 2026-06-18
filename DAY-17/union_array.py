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

###########     union of array     ############

#merging
arr3=[0]*(n1+n2)

for i in range(n1):      #copy arr1
    arr3[i]=arr1[i]

for i in range(n2):    #copy arr2
    arr3[n1+i]=arr2[i]

#removing duplicates from the merged arrray
union_arr=[]

for i in range(len(arr3)):
    count=0
    for j in range(len(union_arr)):
        if (arr3[i]==union_arr[j]):
            count=count+1
            break

    if count==0:
        union_arr.append(arr3[i])    


print(union_arr)            