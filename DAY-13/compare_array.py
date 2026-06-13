n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

largest=arr[0]   #let the first element as largest for refrence 
smallest=arr[0]    #let the first element as smallest for refrence

for i in range (n):   #using loop for comparison

    if arr[i]>largest:            #comparing large number then 'largest'         
        largest=arr[i]         #if found ('largest' = that large number)

    if arr[i]<smallest:   #comparison of elemnts with each other
        smallest=arr[i]

print("Largest Element of the array is: ",largest) 
print("smallest Element of the array is: ",smallest)


    
