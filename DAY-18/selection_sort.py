n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

   ####### Selection sort #######

for i in range(n-1):
    min=i

    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j

    temp=arr[min]
    arr[min]=arr[i]
    arr[i]=temp

print("sorted array :",arr)