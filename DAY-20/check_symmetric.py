row=int(input("enter the no. of rows: "))
column=int(input("Enter the no. of column: "))

if row!=column:
    print("It is not a square matrix , so it can't be symmetric!!!")        

else:
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
    
    # to check symmetry -----

    symmetric=True
    for i in range(row):
        for j in range(column):
            if(matrix[i][j]!=transpose[i][j]):
                symmetric= False
                break

    if symmetric:
        print("Matrix is symmetric!!!")      

    else:
        print("It is not a symmetric matrix!!!")   





                    
