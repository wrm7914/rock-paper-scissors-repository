# this is the "game.py" file...

import random

print("Rock, Paper, Scissors, Shoot!")

print("WELCOME TO ROCK PAPER SCSSORS GAME")



# USE INPUTS

user_choice = input("Please make a selection ('rock', 'paper', 'scissors'): ")
user_choice = user_choice.lower()

valid_options = ["rock", "paper", "scissors"]
# VALIDATE USER INPUTS
print("You chose:", user_choice)

print(f"You chose: '{user_choice}'")
if user_choice not in valid_options:
    # ALL THE STUFF INDENTED
    print("OOPS INVALID TRY AGAIN")
    exit()  #quit()
# DETERMINE THE WINNER

# DISPLAY RESULTS

# Welcome 'Player One' to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
print("You chose:", user_choice)


computer_choice = random.choice(valid_options)
print("comuter chose:", computer_choice)

# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.


# adapted from code shared in slack by Bonnie:
# https://nyu-tech-2335.slack.com/archives/C5WPFSB52/p1657672686150239


if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock crushes scissors. You lose.")
# Thanks for playing. Please play again!

