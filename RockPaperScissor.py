# Ask the user to make a choice 
# If choice is not valid 
#     Print an error
# let the computer to make a choice 
# Print choice (Emojis)
# Determine the Winner
# Ask the user if they want to continue
# If not 
#     Terminate

import random

choices = ('r', 'p', 's')

def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')

def display_choices(user_choice, computer_choice):
    print(f'YOu chose {user_choice}')
    print(f'computer chose {computer_choice}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print('You win')
    else:
        print('You lose')


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()