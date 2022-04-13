m = int(input())
n = int(input())

for row in range(1, m+1):
    print()
    for col in range(1, n+1):
        print(col * row, end="\t")

