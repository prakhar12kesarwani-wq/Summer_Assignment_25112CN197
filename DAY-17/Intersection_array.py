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

###############     intersection of array     ###################

new_arr=[]
for i in range(n1):
    for j in range(n2):

        if(arr1[i]==arr2[j]):

             # duplicate check
            count=0

            for k in range(len(new_arr)):
                if arr1[i]==new_arr[k]:
                    count=1
                    break

            if count==0:
                new_arr.append(arr1[i])

print(new_arr)                

