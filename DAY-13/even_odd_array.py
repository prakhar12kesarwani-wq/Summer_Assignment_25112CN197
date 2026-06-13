n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

print("Even Numbers: ")
count_even=0
for i in range(n):                            #for even number counting and printing
    if arr[i]%2 ==0:
        print(arr[i])
        count_even=count_even+1   
print(f"There are {count_even} even numbers in the array!!!")      

print()

print("Odd Numbers: ")
count_odd=0
for i in range(n):                       #for odd number counting and printing
     if arr[i]%2!=0:
        print(arr[i])
        count_odd=count_odd+1
print(f"there are {count_odd} odd numbers in the array!!!")






            