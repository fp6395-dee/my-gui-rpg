import tkinter as tk
from tkinter import messagebox
from logic import check_win, check_draw, get_bot_move

class TicTacToeBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра против Компьютера"))
        self.root.geometry("320x380")
        self.root.configure(bg="#2c3e50")
        
        self.board = [" " for _ in range(9)]
        self.buttons = []
        self.game_over = False
        
        self.setup_ui()
        
    def setup_ui(self):
        self.lbl_status = tk.Label(self.root, text="Ваш ход (Крестики)", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14, "bold"))
        self.lbl_status.pack(pady=10)
        
        frame = tk.Frame(self.root, bg="#2c3e50")
        frame.pack()
        
        for i in range(9):
            btn = tk.Button(frame, text="", font=("Arial", 20, "bold"), width=5, height=2,
                            bg="#34495e", fg="#ecf0f1", activebackground="#16a085",
                            command=lambda idx=i: self.player_move(idx))
            btn.grid(row=i//3, column=i%3, padx=3, pady=3)
            self.buttons.append(btn)
            
    def player_move(self, idx):
        if self.board[idx] != " " or self.game_over:
            return
        self.make_move(idx, "X", "#e74c3c")
        if self.check_game_status("X", "Вы победили! 🎉"):
            return
        self.lbl_status.configure(text="Компьютер думает...")
        self.root.after(400, self.bot_turn)
        
    def bot_turn(self):
        if self.game_over:
            return
        bot_idx = get_bot_move(self.board)
        if bot_idx is not None:
            self.make_move(bot_idx, "O", "#f1c40f")
            if self.check_game_status("O", "Компьютер победил! 🤖"):
                return
        self.lbl_status.configure(text="Ваш ход (Крестики)")

    def make_move(self, idx, player, color):
        self.board[idx] = player
        self.buttons[idx].configure(text=player, fg=color, state="disabled")
        
    def check_game_status(self, player, win_message):
        if check_win(self.board, player):
            self.game_over = True
            messagebox.showinfo("Конец игры", win_message)
            self.reset_game()
            return True
        if check_draw(self.board):
            self.game_over = True
            messagebox.showinfo("Конец игры", "🤝 Ничья!")
            self.reset_game()
            return True
        return False
        
    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.game_over = False
        self.lbl_status.configure(text="Ваш ход (Крестики)")
        for btn in self.buttons:
            btn.configure(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeBotGUI(root)
    root.mainloop()
