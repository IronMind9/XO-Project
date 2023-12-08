import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.player = "X"
        self.computer = "O"
        self.score_player = 0
        self.score_computer = 0

        self.buttons = [[None, None, None] for _ in range(3)]

        self.create_gui()

    def create_gui(self):
        self.score_label = tk.Label(self.root, text="Player: 0   Computer: 0", font=("Helvetica", 12))
        self.score_label.grid(row=0, column=0, columnspan=3)

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=3, command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i + 1, column=j)
                self.buttons[i][j] = button

        restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        restart_button.grid(row=4, column=0, columnspan=3)

    def button_click(self, row, col):
        if not self.buttons[row][col]["text"]:
            self.buttons[row][col]["text"] = self.player
            if self.check_winner(self.player):
                self.score_player += 1
                self.show_winner("Player")
                self.update_score_label()
                self.restart_game()
            elif self.is_board_full():
                self.show_winner("Tie")
                self.restart_game()
            else:
                self.computer_move()

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if not self.buttons[i][j]["text"]]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.buttons[row][col]["text"] = self.computer
            if self.check_winner(self.computer):
                self.score_computer += 1
                self.show_winner("Computer")
                self.update_score_label()
                self.restart_game()
            elif self.is_board_full():
                self.show_winner("Tie")
                self.restart_game()

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if all(self.buttons[i][j]["text"] == player for j in range(3)) or \
               all(self.buttons[j][i]["text"] == player for j in range(3)):
                return True
        if all(self.buttons[i][i]["text"] == player for i in range(3)) or \
           all(self.buttons[i][2 - i]["text"] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.buttons[i][j]["text"] for i in range(3) for j in range(3))

    def show_winner(self, winner):
        if winner == "Tie":
            messagebox.showinfo("Game Over", "It's a Tie!")
        else:
            messagebox.showinfo("Game Over", f"{winner} wins!")

    def restart_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.player = "X"
        self.computer = "O"
        self.update_score_label()
        if random.choice([True, False]):
            self.computer_move()

    def update_score_label(self):
        self.score_label["text"] = f"Player: {self.score_player}   Computer: {self.score_computer}"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
