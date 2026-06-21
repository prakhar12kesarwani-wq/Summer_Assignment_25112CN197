row=int(input("Enter the no. of row: "))
column=int(input("Enter the no. of column: "))

matrix=[]         

print("Enter first matrix:")
for i in range(row):
    a=[]          #taking temporary row
    for j in range(column):                       #taking input using nested loops 
        value = int(input("Enter the element:" ))
        a.append(value)             #taking input row-wise
    matrix.append(a)             #storing input in matrix1

sum=0

for i in range(row):
    for j in range(column):
        if i==j:
            sum=sum+matrix[i][j]     #addidng primary diagonal elements


print("Sum of the diagonal elements of the matrix is : ",sum)            
    
    