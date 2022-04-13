m = int(input())
n = int(input())

for row in range(m):
    print()
    if (row % 2) == 0:
        even = "O"
        odd = "X"
    else:
        even = "X"
        odd = "O"

    for col in range(n):
        if (col % 2) == 0:
            print(even, end=" ")
        else:
            print(odd, end=" ")

