n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

new_arr=[]

for i in range(n):
    count=0
    for j in range(len(new_arr)):
        if (arr[i]==new_arr[j]):
            count=count+1
            break

    if count==0:
        new_arr.append(arr[i])    


print(new_arr)            
