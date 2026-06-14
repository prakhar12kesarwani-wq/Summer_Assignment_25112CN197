n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

#to find duplicate elements

for i in range(n):
    count=0
    temp=arr[i]
    for j in range(n):
        if(arr[j]==temp):
            count=count+1

    if count>1:
        if arr.index(temp)==i:
            print(f"The duplicate of element {arr[i]} is: ", count)        