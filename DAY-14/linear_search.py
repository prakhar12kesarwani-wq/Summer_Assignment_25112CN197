n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

#to implement linear search
s=int(input("Enter the element to search: "))     #taking input to search

count=0
for i in range(n):
    if arr[i]==s:             #linear search by comparing all element of the array with the input
        count=count+1
        print(f"Element found!!! at {i+1} position")   #it is inside loop in case of multiple existance of that element

if count==0:                #in case there is not that element in the array
    print("Element not found!!!")


