from logic import create_board, print_board, check_win, check_draw

def play_game():
    print("=== КРЕСТИКИ-НОЛИКИ ===")
    print("Инструкция: вводите номера ячеек от 1 до 9")
    print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")
    
    board = create_board()
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            move = int(input(f"Ход игрока [{current_player}]. Выберите ячейку (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Ошибка! Номер должен быть от 1 до 9.")
                continue
            if board[move] != " ":
                print("Эта ячейка уже занята!")
                continue
        except ValueError:
            print("Пожалуйста, введите число.")
            continue
            
        board[move] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Поздравляем! Игрок [{current_player}] победил!")
            break
            
        if check_draw(board):
            print_board(board)
            print("🤝 Ничья!")
            break
            
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
    input("Нажмите Enter, чтобы выйти...")