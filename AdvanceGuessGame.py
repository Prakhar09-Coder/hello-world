"""
Author: Prakhar
Date: 22nd July 2020
Purpose: To Learn And Practice ProblemS
"""
                                   #Advanced Guess Game
import random

def guessgame(a,b,actual):
    guess=int(input(f"guess a number between {a} and {b}"))
    nguess=1
    while guess != actual:
        if guess<actual:
            guess=int(input("Enter A bigger Number"))
            nguess+=1      #this is done to count number of guesses by increasing the number of guesses each time by 1.

        else:
            guess=int(input("Enter A Smaller No."))
            nguess+=1

    print(f"you guessed the number in {nguess} guesses")
    return nguess

if __name__=="__main__":
    a=int(input("Enter The value of a"))
    b=int(input("Enter The value of b"))
    actual1=random.randint(a,b)    #randint function of random helps to randomly select any value b/w a & b.
    print("PLAYER 1'S TURN")
    g1=guessgame(a,b,actual1)
    print("PLAYER 2'S TURN")
    actual2 = random.randint(a, b)    #actual1 & actual2 are taken so that player 2 does not simply copy the number and win it , basically actual2 will randomly choose its value again
    g2 = guessgame(a,b,actual2)
                                       #g1 and g2 are no. of guesses by player 1 and player 2 respectively.
    if g1>g2:
        print("PLAYER 1 WON\n")

    elif g1<g2:
        print("PLAYER 2 WON\n")

    else:
        print("its a tie")

print(f"the number for player 1 was {actual1} and player 2 was {actual2}")

