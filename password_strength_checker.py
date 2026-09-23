# AF, Password Strength Checker
up = "False"
low = "False"
num = "False"
symbol = "False"
count = 0
password = input("What is your password: ")
if len(password) >= 8:
    length = "True"
else:
    length = "False"
for letter in password:
    if letter.isupper():
        up = "True"
    if letter.islower():
        low = "True"
    if letter.isnumeric():
        num = "True"
    if letter in "!@#$%^&*()_-+=<>?/.,;:[}{]`~":
        symbol = "True"
    if up == "True":
        count = count + 1