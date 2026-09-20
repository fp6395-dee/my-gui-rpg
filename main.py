import tkinter as tk
from tkinter import messagebox, ttk
from logic import check_win, check_draw, get_bot_move
from settings import GameSettings

class TicTacToeBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики")
        self.root.geometry("450x550")
        self.root.configure(bg="#1a1a2e")
        
        # Загрузка настроек
        self.settings = GameSettings()
        self.difficulty = tk.StringVar(value="medium")
        
        self.board = [" " for _ in range(9)]
        self.buttons = []
        self.game_over = False
        self.history = []  # История ходов для undo
        
        self.setup_ui()
    
    def setup_ui(self):
        # Верхняя панель с выбором сложности
        top_frame = tk.Frame(self.root, bg="#1a1a2e")
        top_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(top_frame, text="Сложность:", bg="#1a1a2e", fg="#ecf0f1", 
                font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        
        difficulty_menu = ttk.Combobox(top_frame, textvariable=self.difficulty,
                                      values=["easy", "medium", "hard"],
                                      state="readonly", width=10)
        difficulty_menu.pack(side=tk.LEFT, padx=5)
        difficulty_menu.bind("<<ComboboxSelected>>", lambda e: self.reset_game())
        
        # Статус игры
        self.lbl_status = tk.Label(self.root, text="Ваш ход (❌)", 
                                  bg="#1a1a2e", fg="#ecf0f1", 
                                  font=("Arial", 14, "bold"))
        self.lbl_status.pack(pady=10)
        
        # Игровое поле
        frame = tk.Frame(self.root, bg="#1a1a2e")
        frame.pack(pady=10)
        
        for i in range(9):
            btn = tk.Button(frame, text="", font=("Arial", 24, "bold"), 
                          width=5, height=2, bg="#16213e", fg="#ecf0f1",
                          activebackground="#0f3460", relief=tk.RAISED, bd=3,
                          command=lambda idx=i: self.player_move(idx))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_leave(b))
            self.buttons.append(btn)
        
        # Панель управления
        control_frame = tk.Frame(self.root, bg="#1a1a2e")
        control_frame.pack(pady=10)
        
        self.btn_undo = tk.Button(control_frame, text="↩ Отменить", 
                                 font=("Arial", 11), bg="#0f3460", fg="#ecf0f1",
                                 command=self.undo_move, state=tk.DISABLED)
        self.btn_undo.pack(side=tk.LEFT, padx=5)
        
        btn_new = tk.Button(control_frame, text="🔄 Новая игра", 
                           font=("Arial", 11), bg="#e94560", fg="#fff",
                           command=self.reset_game)
        btn_new.pack(side=tk.LEFT, padx=5)
    
    def on_hover(self, btn):
        if btn['state'] == 'normal' and btn['text'] == '':
            btn.configure(bg="#0f3460")
    
    def on_leave(self, btn):
        if btn['state'] == 'normal':
            btn.configure(bg="#16213e")
    
    def player_move(self, idx):
        if self.board[idx] != " " or self.game_over:
            return
        
        # Сохраняем состояние для undo
        self.history.append((idx, "X"))
        
        self.make_move(idx, "X", "#e74c3c", "❌")
        
        if self.check_game_status("X", "Вы победили! 🎉"):
            return
        
        self.lbl_status.configure(text="Компьютер думает... 🤔")
        self.root.after(500, self.bot_turn)
    
    def bot_turn(self):
        if self.game_over:
            return
        
        difficulty = self.difficulty.get()
        bot_idx = get_bot_move(self.board, difficulty)
        
        if bot_idx is not None:
            self.history.append((bot_idx, "O"))
            self.make_move(bot_idx, "O", "#f1c40f", "⭕")
            
            if self.check_game_status("O", "Компьютер победил! 🤖"):
                return
            
            self.lbl_status.configure(text="Ваш ход (❌)")
            self.update_undo_button()
    
    def make_move(self, idx, player, color, symbol):
        self.board[idx] = player
        self.buttons[idx].configure(text=symbol, fg=color, state="disabled")
    
    def check_game_status(self, player, win_message):
        if check_win(self.board, player):
            self.game_over = True
            # Подсветка выигрышной линии
            self.highlight_winning_line(player)
            messagebox.showinfo("Конец игры", win_message)
            self.reset_game()
            return True
        
        if check_draw(self.board):
            self.game_over = True
            messagebox.showinfo("Конец игры", "🤝 Ничья!")
            self.reset_game()
            return True
        
        return False
    
    def highlight_winning_line(self, player):
        win_coords = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in win_coords:
            if self.board[a] == self.board[b] == self.board[c] == player:
                for idx in [a, b, c]:
                    self.buttons[idx].configure(bg="#2ecc71")
                break
    
    def undo_move(self):
        if len(self.history) < 2 or self.game_over:
            return
        
        # Отменяем ход бота и игрока
        for _ in range(2):
            if self.history:
                idx, player = self.history.pop()
                self.board[idx] = " "
                self.buttons[idx].configure(text="", state="normal", bg="#16213e")
        
        self.lbl_status.configure(text="Ваш ход (❌)")
        self.update_undo_button()
    
    def update_undo_button(self):
        if len(self.history) >= 2 and not self.game_over:
            self.btn_undo.configure(state=tk.NORMAL)
        else:
            self.btn_undo.configure(state=tk.DISABLED)
    
    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.game_over = False
        self.history = []
        self.lbl_status.configure(text="Ваш ход (❌)")
        
        for btn in self.buttons:
            btn.configure(text="", state="normal", bg="#16213e")
        
        self.update_undo_button()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeBotGUI(root)
    root.mainloop()
