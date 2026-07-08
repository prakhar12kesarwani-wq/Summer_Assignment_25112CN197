import random

number = random.randint(1, 50)

while True:
    guess = int(input("Guess the number (1-50): "))

    if guess == number:
        print("Congratulations 👌 !!!! You guessed the correct number.")
        break
    elif guess < number:
        print("Too low!!! Try again.")
        print()
    else:
        print("Too high!!! Try again.")
        print()