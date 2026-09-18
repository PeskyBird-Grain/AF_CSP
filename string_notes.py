# AF, String Notes

first_name = "Alex"
last_name = 'Fulton'

#concatenation
name = first_name+" "+last_name
print(name)

# Escape character lets the program ignore the next character in the string
print('Ms. LaRose told the class "You can\'t drive my car."')

user = input('Please tell me your name:\n')

print(f"New user recognized\nWelcome {user}")

# f-string = formatted string used to  easily insert variables and specify how it prints for the user.
print(f'{name} told the class "You can\'t drive my car."')

#Methods

user = input('Please tell me your name:\n').strip().title()
print(f"New user recognized\nWelcome {user}")

sentence = 'The quick brown fox jumped over the lazy dog'
print(f"The sentence is {len(sentence)} characters long.")
print(sentence)
print(sentence.replace("dog", user))