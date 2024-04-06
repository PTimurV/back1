a = int(input("Введите число: "))
for i in range(0, a, 1):
    for j in range(0, a, 1):
        if a-1-i > j:
            print(" ", end="")
        else:
            print("#", end="")
    print()
