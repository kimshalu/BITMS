name = "Shalu"

for i in range(len(name)):
    for j in range(len(name)):
        if i == j or i + j == len(name) - 1:
            print(name[i], end="")
        else:
            print(" ", end="")
    print()
    