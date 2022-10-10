import random
computerGuess = random.randint(1,101)

print("\t\tHi! Here computer picked a number between (1-100).\n\t\tNow your task in pick that number by guessing!")


def isCorrectguess(guess):
    if guess==computerGuess : return "correct"
    elif guess<computerGuess : return "Too small!"
    elif guess>computerGuess : return "Too high!"


userGuess = int(input("guess a number : "))
count = 0
result = ""

while(1):
    result = isCorrectguess(userGuess)
    count+=1

    if result =="correct" : 
        print("\t\t\tU GUESSED",computerGuess,"IN",count,"CHANCES! :)")
        break
    else:
        print("\t\t",isCorrectguess(userGuess))
        userGuess = int(input("guess a number : "))





