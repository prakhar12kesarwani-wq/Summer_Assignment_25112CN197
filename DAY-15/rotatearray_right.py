n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

#rotate array right by 1 position
last_element= arr[n-1]

for i in range(n-1,0,-1):
    arr[i]=arr[i-1]           #shifting element at their next location

arr[0]=last_element       #shifting last element to first location

print(arr)