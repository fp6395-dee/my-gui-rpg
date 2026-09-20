import tkinter as tk
from tkinter import messagebox
from logic import check_win, check_draw

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики GUI")
        self.root.geometry("320x380")
        self.root.configure(bg="#2c3e50")
        
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.buttons = []
        
        self.setup_ui()
        
    def setup_ui(self):
        self.lbl_status = tk.Label(self.root, text="Ход игрока [X]", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14, "bold"))
        self.lbl_status.pack(pady=10)
        
        frame = tk.Frame(self.root, bg="#2c3e50")
        frame.pack()
        
        for i in range(9):
            btn = tk.Button(frame, text="", font=("Arial", 20, "bold"), width=5, height=2,
                            bg="#34495e", fg="#ecf0f1", activebackground="#16a085",
                            command=lambda idx=i: self.make_move(idx))
            btn.grid(row=i//3, column=i%3, padx=3, pady=3)
            self.buttons.append(btn)
            
    def make_move(self, idx):
        if self.board[idx] != " ":
            return
            
        self.board[idx] = self.current_player
        color = "#e74c3c" if self.current_player == "X" else "#f1c40f"
        self.buttons[idx].configure(text=self.current_player, fg=color, state="disabled")
        
        if check_win(self.board, self.current_player):
            messagebox.showinfo("Победа!", f"Игрок [{self.current_player}] победил!")
            self.reset_game()
            return
            
        if check_draw(self.board):
            messagebox.showinfo("Ничья", "🤝 Сыграно вничью!")
            self.reset_game()
            return
            
        self.current_player = "O" if self.current_player == "X" else "X"
        self.lbl_status.configure(text=f"Ход игрока [{self.current_player}]")
        
    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.lbl_status.configure(text="Ход игрока [X]")
        for btn in self.buttons:
            btn.configure(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()