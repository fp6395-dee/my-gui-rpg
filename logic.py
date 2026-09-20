def check_win(board, player):
    win_coords = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for coord in win_coords:
        if board[coord] == board[coord] == board[coord] == player:
            return True
    return False

def check_draw(board):
    return " " not in board