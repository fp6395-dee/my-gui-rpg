import random

def check_win(board, player):
    win_coords = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for coord in win_coords:
        if board[coord] == board[coord] == board[coord] == player:
            return True
    return False

def check_draw(board):
    return " " not in board

def get_bot_move(board):
    for i in range(9):
        if board[i] == " ":
            board_copy = board.copy()
            board_copy[i] = "O"
            if check_win(board_copy, "O"):
                return i
    for i in range(9):
        if board[i] == " ":
            board_copy = board.copy()
            board_copy[i] = "X"
            if check_win(board_copy, "X"):
                return i
    if board[4] == " ":
        return 4
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(empty_cells) if empty_cells else None