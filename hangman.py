# AF, Hangman
import random

#create one file with 10 possible words

#create another file that holds the win-loss count

#read the information from the words file and make it a list. use split(",") on the content
words_file = []
with open("words.txt", "r") as file:
    content = file.read()
    words_file = content.split(",")
#pull win-lose totals and save 2 seperate variables

#build game

# save random.choice(name of list)
word = random.choice(words_file)
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
        if guessed in (word):
            display += guessed
        else:
            display += "_"
#loop over correct word
    #variable for display word (start empty string)
    #check if letter been guessed
        #add letter to display word
    #if not 
        #add an underscore to the word
#return the finished display word

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

