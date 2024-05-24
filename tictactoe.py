from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Initialize the main window
root = Tk()
root.title("Tic Tac Toe")

# Create a frame with padding inside the main window
frm = ttk.Frame(root, padding=20)
frm.grid()

# Initialize game states and turn
xstate = [0] * 9
zstate = [0] * 9
turn = 1

def checkplace(xstate, zstate, p):
    if xstate[p] == 1:
        return "X"
    elif zstate[p] == 1:
        return "O"
    else:
        return ""

def checkwin(state):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for win in wins:
        if state[win[0]] + state[win[1]] + state[win[2]] == 3:
            return True
    return False

def game_end(winner):
    if winner == "X":
        messagebox.showinfo("Winner!", "X Wins!")
    elif winner == "O":
        messagebox.showinfo("Winner!", "O Wins!")
    else:
        messagebox.showinfo("Draw", "Game Draw!")
    root.quit()

def checkdraw(xstate, zstate):
    return sum(xstate) + sum(zstate) == 9

def fillboard(p):
    global turn

    if xstate[p] == 0 and zstate[p] == 0:
        if turn == 1:
            zstate[p] = 1
        else:
            xstate[p] = 1
        
        if checkwin(xstate):
            game_end("X")
        elif checkwin(zstate):
            game_end("O")
        elif checkdraw(xstate, zstate):
            game_end("Draw")
        
        turn = 1 - turn
        update_board()

def update_board():
    for i in range(9):
        buttons[i].config(text=checkplace(xstate, zstate, i))
    turn_label.config(text=f"{'X' if turn == 0 else 'O'}'s turn")

# Create buttons for the tic-tac-toe grid
buttons = [ttk.Button(frm, text=checkplace(xstate, zstate, i), command=lambda i=i: fillboard(i)) for i in range(9)]

# Layout the grid
for i, button in enumerate(buttons):
    button.grid(row=i//3 + 1, column=i%3, padx=5, pady=5, ipadx=10, ipady=10)

# Add a label to indicate the current turn
turn_label = ttk.Label(frm, text=f"{'X' if turn == 0 else 'O'}'s turn", font=("Helvetica", 20))
turn_label.grid(column=0, row=0, columnspan=3, pady=10)

# Start the Tkinter event loop
update_board()
root.mainloop()
