number = int(input("Enter a number of lemons: "))
print("equal" if number == 21 else "less by {}".format(21 - number) if number < 21 else "more by {}".format(number - 21))
