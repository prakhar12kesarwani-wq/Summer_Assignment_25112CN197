n=int(input("Enter the size of the array: "))

arr=[]                 #array 

for i in range(n):                             #taking input using loops 
    value =int(input("Enter the element:" ))
    arr.append(value)

sum=0
for i in range(n):                   #taking sum using loop
    sum=sum+arr[i]    

print ("Sum of the elements of the array is: ",sum)   #display total sum

average=sum/n          #taking average by dividing total sum with size of the array(no. of elements) 
print("Average of the elemnts of the array is: ", average)