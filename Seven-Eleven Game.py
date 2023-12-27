'''
Programmer: Raj Shah
Version: 1.1
Description: A game is played where the player rolls two dice. If the sum of the dice is neither
seven nor eleven, the player is awarded a number of points equal to the larger of the two values
rolled. The player has up to 10 rolls to accumulate points; however, if the sum is either seven or
eleven, the player loses all his/her points. The player can choose to stop at any point, keeping
his/her points from previous rounds.
Date: July 8, 2022



pre-condition: one string input, enter 'y' or enter 'n'. If incorrect input is entered, program will terminate.
post-condition: prints what round the player is on, what the roll values are, and what the current and final score is.

'''

import random
score = 0   # define score

for i in range(1, 11):   
    dice1 = random.randint(1, 6)    # roll dices
    dice2 = random.randint(1, 6)
    
    print("This is round ", i, "!", sep = '')
    play_round = input("Would you like to play this round? (y/n): ")   # ask user to play current round
    
    if play_round == 'y':
        if dice1 + dice2 == 7 or dice1 + dice2 == 11:   # if the sum of the dices eqauls to 7 or 11, reset the score to 0
            score = 0
        else:
            if dice1 >= dice2:    # if it is not equal to 7 or 11, add the largest dice to the score
                score += dice1
            else:
                score += dice2
                
        print("Roll 1:", dice1)     # print all the statistics once round is over
        print("Roll 2:", dice2)
        print("Current Score:", score)
        print()
        
    elif play_round == 'n':    
        print("Okay, round", i, "will be skipped, you still have", score, "points.")     # skip the round
        print()
    else:
        print("That is not a valid entry. Terminating the game.")     # terminate if invalid entry is inputted
        break
    
print()
print("Thanks for playing!")
print("Final Score:", score)    # display end message and final score
