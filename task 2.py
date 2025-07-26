import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="black")
root.geometry("400x500")

current_player = "X"
buttons = []
difficulty = "Easy"

def reset_board():
    global current_player
    current_player = "X"
    for btn in buttons:
        btn["text"] = ""
        btn["state"] = "normal"

def exit_game():
    root.destroy()

def set_difficulty(level):
    global difficulty
    difficulty = level
    messagebox.showinfo("Difficulty Set", f"Difficulty set to {level}")

def ai_move():
    empty = [(i, j) for i in range(3) for j in range(3) if buttons[i*3 + j]["text"] == ""]
    if not empty:
        return
    if difficulty == "Easy":
        i, j = random.choice(empty)
    elif difficulty == "Medium":
        i, j = random.choice(empty)
    else:  # Hard
        i, j = best_move()
    buttons[i*3 + j]["text"] = "O"
    buttons[i*3 + j]["state"] = "disabled"
    check_winner()

def click(row, col):
    index = row * 3 + col
    if buttons[index]["text"] == "":
        buttons[index]["text"] = "X"
        buttons[index]["state"] = "disabled"
        check_winner()
        if any(btn["text"] == "" for btn in buttons):
            root.after(500, ai_move)

def check_winner():
    combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in combos:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            messagebox.showinfo("Game Over", f"{buttons[a]['text']} Wins!")
            disable_buttons()
            return
    if all(btn["text"] != "" for btn in buttons):
        messagebox.showinfo("Game Over", "Draw!")
        disable_buttons()

def disable_buttons():
    for btn in buttons:
        btn["state"] = "disabled"

def best_move():
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            if buttons[index]["text"] == "":
                buttons[index]["text"] = "O"
                if is_winner("O"):
                    buttons[index]["text"] = ""
                    return i, j
                buttons[index]["text"] = ""
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            if buttons[index]["text"] == "":
                buttons[index]["text"] = "X"
                if is_winner("X"):
                    buttons[index]["text"] = ""
                    return i, j
                buttons[index]["text"] = ""
    empty = [(i, j) for i in range(3) for j in range(3) if buttons[i*3 + j]["text"] == ""]
    return random.choice(empty)

def is_winner(player):
    lines = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(buttons[i]["text"] == player for i in line) for line in lines)

frame = tk.Frame(root, bg="black")
frame.pack(pady=20)

for i in range(3):
    for j in range(3):
        btn = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                        bg="#333333", fg="white", activebackground="#555555",
                        command=lambda i=i, j=j: click(i, j))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(btn)

diff_frame = tk.Frame(root, bg="black")
diff_frame.pack()

for level in ["Easy", "Medium", "Hard"]:
    tk.Button(diff_frame, text=level, width=10,
              bg="#444444", fg="white", activebackground="#666666",
              command=lambda l=level: set_difficulty(l)).pack(side="left", padx=5)

control_frame = tk.Frame(root, bg="black")
control_frame.pack(pady=20)

tk.Button(control_frame, text="Restart", width=10,
          bg="#444444", fg="white", activebackground="#666666",
          command=reset_board).pack(side="left", padx=10)

tk.Button(control_frame, text="Exit", width=10,
          bg="#444444", fg="white", activebackground="#666666",
          command=exit_game).pack(side="right", padx=10)

root.mainloop()
