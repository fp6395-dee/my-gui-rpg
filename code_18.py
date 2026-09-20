import os
import subprocess

# 1. ОБНОВЛЯЕМ КОД ИГРЫ ДО ВЕРСИИ С ГРАФИЧЕСКИМ ИНТЕРФЕЙСОМ (GUI)
files = {
    "logic.py": """def check_win(board, player):
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
""",
    "main.py": """import tkinter as tk
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
"""
}

print("🛠️ Шаг 1: Заменяю файлы игры на новую GUI-версию...")
for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content.strip())
print("✅ Код успешно обновлен.")

# 2. АВТОМАТИЧЕСКИЙ ВВОД КОМАНД GIT ОДНА ЗА ДРУГОЙ
print("\n🔄 Шаг 2: Начинаю автоматическую отправку обновлений в Git...")

commands = [
    (["git", "add", "."], "Добавление измененных файлов"),
    (["git", "commit", "-m", "Added graphical interface via AI script"], "Создание коммита (сохранения)"),
    (["git", "push"], "Отправка изменений на GitHub")
]

for cmd, description in commands:
    print(f"\nВыполняю: {' '.join(cmd)} ({description})...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        if result.stdout:
            print(result.stdout.strip())
    else:
        print(f"❌ Ошибка при выполнении команды!")
        if result.stderr:
            print(result.stderr.strip())
        print("\nПроцесс остановлен из-за ошибки.")
        exit(1)

print("\n🚀 МАГИЯ ГИТА СРАБОТАЛА! Все команды выполнены успешно!")
print("Зайдите на свой GitHub и обновите страницу — вы увидите, что описание коммита изменилось, а код обновился.")
print("Теперь вы можете запустить и протестировать саму игру через файл main.py!")
input("\nНажмите Enter, чтобы закрыть окно...")
