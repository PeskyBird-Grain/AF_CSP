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
stats = []
with open("stats.txt", "r") as file:
    content = file.read()
    stats = content.split(",")
    wins = stats
    losses = stats
print(wins)
print(losses)
# save random.choice(name of list)
word = random.choice(words_file).capitalize()
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

    for letter in (word):
        display = ""
        if guessed in (letter):
            display += guessed
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

    print(wrong)    
    displayed = display_word(word, guessed)
    print(display_word(word, guessed))
    guess_letter = input("Guess a letter: ")
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
        if play == "Y":
            word = random.choice(words_file).capitalize()
            wrong = 0
            guessed = []
    if wrong >= 6:
        print(f"You ran out of guesses!! The word was: {word}")
        while True:
            play = input("Play Again? (Y) (N) ")
            if play not in ("YyNn"):
                print("Must be (Y) or (N)")
            else:
                break
        if play == "Y":
            word = random.choice(words_file).capitalize()
            wrong = 0
            guessed = []

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