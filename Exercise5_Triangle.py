height = int(input("Enter the height of th triangle (in row):\n"))

for i in range (1, height + 1):
    for j in range (i):
        print("*", end="")

        print()