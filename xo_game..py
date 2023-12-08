import tkinter as tk
from tkinter import ttk
import random

#ask the user to chose between O OR X 


user_choice = input("Choose X or O: ")
computer_choice = "O" if user_choice == "X" else "X"

def get_user_choice():
    while True:
        user_choice = input("Choose X or O: ").upper()
        if user_choice in ["X", "O"]:
            return user_choice
        else:
            print("Invalid choice. Please choose either X or O.")

user_choice = get_user_choice()
    
user_score=0
computer_score = 0
table = [""] * 9

#The possible ways to win the game 

def check_winner():
    winning_prob = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns 
        [0, 4, 8], [2, 4, 6]              # Diagonals 
    ] 

    for i in winning_prob:
        if table[i[0]] == table[i[1]] == table[i[2]] and table[i[0]] != "":
            return table[i[0]]

    if "" not in table:
       
        return "Tie"
    

    return None

def update_board(index):
    if table[index] == "":
        table[index] = user_choice
        update_buttons()
        winner = check_winner()
        if winner:
            show_winner(winner)
        else:
            computer_move()

#make the computer chose random place to play 

def computer_move():
    empty_cells = [i for i, value in enumerate(table) if value == ""]
    if empty_cells:
        computer_choice_index = random.choice(empty_cells)
        table[computer_choice_index] = computer_choice
        update_buttons()
        winner = check_winner()
        if winner:
            show_winner(winner)

def update_buttons():
    for i, value in enumerate(table):
        buttons[i].config(text=value)

#Show the score of game 

def show_winner(winner):
    score_label.config(text=f"You: {user_choice} -- Computer: {computer_choice} - {winner}")
    global user_score, computer_score
    if winner == user_choice:
        user_score += 1
    elif winner == computer_choice:
        computer_score += 1
    else : 
        return 0     
    score_label.config(text=f"You: {user_score} -- Computer: {computer_score} - {winner}")
    disable_buttons()


def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

#restart the game 

def restart_game():
    global table
    table = [""] * 9
    update_buttons()
    score_label.config(text=f"You: {user_choice} -- Computer: {computer_choice}")
    for button in buttons:
        button.config(state=tk.NORMAL)

# GUI
window = tk.Tk()
window.title("X, O Game")
window.geometry('600x600')

score_label = tk.Label(window, text=f"You: {user_choice} -- Computer: {computer_choice}")
score_label.place(relx=.66, rely=.66, anchor='ne')

buttons = []
for i in range(3):
    for j in range(3):
        index = i * 3 + j
        button = tk.Button(window, text="", font=("Helvetica", 24),
                           width=4, height=2, command=lambda index=index: update_board(index))
        button.grid(row=i, column=j)
        buttons.append(button)

restart_btn = ttk.Button(window, text='Restart', style='TButton', command=restart_game)
restart_btn.grid(column=3, row=1, sticky="ne", padx=5, pady=5)

window.mainloop() 
