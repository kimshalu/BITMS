try:
    # Division by zero error
    x = 10 / 0
except ZeroDivisionError:
    print("Error 1: Division by zero")

try:
    # Index out of range error
    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError:
    print("Error 2: Index out of range")

try:
    # Value error
    x = int("abc")
except ValueError:
    print("Error 3: Invalid literal for int()")

try:
    # Name error
    print(variable)
except NameError:
    print("Error 4: NameError ")

try:
    # Type error
    print("5" + 5)
except TypeError:
    print("Error 5: TypeError - Cannot concatenate str and int objects")
