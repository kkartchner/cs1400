"""
Ky Kartchner
CS 1400-1
Assignment 6

task 1: Prompts the user to enter their move (0-Rock, 1-Paper, 2-Scissors), randomly generates a 0, 1, or 2 for the
computer's move, then determines and displays the winner. The user is then asked if they would like to play again.
"""
from random import randint
play_again = 'Y'


def name_of_move(move):
    if move == 0:
        return "Rock"
    elif move == 1:
        return "Paper"
    elif move == 2:
        return "Scissors"


print("Welcome to Rock-Paper-Scissors!")
while play_again == 'Y' or play_again == 'y':
    user_move = eval(input("\nEnter your move (0-Rock, 1-Paper, 2-Scissors): "))
    if user_move > 2 or user_move < 0:
        print("Invalid move. Enter only 0, 1, or 2")
    else:
        ai_move = randint(0, 2)
        if user_move == ai_move:
            round_result = "It's a tie!"
        elif (user_move - ai_move) % 3 == 1:
            round_result = "You won! :)"
        else:
            round_result = "You lost :("

        print("You chose " + name_of_move(user_move) + ". AI chose " + name_of_move(ai_move) + ".\n" + round_result)
        play_again = input("\nWould you like to play again? (Y/N): ")