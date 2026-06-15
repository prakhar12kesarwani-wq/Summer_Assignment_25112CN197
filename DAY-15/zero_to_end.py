n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

for i in range(n):
    if(arr[i]==0):    #check if element is zero or not
        for j in range(i,n-1):            #if found 0 then shifting element to left
            arr[j]=arr[j+1]        

        arr[n-1]=0    #put zero in last

print(arr)            