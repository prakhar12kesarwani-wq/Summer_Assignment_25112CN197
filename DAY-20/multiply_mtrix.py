row1=int(input("Enter the no. of row of 1st matrix: "))
column1=int(input("Enter the no. of column of 1st matrix: "))

matrix1=[]

print("Enter first matrix:")
for i in range(row1):
    a=[]          #taking temporary row
    for j in range(column1):                       #taking input using nested loops 
        value1 = int(input("Enter the element:" ))
        a.append(value1)             #taking input row-wise
    matrix1.append(a)             #storing input in matrix1


row2=int(input("Enter the no. of row of 2nd matrix: "))
column2=int(input("Enter the no. of column of 2nd matrix: "))

matrix2=[]              #array 

print("Enter second matrix:")
for i in range(row2):
    a=[]          #taking temporary row
    for j in range(column2):                       #taking input using nested loops 
        value2 = int(input("Enter the element:" ))
        a.append(value2)             #taking input row-wise
    matrix2.append(a)             #storing input in matrix1

####  Multiply of matrices  ####
result=[]

if column1==row2:
    for i in range(row1):
        a=[]
        for j in range(column2):
            multiply=0

            for k in range(column1):                  
                multiply=multiply+matrix1[i][k]*matrix2[k][j]

            a.append(multiply)

    result.append(a)
    print("Multiplication of the matrices are: ")    
    for i in range(row1):
        print(result[i])

else:
    print("Matrices does'nt match the condition of multiplication!!!! ")        


               
