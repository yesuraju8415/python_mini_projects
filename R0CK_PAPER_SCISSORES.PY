

import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer = (random.choice(['r', 'p', 's']))

    USER = fullForm(user);
    COMPUTER =fullForm(computer);

    print("\tuser choice : ",USER)
    print("\tcomputer choice : ",COMPUTER)

    if user == computer:
        return "IT'S TIE!"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'U WON! :)'

    return 'U LOST! :('

def is_win(player, opponent): # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

def fullForm(letter): #changing r --> rock,p --> paper,s -->scissors
    return ("ROCK" if letter == 'r' else  
            "PAPER" if letter == 'p' else 
            "SCISSORES" if letter == 's' else
             "invalid")

print("\t\t",play(),"\n")