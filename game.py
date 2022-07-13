# this is the "game.py" file...

import random

print("Rock, Paper, Scissors, Shoot!")

print("WELCOME TO ROCK PAPER SCSSORS GAME")



# USE INPUTS

user_choice = input("Please make a selection ('rock', 'paper', 'scissors'): ")



# VALIDATE USER INPUTS
print("You chose:", user_choice)

print(f"You chose: '{user_choice}'")

# DETERMINE THE WINNER

# DISPLAY RESULTS

# Welcome 'Player One' to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
print("You chose:", user_choice)

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("comuter chose:", computer_choice)

# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.
# -------------------
# Thanks for playing. Please play again!

