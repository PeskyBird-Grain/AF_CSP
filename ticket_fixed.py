# AF, Vibe Code for a Theater
while True:
    try:
        age = int(input("Enter your age: "))
        if age >= 0:
            matinee = input("Is this a matinee? (yes/no): ").lower()

            if age < 5:
                price = 0
            elif age < 13:
                price = 8
            elif age < 65:
                price = 12
            else:
                price = 9

            if matinee == "yes":
                price = price - 3
                if price < 0:
                    price = 0

            print(f"Ticket price: ${price:.2f}")
            break
        else:
            print("Invalid age")
            break
    except:
        print("Invalid age")
        break
        