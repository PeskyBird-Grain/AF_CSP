# AF, Conditionals Notes

millitary_time = 1338

if millitary_time < 600:
    print("It's too early why are you awake!!")
elif millitary_time < 900:
    print("Good morning!!")
elif millitary_time < 1200:
    print("Good morning!! You should be at school!!")
elif millitary_time < 1700:
    print("Good afternoon!!")
else:
    print("Good evening!!")

# Nesting
day = "Saturday"
time = 1000

if time > 900 and time < 1600:
    if day != "Saturday" or day != "Sunday":
        print("You should be at school!!")
    else:
        if time > 1200:
            print("Good afternoon!!")
        else:
            print("Good morning!!")
else:
    print("You don't need to be at school!!")