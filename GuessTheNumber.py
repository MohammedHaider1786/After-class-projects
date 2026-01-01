import random

number = random.randint(1, 10)

print("Guess the number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == number:
    print("Congratulations! You guessed the correct number.")
else:
    print("Wrong guess.")
    print("The correct number was:", number)
