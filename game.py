import random

computer_number = random.randint(10, 20)
attempts = 0

while True:
    user_number = int(input())
    attempts = attempts + 1

    if user_number == computer_number:
        print("Tabrikkkk!! ❤")
        break
    elif user_number < computer_number:
        print("Boro bala ⬆")
    elif user_number > computer_number:
        print("Boro paeen ⬇")


print("Your attempts:", attempts, "\nEnd of Game, Come back soon 😉")
