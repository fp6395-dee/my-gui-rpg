import random

def check_win(board, player):
    win_coords = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикали
        (0, 4, 8), (2, 4, 6)              # Диагонали
    ]
    for a, b, c in win_coords:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def check_draw(board):
    return " " not in board

def get_bot_move(board):
    # 1. Если бот (O) может выиграть этим ходом — выигрываем
    for i in range(9):
        if board[i] == " ":
            board_copy = board.copy()
            board_copy[i] = "O"
            if check_win(board_copy, "O"):
                return i
                
    # 2. Если игрок (X) может выиграть следующим ходом — блокируем его
    for i in range(9):
        if board[i] == " ":
            board_copy = board.copy()
            board_copy[i] = "X"
            if check_win(board_copy, "X"):
                return i
                
    # 3. Пытаемся занять центр
    if board[4] == " ":
        return 4
        
    # 4. Выбираем случайную свободную ячейку
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(empty_cells) if empty_cells else None