# --------------------------------------------
# Project  : Rock-Paper-Scissors Game
# Author   : [Abhinav Pal]
# Role     : Intern @ CodSoft
# Description:
#     This is a simple Rock-Paper-Scissors game
#     where the user plays against the computer.
#     It tracks scores and supports multiple rounds.
# --------------------------------------------

import random

print("Welcome to Rock-Paper-Scissors!")
print("Instructions:")
print("- Type rock, paper, or scissors to play.")
print("- Type exit to quit the game at any time.\n")

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Your move (rock/paper/scissors): ").lower()

    if user_choice == "exit":
        print("\nThanks for playing! Final scores:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break

    if user_choice not in options:
        print("Invalid input. Please choose rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!")
        user_score += 1
    else:
        print("You lose this round.")
        computer_score += 1

    # Show current score
    print(f"Score You: {user_score} | Computer: {computer_score}\n")
