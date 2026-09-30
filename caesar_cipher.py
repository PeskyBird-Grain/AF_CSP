# AF, Caesar Cipher

# ord: letter to number, char: number to letter
#A = 65
#Z = 90
#a = 97
#z = 122
d_e = input("Would you like to (E)ncript or (D)ecript a message? ")
mess = input("Enter your message: ")
shift = input("Enter a shift amount: ")

#def caeser_shift(message, shift):
    
for letter in mess:
    if letter.isalpha():
        ord(letter) + shift
        if ord(letter) > 122:
            ord(letter) = 97 + ord(letter) - 122
        elif ord(letter) < 97:
            ord(letter) = 122 + ord(letter) - 97
        if ord(letter) > 90:
            ord(letter) = 97 + ord(letter) - 122
        elif ord(letter) < 97:
            ord(letter) = 122 + ord(letter) - 97