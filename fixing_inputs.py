# AF, Fixing Inputs

# When you want a specific input
while True:
    color = input("Type a color that is only one word: ").lower().strip()
    if color.isnumeric():
        print("That isn't a color!!")
    elif " " in color:
        print("I said one word!!")
    else:
        break

print(f"The sky is {color}... maybe")

# When you want a number
while True:
    try: 
        age = int(input("how old are you: "))
        break
    except:
        print("That isn't a number!! Try again.")

print(f"Wow!! You are {age} years old. You're ancient!!")