name = "Shalu"

for i in range(len(name)):
    for j in range(len(name)):
        if i == j and i <= len(name)//2:
            print(name[i], end="")
        elif i + j == len(name) - 1 and i <= len(name)//2:
            print(name[j], end="")
        elif j == len(name)//2 and i > len(name)//2:
            print(name[j], end="")
        else:
            print(" ", end="")
    print()
