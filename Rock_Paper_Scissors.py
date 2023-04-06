import random

choices = ['rock', 'paper', 'scissors']
choices2 = ['y', 'n']


while True:
    computer = random.choice(choices)
    player = None
    play_again = None

    while player not in choices:
        player = input('Rock, paper or scissors?: ').lower()

    if player == computer:
        print('Player:', player)
        print('Computer:', computer)
        print('Tie!')

    elif player == "scissors":
        print('Player:', player)
        print('Computer:', computer)
        if computer == 'rock':
            print('You lose!')
        else:
            print('You win!')

    elif player == "rock":
        print('Player:', player)
        print('Computer:', computer)
        if computer == 'scissors':
            print('You win!')
        else:
            print('You lose!')

    elif player == "paper":
        print('Player:', player)
        print('Computer:', computer)
        if computer == 'rock':
            print('You win!')
        else:
            print('You lose!')

    while play_again not in choices2:
        play_again = input('Do you want to play again?(y/n): ').lower()

    if play_again != 'y':
        break

print('Thanks for playing!')