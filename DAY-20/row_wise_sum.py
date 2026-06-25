row=int(input("enter the no. of rows: "))
column=int(input("Enter the no. of column: "))

matrix=[]
result=[]

for i in range(row):
    a=[]          #taking temporary row
    for j in range(column):                       #taking input using nested loops 
        value = int(input("Enter the element:" ))
        a.append(value)             #taking input row-wise
    matrix.append(a)             #storing input in matrix1

#row wise sum ------
for i in range(row):
    a=[]
    sum=0
    for j in range(column):
        sum=sum+matrix[i][j]
    result.append(sum)

for i in range(row):
    print(f"row {i+1}: sum : ",result[i])


        