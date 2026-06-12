n = int(input("Enter the number: "))
factor = []

for i in range(2, n + 1):                
    if n % i == 0:           #taking factors
        fact = i            #assigning into a temporary variable

        count = 0
        for j in range(1, fact + 1):
            if fact % j == 0:           #checking the factorial is prime or not
                count=count+1

        if count == 2:
            factor.append(fact)             #appending all prime factors in the list

print("Largest prime factor:", max(factor))