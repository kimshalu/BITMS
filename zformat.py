
name = "Shalu"

for i in range(len(name)):
    for j in range(len(name)):
        if i == 0 or i == len(name) - 1 or i + j == len(name) - 1:
            print(name[j], end="")
        else:
            print(" ", end="")
    print()
