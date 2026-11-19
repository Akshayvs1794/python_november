import random

def guess_game():
    luckyNum = random.randint(0, 50)

    while True:
        userNum = int(input("Enter yout number :"))

        if userNum == luckyNum:
            print("you won .. Game Over ..")
            break
        elif userNum < luckyNum:
            print("guessed too low")
        else:
            print("guessed too high")

    print("Thank you for playing the game ..")

guess_game()