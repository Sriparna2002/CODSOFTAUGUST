import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def Generate():
    password_length = int(task_field.get())
    password_strength = var.get()

    if password_length <= 0:
        messagebox.showerror("Error", "Password length should be greater than 0.")
        return

    if password_strength == "Simple":
        characters = string.ascii_letters + string.digits
    elif password_strength == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()

    password = ''.join(random.choice(characters) for i in range(password_length))
    pass_word_label.delete(0, tk.END)
    pass_word_label.insert(0, password)

def copy():
    generated_password = pass_word_label.get()
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    root.update_idletasks()


root = tk.Tk()
root.title("Password Generator")
root.geometry("325x400")
root.resizable(0, 0)
root.configure(bg="#FAEBD7")

header_frame = tk.Frame(root, bg="#FAEBD7")
header_frame.pack(fill="both")

header_label = tk.Label(
    header_frame,
    text="Password Generator",
    font=("Lobster", 30),
    background="#FAEBD7",
    foreground="Brown"
)
header_label.pack()

radio_frame = tk.Frame(root, bg="#FAEBD7")
radio_frame.pack()

var = tk.StringVar()
var.set(-1)

radio_button1 = tk.Radiobutton(
    radio_frame,
    text="Simple",
    variable=var,
    value="Simple",
    font=("Helvetica", 15, "bold"),
    foreground="Black",
    background="#FAEBD7",
    selectcolor="Orange",
)
radio_button2 = tk.Radiobutton(
    radio_frame,
    text="Medium",
    variable=var,
    value="Medium",
    font=("Helvetica", 15, "bold"),
    foreground="Black",
    background="#FAEBD7",
    selectcolor="Orange",
)
radio_button3 = tk.Radiobutton(
    radio_frame,
    text="Strong",
    variable=var,
    value="Strong",
    font=("Helvetica", 15, "bold"),
    foreground="Black",
    background="#FAEBD7",
    selectcolor="Orange",
)
radio_button1.pack(side=tk.LEFT)
radio_button2.pack(side=tk.LEFT)
radio_button3.pack(side=tk.LEFT)

entry_frame = tk.Frame(root, bg="#FAEBD7")
entry_frame.pack(side="left", expand=True, fill="both")

task_label = tk.Label(
    entry_frame,
    text="Enter the Length:",
    font=("Helvetica", 15, "bold"),
    foreground="Black",
    background="#FAEBD7",
)
task_label.grid(row=0, column=0, padx=10, pady=10)

task_field = tk.Entry(
    entry_frame,
    font=("Helvetica", 15, "bold"),
    foreground="Black",
    background="white",
    width=5,
    relief="groove"
)
task_field.grid(row=0, column=1, padx=10, pady=10)

custom_style = ttk.Style()
custom_style.configure("Custom.TButton", background="brown", foreground="black")

generate_button = ttk.Button(
    entry_frame,
    text="Generate",
    style="Custom.TButton",
    command=Generate,
)
generate_button.grid(row=1, column=0, padx=10, pady=(10, 20))

generate_button2 = ttk.Button(
    entry_frame,
    text="Copy",
    style="Custom.TButton",
    command=copy,
)
generate_button2.grid(row=1, column=1, padx=10, pady=(10, 20))

pass_word_label = tk.Entry(
    entry_frame,
    font=("Helvetica", 15, "bold"),
    foreground="Black",
    background="white",
    width=20,
    relief="groove"
)
pass_word_label.grid(row=2, column=0, columnspan=2, padx=50, pady=10)

root.mainloop()
