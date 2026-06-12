n=int(input("Enter the term upto which you want fibonacci series: "))
firstterm=0
secondterm=1
if(n==1):
      print(firstterm)
elif(n==2):
      print(secondterm)
else:
    for i in range(3,n+1):
      
       nextterm=firstterm+secondterm
       firstterm=secondterm
       secondterm=nextterm

print(nextterm)      
