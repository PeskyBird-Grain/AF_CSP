# AF, Number Information

for number in range(1,21):
    if number%2 == 0:
        num = "even"
        if number%5 != 0:
            div = "not divisible by 5"
        else:
            div = "divisible by 5"
    else:
        num = "odd"
        if number%5 != 0:
            div = "not divisible by 5"
        else:
            div = "divisible by 5"
    print(f"\n{number} is {num} and {div}")