n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

#rotate array left by 1 position
first_element= arr[0]
for i in range(n-1):
    arr[i]=arr[i+1]           #storing element at their previous location

arr[n-1]=first_element       #storing first element to last

print(arr)