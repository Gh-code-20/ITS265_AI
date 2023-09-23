# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 22:55:28 2021
Game:  Tic-Tac-Toe using MiniMax
Adopted from:  https://github.com/javacodingcommunity/TicTacToeAI-with-Minimax

@author: acybe
"""

import sys

#board = [' ' for x in range(10)]
board = {1: ' ', 2: ' ', 3: ' ', 4: ' ',
         5: ' ', 6: ' ', 7: ' ', 8: ' ',
         9: ' ', 10: ' ', 11: ' ', 12: ' ',
         13: ' ', 14: ' ', 5: ' ', 16: ' '}


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4])
    print('-+-+-+-+-')
    print(board[5] + '|' + board[6] + '|' + board[7] + '|' + board[8])
    print('-+-+-+-+-')    
    print(board[9] + '|' + board[10] + '|' + board[11] + '|' + board[12])
    print('-+-+-+-+-')
    print(board[13] + '|' + board[14] + '|' + board[15] + '|' + board[16])
    print('-+-+-+-+-') 
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

#int sizeToWin = Math.min(size, 5);
        
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] != ' '):
        return True
    elif (board[5] == board[6] and board[5] == board[7] and board[5] == board[8] and board[5] != ' '):
        return True
    elif (board[9] == board[10] and board[9]== board[11] and board[9] == board[12] and board[9]  != ' '):
        return True
    elif (board[13] == board[14] and board[13] == board[15] and board[13] == board[16] and board[13] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == board[13] and board[1] != ' '):
        return True
    elif (board[2] == board[6] and board[2] == board[10] and board[2] == board[14] and board[2] != ' '):
        return True
    elif (board[3] == board[7] and board[3]== board[11] and board[3] == board[15] and board[3]  != ' '):
        return True
    elif (board[4] == board[8] and board[4] == board[12] and board[4] == board[16] and board[4] != ' '):
        return True
    elif (board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] != ' '):
        return True
    elif (board[4] == board[7] and board[4] == board[10] and board[4] == board[13] and board[4] != ' '):
        return True
    else:
        return False 

# check which player won
def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] == mark):
        return True
    elif (board[5] == board[6] and board[5] == board[7] and board[5] == board[8] and board[5] == mark):
        return True
    elif (board[9] == board[10] and board[9]== board[11] and board[9] == board[12] and board[9]  == mark):
        return True
    elif (board[13] == board[14] and board[13] == board[15] and board[13] == board[16] and board[13] == mark):
        return True 
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == board[13] and board[1] == mark):
        return True
    elif (board[2] == board[6] and board[2] == board[10] and board[2] == board[14] and board[2] == mark):
        return True
    elif (board[3] == board[7] and board[3]== board[11] and board[3] == board[15] and board[3]  == mark):
        return True
    elif (board[4] == board[8] and board[4] == board[12] and board[4] == board[16] and board[4] == mark):
        return True
    elif (board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] == mark):
        return True
    elif (board[4] == board[7] and board[4] == board[10] and board[4] == board[13] and board[4] == mark):
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
                print("Computer wins!")
                sys.exit()
            else:
                print("Player wins!")
                sys.exit()
        return
    
    else:
        print("Can't insert there!")
        position = int(input("Enter new position: "))
        insertLetter(letter, position)
        return

player = 'O'
bot = 'X'

# Function to prompt player to enter uppercase letter into board position
# Player will use O in this game
def playerMove():
    position = int(input("Enter the psotion for 'O': "))
    insertLetter(player, position)
    return

# Function to prompt computer to enter uppercase letter into board position
# Computer will  use X in this game
# Will check with minmax algorithm if it is best move.
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
    elif checkWhichMarkWon(player):  # check if player won
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
                board[key] = player
                score = minimax(board, 0, True)
                board[key] = ' '
                if(score < bestScore):
                    bestScore = score
        return bestScore   
           
while not checkForWin():
    compMove()
    playerMove()
    
# printBoard(board) 
# print(spaceIsFree(1))
# insertLetter('x',1)