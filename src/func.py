import numpy as np

def value(board):

    for i in range(3):
        if (board[:, i] == "X").all() or (board[i, :] == "X").all():
            return 1
        elif (board[:, i] == "O").all() or (board[i, :] == "O").all():
            return -1
    if (board.diagonal() == "X").all() or (np.rot90(board).diagonal() == "X").all():
        return 1
    elif (board.diagonal() == "O").all() or (np.rot90(board).diagonal() == "O").all():
        return -1
    
    return 0

def is_terminal(board):
    for i in range(3):
        if (board[:, i] == "X").all() or (board[i, :] == "X").all() or (board[:, i] == "O").all() or (board[i, :] == "O").all():
            return True
        
    if (board.diagonal() == "X").all() or (np.rot90(board).diagonal() == "X").all() or (board.diagonal() == "O").all() or (np.rot90(board).diagonal() == "O").all():
        return True
    
    if (board != " ").all():
        return True
    
    return False

def print_board(board):
    print("|||||||||||||||||||||||")
    print("||     ||     ||     ||")
    print(f"||  {board[0, 0]}  ||  {board[0, 1]}  ||  {board[0, 2]}  ||")
    print("||     ||     ||     ||")
    print("|||||||||||||||||||||||")
    print("||     ||     ||     ||")
    print(f"||  {board[1, 0]}  ||  {board[1, 1]}  ||  {board[1, 2]}  ||")
    print("||     ||     ||     ||")
    print("|||||||||||||||||||||||")
    print("||     ||     ||     ||")
    print(f"||  {board[2, 0]}  ||  {board[2, 1]}  ||  {board[2, 2]}  ||")
    print("||     ||     ||     ||")
    print("|||||||||||||||||||||||")


def minimax(board, depth, max_player, alpha, beta):
    if is_terminal(board):
        return value(board)

    if max_player:
        best_max = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == " ":
                    board[i, j] = "X"
                    res = minimax(board.copy(), depth - 1, False, alpha, beta)
                    best_max = max(res, best_max)
                    alpha = max(res, alpha)
                    board[i, j] = " "
                    if beta <= alpha:
                        break
        return best_max
    else:
        best_min = np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == " ":
                    board[i, j] = "O"
                    res = minimax(board, depth - 1, True, alpha, beta)
                    best_min = min(res, best_min)
                    beta = min(res, beta)
                    board[i, j] = " "
                    if beta <= alpha:
                        break
        return best_min

def best_move(board, first_player):
    best_val = -np.inf if first_player else np.inf
    best_move = (-1, -1)
    depth = 0

    for i in range(3):
        for j in range(3):
            if board[i, j] == " ":
                board[i, j] = "X" if first_player else "O"
                res = minimax(board, depth, not first_player, -np.inf, np.inf)
                board[i, j] = " "
                if first_player:
                    if res > best_val:
                        best_move = (i, j)
                        best_val = res
                else:
                    if res < best_val:
                        best_move = (i, j)
                        best_val = res
    
    return best_move