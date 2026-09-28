# AF, Number Guessing Game
import random
print("I'm thinking of a number between 1 and 50. You have 6 tries to guess it!!")
rand = random.randint(1,50)
attempts = 1
while True:
    guess = input(f"Guess #{attempts}: ")
    attempts += 1

    if int(guess) != rand:
        if attempts > 6:
            attempts += 1
            print(f"You ran out of guesses!! The number was {rand}")
            break
        if int(guess) < rand:
            print("Too low!!")
            continue
        if int(guess) > rand:
            print("Too high!!")
            continue
    else:
        break
if attempts <= 7: 
    print(f"Correct!! You guessed '{rand}' in {attempts - 1} tries.")