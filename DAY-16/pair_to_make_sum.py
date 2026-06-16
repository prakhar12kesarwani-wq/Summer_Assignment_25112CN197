n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

target=int(input("Enter the sum: "))

count=0
for i in range(n):

    for j in range(i+1,n):
        if (arr[i]+arr[j])==target:
            count=count+1
            print(f"pairs are : {arr[i]},{arr[j]}")

if(count==0):       
    print("Pair does not exist!!!!")            

