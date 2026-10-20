# AF, Vibe Code for a theater
age = int(input("Enter your age: "))
matinee = input("Is this a matinee? (yes/no): ").lower()

if age < 5:
    price = 0
elif age < 12:
    price = 8
elif age < 65:
    price = 12
else:
    price = 9

if matinee == "yes":
    price = price - 3

print(f"Ticket price: ${price}")