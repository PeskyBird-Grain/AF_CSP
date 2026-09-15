# AF, Hello User
while True:
    name = input("What is your first name: ").capitalize().strip()
    if name.isnumeric():
        print("Wait!! There shouldn't be a number...")
    elif " " in name:
        print("Wait!! Only type your FIRST name...")
    else:
        break

while True:
    try: 
        age = int(input("How old are you: "))
        break
    except:
        print("Wait!! Your age should be a number...")

print(f"Wow {name}!! You are {age} years old. You're ancient!!")