n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value = int(input("Enter the element:" ))
    arr.append(value)

sum=0
for i in range(n-1):
    sum=sum+arr[i]     #sum of elements of array
    

expected_sum=n*(n+1)//2      #calculating sum of n integers

missing_number=expected_sum-sum
print("Missing Number is: ",missing_number)
