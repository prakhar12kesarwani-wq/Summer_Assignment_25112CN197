#addition of matrices
row=int(input("Enter the no. of row: "))
column=int(input("Enter the no. of column: "))

matrix1=[]
matrix2=[]
result=[]                #array 

print("Enter first matrix:")
for i in range(row):
    a=[]          #taking temporary row
    for j in range(column):                       #taking input using nested loops 
        value = int(input("Enter the element:" ))
        a.append(value)             #taking input row-wise
    matrix1.append(a)             #storing input in matrix1

print("Enter second matrix:")
for i in range(row):
    a=[]          #taking temporary row
    for j in range(column):                       #taking input using nested loops 
        value = int(input("Enter the element:" ))
        a.append(value)             #taking input row-wise
    matrix2.append(a)             #storing input in matrix2

for i in range(row):
    a=[]
    for j in range(column):
        a.append(matrix1[i][j]+matrix2[i][j])    #adding same position elements
    result.append(a)
    
print("Addition of the matrices: ")
for i in range(row):
        print(result[i])
       

