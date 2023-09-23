# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:35:21 2021

@author: acybe
"""

"""
Game:  Tic-Tac-Toe using MiniMax
Adopted from:  https://github.com/javacodingcommunity/TicTacToeAI-with-Minimax
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
                print("Bot wins!")
                sys.exit()
            else:
                print("Bot2 wins!")
                sys.exit()
        return
    
    else:
        print("Can't insert there!")
        position = int(input("Enter new position: "))
        insertLetter(letter, position)
        return

#player = 'O'
bot = 'X'
bot1 = 'O'

def compMove1():
#    position = int(input("Enter the postion for 'O': "))
#    insertLetter(bot, position)
    bestScore = -1 # initialize with any number
    bestMove = 0      # initialize
    
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot1
            score = minimax1(board, 0, False)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter(bot1, bestMove)    
    return  
#  The bots should use the minimax algorithm 
# to calculate their best moves against each other.
def minimax1(board, depth, isMaximizing):
    if checkWhichMarkWon(bot1):    # check if bot won
        return 1
    elif checkWhichMarkWon(bot):  # check if player won
        return -1
    elif checkDraw():
        return 0
    
    # if maximizing (playing as computer) take score with highest move value
    if isMaximizing:   
        bestScore = -1
        
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot1
                score = minimax1(board, 0, False)
                board[key] = ' '
                if(score > bestScore):
                    bestScore = score
        return bestScore
    else:                       # if you are not maximizing, best score is low score
        bestScore = 1
        
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax1(board, 0, True)
                board[key] = ' '
                if(score < bestScore):
                    bestScore = score
        return bestScore  
    
def compMove():
#    position = int(input("Enter the postion for 'O': "))
#    insertLetter(bot, position)
    bestScore = -1 # initialize with any number
    bestMove = 0      # initialize
    
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter(bot, bestMove)    
    return  


# Define the minmax function
# computer plays against itself playing the game out
def minimax(board, depth, isMaximizing):
    if checkWhichMarkWon(bot):    # check if bot won
        return 1
    elif checkWhichMarkWon(bot1):  # check if player won
        return -1
    elif checkDraw():
        return 0
    
    # if maximizing (playing as computer) take score with highest move value
    if isMaximizing:   
        bestScore = -1
        
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = ' '
                if(score > bestScore):
                    bestScore = score
        return bestScore
    else:                       # if you are not maximizing, best score is low score
        bestScore = 1
        
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot1
                score = minimax(board, 0, True)
                board[key] = ' '
                if(score < bestScore):
                    bestScore = score
        return bestScore  
    
def nextmove():
    reply= input("Y/N to continu: ")
    if reply[0] == 'Y':
        compMove()
        return True
    elif reply[0] == 'N':
        print('Exit the game')
        sys.exit()
    else:
        print("Please enter a diffrent letter")
        
def nextmove1():
    reply= input("Y/N to continu: ")
    if reply[0] == 'Y':
        compMove1()
        return True
    elif reply[0] == 'N':
        print('Exit the game')
        sys.exit()
    else:
        print("Please enter a diffrent letter")
           
while not checkForWin():
    nextmove()
    nextmove1()
    
    
# printBoard(board) 
# print(spaceIsFree(1))
# insertLetter('x',1)

"""
Modify the Python code to allow two computers (bot1 and bot2) to play each other –
this should always result in a draw. After each move by each bot, display the board
state and prompt to the console “Make next move (Y/N)?”. If yes, have the next bot
make the move and print out the board at that point. If no, exit the game. The bots
should use the minimax algorithm to calculate their best moves against each other.

"""

