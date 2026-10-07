# AF, Hangman
import random

words_file = []
with open("words.txt", "r") as file:
    content = file.read()
    words_file = content.split(",")


with open("stats.txt", "r") as file:
    content = file.read()
    wins = int(content[0])
    losses = int(content[2])
print(f"Your stats: Wins: {wins}, Losses: {losses}")


word = random.choice(words_file).upper()
wrong = 0
guessed = []


def hangman(wrong):
    if wrong == 0:
        print("Wrong guesses remaining: 6")
        print("""_____
|   |
|
|
|
|_______""")
    if wrong == 1:
        print("Wrong guesses remaining: 5")
        print("""_____
|   |
|   O
|
|
|_______""")
    if wrong == 2:
        print("Wrong guesses remaining: 4")
        print("""_____
|   |
|   O
|   |
|
|_______""")
    if wrong == 3:
        print("Wrong guesses remaining: 3")
        print("""_____
|   |
|   O
|  /|
|
|_______""")
    if wrong == 4:
        print("Wrong guesses remaining: 2")
        print("""_____
|   |
|   O
|  /|\\
|
|_______""")
    if wrong == 5:
        print("Wrong guesses remaining: 1")
        print("""_____
|   |
|   O
|  /|\\
|  /
|_______""")
    if wrong == 6:
        print("Wrong guesses remaining: 0")
        print("""_____
|   |
|   O
|  /|\\
|  / \\
|_______""")
    return ""


def display_word(word, guessed):
    display = ""
    for letter in (word):
        if letter in (guessed):
            display += letter
        else:
            display += "_"
    return display

def letters_guessed(guessed):
    characters = ""
    for item in (guessed):
        characters += item + ", "
    return characters

while True:

    displayed = display_word(word, guessed)
    if displayed != word:
        print(hangman(wrong))
        print(display_word(word, guessed))
        print(f"Guessed letters: {letters_guessed(guessed)}")
        guess_letter = input("Guess a letter: ").upper()
        if guess_letter not in guessed:
            if guess_letter not in word:
                wrong += 1
            guessed.append(guess_letter)
    if displayed == word:
        print(hangman(wrong))
        wins += 1
        with open("stats.txt", "w") as file:
            file.write(f"{wins},{losses}")
        print(f"Congratulations!! You guesed the word: {word}")
        print(f"Updated stats: Wins: {wins}, Losses: {losses}")
        while True:
            play = input("Play Again? (Y) (N) ")
            if play not in ("YyNn"):
                print("Must be (Y) or (N)")
            else:
                break
        if play in ("Yy"):
            word = random.choice(words_file).upper()
            wrong = 0
            guessed = []
        else:
            break
    if wrong >= 6:
        print(hangman(wrong))
        losses += 1
        with open("stats.txt", "w") as file:
            file.write(f"{wins},{losses}")
        print(f"You ran out of guesses!! The word was: {word}")
        print(f"Updated stats: Wins: {wins}, Losses: {losses}")
        while True:
            play = input("Play Again? (Y) (N) ")
            if play not in ("YyNn"):
                print("Must be (Y) or (N)")
            else:
                break
        if play in ("Yy"):
            word = random.choice(words_file).upper()
            wrong = 0
            guessed = []
        else:
            break