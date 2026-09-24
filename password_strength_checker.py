# AF, Password Strength Checker
one = " "
two = " "
three = " "
four = " "
five = " "
length = "False"
up = "False"
low = "False"
num = "False"
symbol = "False"
count = 0
password = input("What is your password: ")
if len(password) >= 8:
    length = "True"
for letter in password:
    if letter.isupper():
        up = "True"
    if letter.islower():
        low = "True"
    if letter.isnumeric():
        num = "True"
    if letter in "!@#$%^&*()_-+=<>?/.,;:[}{]`~":
        symbol = "True"
if length == "True":
    count = count + 1
if up == "True":
    count = count + 1
if low == "True":
    count = count + 1
if num == "True":
    count = count + 1
if symbol == "True":
    count = count + 1
if length == "False":
    one = "8 characters long"
if up == "False":
    two = "Add uppercase"
if low == "False":
    three = "Add lowercase"
if num == "False":
    four = "Add number"
if symbol == "False":
    five = "Add a symbol"
if count <=2:
    strength = "Weak"
if count == 4 or count == 3:
    strength = "Medium"
if count == 5:
    strength = "Strong"
print("At least 8 characters: " + length)
print("Has an uppercase letter: " + up)
print("Has a lowercase letter: " + low)
print("Has a number: " + num)
print("Has a symbol: " + symbol)
print("Your password strength: " + strength)
print("To make it strong: " + one + two + three + four + five)