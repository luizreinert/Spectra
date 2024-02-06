import tkinter as tk

def do_something(row, col):
    buttons[row][col].config(bg="blue")
    # change direct connected buttons (left, right, up, down)
    for dir in (-1, +1):
        if 0 <= row+dir < len(buttons):
            buttons[row+dir][col].config(bg="blue")
        if 0 <= col+dir < len(buttons[row]):
            buttons[row][col+dir].config(bg="blue")

window = tk.Tk()
frame = tk.Frame(window)
frame.pack()

ROWS = 10
COLS = 10

buttons = [[None]*COLS for _ in range(ROWS)] # for storing references of buttons
for row in range(ROWS):
    for col in range(COLS):
        buttons[row][col] = tk.Button(frame, width=10, height=5, bg="orange", command=lambda r=row,c=col: do_something(r,c))
        buttons[row][col].grid(row=row, column=col, sticky="nsew")

window.mainloop()