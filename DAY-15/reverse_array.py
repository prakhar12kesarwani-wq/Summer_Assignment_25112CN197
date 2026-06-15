n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

for i in range(n//2):      #reverse the array by swapping ,in order first element swaps with last and same for the other elements 
    temp=arr[i]
    arr[i]=arr[n-1-i]
    arr[n-1-i]=temp

for i in range(n):   #displaying reversed array
    print(arr[i])
