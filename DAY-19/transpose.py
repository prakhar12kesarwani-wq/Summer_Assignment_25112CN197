row=int(input("enter the no. of rows: "))
column=int(input("Enter the no. of column: "))

matrix=[]
transpose=[]

for i in range(row):
    a=[]          #taking temporary row
    for j in range(column):                       #taking input using nested loops 
        value = int(input("Enter the element:" ))
        a.append(value)             #taking input row-wise
    matrix.append(a)             #storing input in matrix1

for i in range(column):
    a=[]
    for j in range(row):
        a.append(matrix[j][i])      #transpose
    transpose.append(a)

print("transpose of the matrix : ")
for i in range(column):
    print(transpose[i])    