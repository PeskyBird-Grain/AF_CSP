# AF, Loops Notes
import random
count = 1

while count <= 10:
    print(count)
    count += 1


goose = random.randint(1,11)
ducks = 1

while True:
    print("Duck")
    if ducks == goose:
        break
    ducks += 1
print("GOOSE!!!!!")


siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]
print(siblings[2])
print(siblings)
siblings.append("Jayshree")
siblings.insert(3,"LaRose")
print(siblings)
siblings.pop(3)
print(siblings)


for number in range(1,11,2):
    print(number)

for item in (siblings):
    print(item + " LaRose")