n=int(input("Enter the term upto which you want fibonacci series"))
firstterm=0
secondterm=1
for i in range (1,n+1):
    if(i==1):
      print(firstterm)
    elif(i==2):
      print(secondterm)
    elif(i>2):
      nextterm=firstterm+secondterm
      print(nextterm)
      firstterm=secondterm
      secondterm=nextterm
