def create_board():
    return [" " for _ in range(9)]

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    win_coords = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Строки
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Столбцы
        (0, 4, 8), (2, 4, 6)             # Диагонали
    ]
    for coord in win_coords:
        if board[coord[0]] == board[coord[1]] == board[coord[2]] == player:
            return True
    return False

def check_draw(board):
    return " " not in board