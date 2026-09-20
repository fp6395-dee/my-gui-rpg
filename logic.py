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

def get_bot_move(board, difficulty="medium"):
    """
    Получает ход бота в зависимости от уровня сложности
    difficulty: "easy", "medium", "hard"
    """
    if difficulty == "easy":
        return get_easy_move(board)
    elif difficulty == "medium":
        return get_medium_move(board)
    elif difficulty == "hard":
        return get_hard_move(board)
    else:
        return get_medium_move(board)

def get_easy_move(board):
    """Легкий уровень: 80% случайных ходов, 20% умных"""
    if random.random() < 0.2:
        return get_medium_move(board)
    
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(empty_cells) if empty_cells else None

def get_medium_move(board):
    """Средний уровень: базовая стратегия"""
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

def get_hard_move(board):
    """Сложный уровень: алгоритм Minimax (непобедимый)"""
    best_score = float('-inf')
    best_move = None
    
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move

def minimax(board, depth, is_maximizing):
    """Алгоритм Minimax для поиска оптимального хода"""
    if check_win(board, "O"):
        return 10 - depth
    if check_win(board, "X"):
        return depth - 10
    if check_draw(board):
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score
