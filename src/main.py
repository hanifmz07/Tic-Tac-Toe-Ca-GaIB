import numpy as np
import os
from func import *

board = np.array([
    [ ' ', ' ', ' ' ], 
    [ ' ', ' ', ' ' ], 
    [ ' ', ' ', ' ' ] 
])

print("Welcome to Tic-Tac-Toe game!")
print("Choose player:")
print("\t1. First Player")
print("\t2. Second Player")
while True:
    try:
        id_player = int(input())
        if id_player == 1:
            player_turn = True
            break
        elif id_player == 2:
            player_turn = False
            break
        else:
            print("Invalid input")
    except:
        print("Invalid input")
        continue

os.system('cls')

while True:
    print_board(board)
    if player_turn:
        print("Input row and column index (0-2) :")
        print("Example : 1 2")
        while True:
            input_player = input().split()
            if len(input_player) != 2:
                print("Invalid input")
                continue
            row, col = map(int, input_player)
            if col < 0 or col > 2 or row < 0 or col > 2:
                print("Invalid input")
            else:
                break
        board[row, col] = "X"
        os.system('cls')
    else:
        bestMove = best_move(board, first_player=False)
        board[bestMove[0], bestMove[1]] = "O"
        os.system('cls')
        print(f"AI played {bestMove[0]} {bestMove[1]}!")

    player_turn = not player_turn
    
    if is_terminal(board):
        print_board(board)
        if value(board) == 1:
            print("Player wins!")
        elif value(board) == -1:
            print("AI wins!")
        else:
            print("It's a draw!")
        break