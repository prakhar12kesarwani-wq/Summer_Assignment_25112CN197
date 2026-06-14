n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

largest=arr[0]
second=arr[0]

for i in range(n):
    if arr[i]>largest:      
        second=largest       #sorting
        largest=arr[i]

    elif arr[i]>second and arr[i]!=largest:
        second=arr[i]   

print("Second largest element is: ", second)             
