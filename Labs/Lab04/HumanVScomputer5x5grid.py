# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:49:16 2021

@author: acybe
"""

"""
Game:  Tic-Tac-Toe using MiniMax
Adopted from:  https://github.com/javacodingcommunity/TicTacToeAI-with-Minimax
"""

import sys

#board = [' ' for x in range(10)]
board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 
         11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ',
         16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ',
         21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8] + '|' + board[9] + '|' + board[10])
    print('-+-+-+-+-')    
    print(board[11] + '|' + board[12] + '|' + board[13] + '|' + board[14] + '|' + board[15])
    print('-+-+-+-+-')
    print(board[16] + '|' + board[17] + '|' + board[18] + '|' + board[19] + '|' + board[20])
    print('-+-+-+-+-') 
    print(board[21] + '|' + board[22] + '|' + board[23] + '|' + board[24] + '|' + board[25])
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
    if (board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] == board[5] and board[1] != ' '):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and board[6] == board[9] and board[6] == board[10] and board[6] != ' '):
        return True
    elif (board[11] == board[12] and board[11]== board[13] and board[11] == board[14] and board[11] == board[15] and board[11] != ' '):
        return True
    elif (board[16] == board[17] and board[16]== board[18] and board[16] == board[19] and board[16] == board[20] and board[16] != ' '):
        return True
    elif (board[21] == board[22] and board[21] == board[23] and board[21] == board[24] and board[21] == board[25] and board[21] != ' '):
        return True     
    elif (board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] == board[21] and board[1] != ' '):
        return True
    elif (board[2] == board[7] and board[2] == board[12] and board[2] == board[17] and board[2] == board[22] and board[2] != ' '):
        return True
    elif (board[3] == board[8] and board[3] == board[13] and board[3] == board[18] and board[3] == board[23] and board[3] != ' '):
        return True
    elif (board[4] == board[9] and board[4] == board[14] and board[4] == board[19] and board[4] == board[24] and board[4] != ' '):
        return True
    elif (board[5] == board[10] and board[5] == board[15] and board[5] == board[20] and board[5] == board[25] and board[5] != ' '):
        return True
    elif (board[1] == board[7] and board[1] == board[13] and board[1] == board[19] and board[1] == board[25] and board[1] != ' '):
        return True
    elif (board[5] == board[9] and board[5] == board[13] and board[5] == board[17] and board[5] == board[21] and board[5] != ' '):
        return True
    else:
        return False

# check which player won
def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] == board[5] and board[1] == mark):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and board[6] == board[9] and board[6] == board[10] and board[6] == mark):
        return True
    elif (board[11] == board[12] and board[11]== board[13] and board[11] == board[14] and board[11] == board[15] and board[11] == mark):
        return True
    elif (board[16] == board[17] and board[16]== board[18] and board[16] == board[19] and board[16] == board[20] and board[16] == mark):
        return True
    elif (board[21] == board[22] and board[21] == board[23] and board[21] == board[24] and board[21] == board[25] and board[21] == mark):
        return True     
    elif (board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] == board[21] and board[1] == mark):
        return True
    elif (board[2] == board[7] and board[2] == board[12] and board[2] == board[17] and board[2] == board[22] and board[2] == mark):
        return True
    elif (board[3] == board[8] and board[3] == board[13] and board[3] == board[18] and board[3] == board[23] and board[3] == mark):
        return True
    elif (board[4] == board[9] and board[4] == board[14] and board[4] == board[19] and board[4] == board[24] and board[4] == mark):
        return True
    elif (board[5] == board[10] and board[5] == board[15] and board[5] == board[20] and board[5] == board[25] and board[5] == mark):
        return True
    elif (board[1] == board[7] and board[1] == board[13] and board[1] == board[19] and board[1] == board[25] and board[1] == mark):
        return True
    #elif (board[21] == board[17] and board[21] == board[13] and board[21] == board[9] and board[21] == board[5] and board[21] == mark):
    elif (board[5] == board[9] and board[5] == board[13] and board[5] == board[17] and board[5] == board[21] and board[5] == mark):
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
                print("Player wins!")
                sys.exit()
            else:
                print("Computer wins!")
                sys.exit()
        return
    
    else:
        print("Can't insert there!")
        position = int(input("Enter new position: "))
        insertLetter(letter, position)
        return

player = 'X'
bot = 'O'

# Function to prompt player to enter uppercase letter into board position
# Player will use O in this game
def playerMove():
    position = int(input("Player Move, Enter the psotion for 'X': "))
    insertLetter(player, position)
    return

# Function to prompt computer to enter uppercase letter into board position
# Computer will  use X in this game
# Will check with minmax algorithm if it is best move.
def compMove():
#    position = int(input("Enter the postion for 'O': "))
#    insertLetter(bot, position)
    bestScore = -1 # initialize with any number
    bestMove = 0     # initialize
    
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
    print("\nWelcome to the Tic Tac Toe!")
    playerMove()
    compMove()
    
    
    
# printBoard(board) 
# print(spaceIsFree(1))
# insertLetter('x',1)

