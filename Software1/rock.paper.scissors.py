import random


def rock_paper_scissors():
    choices = ('Rock', 'Paper', 'Scissors')
    chosen = random.choice(choices)
    return chosen


def user_rock_paper():
    print("Choose:\nRock\nPaper\nScissors\nUse Enter to quit")
    user_choice = input("Which one do you choose? ")
    user_choice = user_choice.title()
    return user_choice


def winner():
    computer = rock_paper_scissors()
    while True:
        user = user_rock_paper()
        if computer == user:
            print("Draw")
        if ((computer == 'Rock' and user == 'Paper') or (computer == 'Paper' and user == 'Scissors')
              or (computer == 'Scissors' and user == 'Rock')):
            print(f'You chose {user}, I chose {computer}. You won...')
        else:
            print(f'You chose {user}, I chose {computer}. I won!')


winner()
