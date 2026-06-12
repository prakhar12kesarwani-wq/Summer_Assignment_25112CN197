n=int(input("Enter the term upto which you want fibonacci series: "))

def fibonacci(n):
    firstterm=0
    secondterm=1
    for i in range (1,n+1):
        if(i==1):
            print(firstterm,end=" ")

        elif(i==2):
            print(secondterm,end=" ")

        elif(i>2):
            nextterm=firstterm+secondterm
            print(nextterm,end=" ")
            firstterm=secondterm
            secondterm=nextterm

fibonacci(n)            


