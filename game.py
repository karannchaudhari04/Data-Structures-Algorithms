import random

def play_game():

    lucky_number = random.randint(1,50)
    while True:
        num = int(input("Guess a lucky number: "))

        if num == lucky_number:
            print()
            print("You guessed a lucky number, You won the game")
            break

        elif num > lucky_number:
            print("Too high")

        elif num < lucky_number:
            print("Too low")

    print("Thank you for playing the game")

play_game()
