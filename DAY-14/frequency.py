n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

#to find frequency of a number in a array
s=int(input("Enter the element to search: "))     #taking input to search

count=0
for i in range(n):
    if arr[i]==s:             #linear search by comparing all element of the array with the input
        count=count+1 

print(f"Frequency of {s} in the array is : ", count)    #displaying the no. of times that element exist is the array



