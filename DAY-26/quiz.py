name=input("Enter your name : ")
score = 0

ans = input("1. What is the capital of India? ")
if ans.lower() == "delhi":
    score += 1

ans = input("2. How many days are there in a week? ")
if ans == "7":
    score += 1

ans = input("3. What is 5 + 5? ")
if ans == "10":
    score += 1

ans = input("4. Who is known as the Father of the Nation? ")
if ans.lower() == "mahatma gandhi":
    score += 1

ans = input("5. What is the largest planet in our Solar System? ")
if ans.lower() == "jupiter":
    score += 1

print("Your Score =", score)