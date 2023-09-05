import tkinter as tk
from tkinter import messagebox

expression = ""

def update_input(val):
    global expression
    expression += val
    data.set(expression)

def clear_input():
    global expression
    expression = ""
    data.set("")

def evaluate_expression():
    global expression
    try:
        result = eval(expression)
        data.set(result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression: {str(e)}")
        clear_input()

root = tk.Tk()
root.title("Calculator")
root.geometry("380x450")
root.resizable(0, 0)


data = tk.StringVar()
data.set("")

input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

input_entry = tk.Entry(
    input_frame,
    textvariable=data, 
    font=("Arial", 18), 
    justify="right"
    )

input_entry.grid(
    row=0, 
    column=0, 
    columnspan=4, 
    padx=10, 
    pady=10, 
    ipadx=10, 
    ipady=10
    )

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0
for button_text in buttons:
    tk.Button(
        button_frame,
        text=button_text,
        font=("Arial", 18),
        width=5,
        height=2,
        background="orange",
        foreground="black",
        command=lambda text=button_text: update_input(text) if text not in ['C', '='] else evaluate_expression() if text == '=' else clear_input()
    ).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
