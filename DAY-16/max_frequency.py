n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

#to find maximum frequency of a number in a array
max_count=0
max_element=arr[0]

for i in range(n):
    count=0

    for j in range(n):

        if arr[i]==arr[j]:             #linear search by comparing all element of the array with the input
            count=count+1

    if count>max_count:
        max_count=count
        max_element=arr[i]         
        

print(f"maximum Frequency of {max_element} in the array is : ", max_count)    #displaying the no. of times that element exist is the array



