# AF, Your Budget

while True:
    try:
        income = float(input("What is your monthly income: $"))
        break
    except:
        print("Only use whole numbers.")
while True:
    try:
        rent = float(input("What is your monthly rent/mortgage: $"))
        break
    except:
        print("Only use whole numbers.")
while True:
    try:
        utilities = float(input("What is your monthly utilities: $"))
        break
    except:
        print("Only use whole numbers.")
while True:
    try:
        groceries = float(input("What is your monthly groceries: $"))
        break
    except:
        print("Only use whole numbers.")
while True:
    try:
        transport = float(input("What is your monthly transportation: $"))
        break
    except:
        print("Only use whole numbers.")
print(f"Your rent is ${rent:2f} and that is {int(rent//income*100)}% of your income")
print(f"Your utilities are ${utilities:2f} and that is {int(utilities//income*100)}% of your income")
print(f"Your groceries are ${groceries:2f} and that is {int(groceries//income*100)}% of your income")
print(f"Your transportation is ${transport:2f} and that is {int(transport//income*100)}% of your income")
print(f"You should save ${} a month, which is 10% of your income")
print(f"You have ${income-(rent+utilities+groceries+transport):2f}")
