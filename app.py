#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

def welcome():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    print("The first to 3 wins is the winner!")
    print("Good luck!")
    print("")

def menu():
    print("Please choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user = int(input("Enter your option here: "))
    return user

def validateInput():
    user = menu()
    while user < 1 or user > 3:
        print("Invalid input. Please try again.")
        user = menu()
    return user

def turnOfComputer():
    import random
    computer = random.randint(1,3)
    return computer 

def playAgain():
    print("Would you like to play again?")
    print("1. Yes")
    print("2. No")
    user = int(input("Enter your option here: "))
    while user < 1 or user > 2:
        print("Invalid input. Please try again.")
        user = int(input("Enter your option here: "))
    return user

def score(user, computer):
    global userScore
    global computerScore
    if user == 1:
        if computer == 1:
            print("You chose Rock and the computer chose Rock. It's a tie!")
        elif computer == 2:
            print("You chose Rock and the computer chose Paper. You lose!")
            computerScore += 1
        else:
            print("You chose Rock and the computer chose Scissors. You win!")
            userScore += 1
    elif user == 2:
        if computer == 1:
            print("You chose Paper and the computer chose Rock. You win!")
            userScore += 1
        elif computer == 2:
            print("You chose Paper and the computer chose Paper. It's a tie!")
        else:
            print("You chose Paper and the computer chose Scissors. You lose!")
            computerScore += 1
    else:
        if computer == 1:
            print("You chose Scissors and the computer chose Rock. You lose!")
            computerScore += 1
        elif computer == 2:
            print("You chose Scissors and the computer chose Paper. You win!")
            userScore += 1
        else:
            print("You chose Scissors and the computer chose Scissors. It's a tie!")

def cumulativeScore():
    print("Your score is: " + str(userScore))
    print("The computer's score is: " + str(computerScore))
    
def main():
    welcome()
    global userScore
    global computerScore
    userScore = 0
    computerScore = 0
    while userScore < 3 and computerScore < 3:
        user = validateInput()
        computer = turnOfComputer()
        score(user, computer)
        cumulativeScore()
    if userScore == 3:
        print("You win!")
    else:
        print("You lose!")
    play = playAgain()
    while play == 1:
        main()
    print("Thanks for playing!")

main()
