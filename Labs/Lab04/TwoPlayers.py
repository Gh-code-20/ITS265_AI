# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:09:49 2021

@author: acybe
"""


import sys

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')    
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')  
    print("\n")
    

# chck if board position is free - a space
def spaceIsFree(position):
    if(board[position] == ' '):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False    # if there are empty spaces then still can play
    return True             # it is a draw
        
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7]== board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

# check which player won
def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7]== board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False
    
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        
        if(checkDraw()):
            print("Draw!")
            sys.exit()
            
        if checkForWin():
            if letter == 'X':
                print("Plyer2 wins!")
                sys.exit()
            else:
                print("Player1 wins!")
                sys.exit()
        return
    
    else:
        print("Can't insert there!")
        position = int(input("Enter new position: "))
        insertLetter(letter, position)
        return

player1 = 'O'
player2 = 'X'

def player1Move():
#    position = int(input("Enter the postion for 'O': "))
#    insertLetter(bot, position)
    # bestScore = -1 # initialize with any number
    # bestMove = 0      # initialize
    
    position = int(input("Player1, Enter the psotion for 'O': ")) #only int
    insertLetter(player1, position)
    return

# Function to prompt player to enter uppercase letter into board position
# Player will use O in this game
def player2Move():
    position = int(input("Player2, Enter the psotion for 'X': ")) #only int
    insertLetter(player2, position)
    return


# Define the minmax function 
# computer plays against itself playing the game out
def minimax(board, depth, isMaximizing):
    if checkWhichMarkWon(player1):    # check if bot won
        return -1
    elif checkWhichMarkWon(player2):  # check if player won
        return 1
    elif checkDraw():
        return 0
    
    # if maximizing (playing as computer) take score with highest move value
    if isMaximizing:   
        bestScore = -1
        
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player2
                score = minimax(board, 0, False)
                board[key] = ' '
                if(score > bestScore):
                    bestScore = score
        return bestScore
    else:                       # if you are not maximizing, best score is low score
        bestScore = 1
        
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player1
                score = minimax(board, 0, True)
                board[key] = ' '
                if(score < bestScore):
                    bestScore = score
        return bestScore   
           
while not checkForWin():
    player1Move()
    player2Move()
    

# printBoard(board) 
# print(spaceIsFree(1))
# insertLetter('x',1)
