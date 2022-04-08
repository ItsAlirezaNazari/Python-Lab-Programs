import time
import random

def check():
    symbol = ""
    
    if game[0][0] == game[1][1] and game[1][1] == game[2][2]:
        symbol = game[0][0]

    if game[0][2] == game[1][1] and game[1][1] == game[2][0]:
        symbol = game[0][2]

    for i in range(3):
        if game[i][0] == game[i][1] and game[i][1] == game[i][2]:
            symbol = game[i][0]
            break

        if game[0][i] == game[1][i] and game[1][i] == game[2][i]:
            symbol = game[0][i]
            break
    
    if symbol == "X":
        print("Player 1 Wins")
        return True
    elif symbol == "O":
        print("Player 2 Wins")
        return True


game = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

print("Tell me how many you are: ")
players_count = int(input())

start = time.time()

while True:
    print("Player 1")
    while True:
        row = int(input())
        col = int(input())
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == " ":
                game[row][col] = "X"
                break
            else:
                print("deghat nakardi bache, try again")
        else:
            print("mese adam vared kon")

    for row in game:
        print(row)
    
    if check():
        break

    print("Player 2")
    if players_count < 2:
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if game[row][col] == " ":
                game[row][col] = "O"
                break
    else:
        while True:
            row = int(input())
            col = int(input())
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == " ":
                    game[row][col] = "O"
                    break
                else:
                    print("deghat nakardi bache, try again")
            else:
                print("mese adam vared kon")

    for row in game:
        print(row)
    
    if check():
        break

end = time.time()
running_time = end - start
print(round(running_time), "Seconds")

