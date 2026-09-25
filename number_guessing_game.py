# AF, Number Guessing Game
import random
print("I'm thinking of a number between 1 and 50. You have 6 tries to guess it!!")

rand = random.randint(1,51)
attempts = 1

while True:
    guess = input(f"Guess #{attempts}: ")
    if guess != rand:
        if guess < rand:
            print("Too low!!")
        if guess > rand:
            print("Too high!!")