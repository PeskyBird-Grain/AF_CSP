# AF, Nesting

"""for number in range(2,22,2):
    print(number)"""

csp = ["Remy", "Alex", "Gabe", "Bliss", "Elsie", "Ivan", "Caydon", "Kaylee", "Levi", "Masen", "William", "Carrera"]
if len(csp) > 0:
    for student in csp:
        print(f"Checking in {student}")
else:
    print("There is no on in this class.")

while True:
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username == "AlexF4" and password == "Al3x!23":
        print("Welcome!!")
        break
    else:
        print("Incorrect credentials.")