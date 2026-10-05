# AF, Hangman
import random

#create one file with 10 possible words

#create another file that holds the win-loss count

#read the information from the words file and make it a list. use split(",") on the content
words_file = []
with open("words.txt", "r") as file:
    content = file.read()
    words_file = content.split(",")
print(words_file)
#pull win-lose totals and save 2 seperate variables

with open("stats.txt", "r") as file:
    content = file.read()
    wins = int(content[0])
    losses = int(content[2])
print(f"Your stats: Wins: {wins}, Losses: {losses}")
# save random.choice(name of list)
word = random.choice(words_file).upper()
print(word)
# #wrong guesses
wrong = 0
# what's been guessed
guessed = []

# function displays hangman (needs # wrong)
#"""_____
#   |   |
#   |   O
#   |  /|\\
#   |  / \\
#   |_______
#"""

#function to show letters and spaces (the correct word, letters guesed)
def display_word(word, guessed):
    display = ""
    for letter in (word):
        if letter in (guessed):
            display += letter
        else:
            display += "_"
    return display
#loop over correct word
    #variable for display word (start empty string)
    #check if letter been guessed
        #add letter to display word
    #if not 
        #add an underscore to the word
#return the finished display word

while True:

    displayed = display_word(word, guessed)
    if displayed != word:
        print(wrong)    
        print(display_word(word, guessed))
        guess_letter = input("Guess a letter: ").upper()
        guessed.append(guess_letter)
    if guess_letter not in (word):
        wrong += 1
    if displayed == word:

        print(f"Congratulations!! You guesed the word: {word}")
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
        losses += 1
        print(f"You ran out of guesses!! The word was: {word}")
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
with open("stats.txt", "w") as file:
    file.write(f"{wins},{losses}")
#main game loop (while True)
    #call function to show hangman
    #print function call to show display word
    #create variable and ask to guess letter
    #add letter to list of guessed letters
    #check if letter not in word
        #increase wrong guesses
    #check if display word is same as word
        #you win
        #increase win total
        #play again?
            #reset random word, wrong guess count, 
#check if loss(6 wrong)
    #tell loss
    #tell word
    #increased loss