# AF, Caesar Cipher

# ord: letter to number, char: number to letter
#A = 65
#Z = 90
#a = 97
#z = 122
while True:
    decrypt_encrypt = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").upper()
    if decrypt_encrypt not in ["D", "E"]:
        print("Only type D or E!!")
    else:
        break
mess = input("Enter your message: ")
shift = input("Enter a shift amount: ")

def caeser_shift(message, decrypt_encrypt, shift):
    shifted_message = ""
    print(f"Decript encrypt: {decrypt_encrypt}")
    if decrypt_encrypt == "decrypted":
        shift = -shift
    if decrypt_encrypt == "encrypted":
        shift = shift
    for letter in message:
        if letter.isalpha():
            letter_ascii = ord(letter)
            letter_shifted = letter_ascii + shift
            if letter.islower():
                if letter_shifted > 122:
                    letter_shifted -= 26
                elif letter_shifted < 97:
                    letter_shifted += 26
            if letter.isupper():
                if letter_shifted > 90:
                    letter_shifted -= 26
                elif letter_shifted < 65:
                    letter_shifted += 26
            shifted_message += chr(letter_shifted)
        else:
            shifted_message += letter
    return shifted_message
if decrypt_encrypt in "Dd":
    decrypt_encrypt = "decrypted"
if decrypt_encrypt in "Ee":
    decrypt_encrypt = "encrypted"
print(f"Your {decrypt_encrypt} message is: {caeser_shift(mess, decrypt_encrypt, int(shift))}")