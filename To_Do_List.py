import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

tasks = []

def load_tasks():
    try:
        with open("record.txt", "r") as f:
            tasks.extend(f.read().splitlines())
    except FileNotFoundError:
        pass 

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo("Error", "Field is Empty.")
    else:
        tasks.append(task_string)

        with open("record.txt", "a") as f:
            f.write(task_string + "\n")
        
        list_update()  

        task_field.delete(0, 'end')


def delete_task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())  
        if the_value in tasks:     
            tasks.remove(the_value)
            update_file()  
            list_update()     
    except:  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')   
        list_update()
        task_field.delete(0, 'end')

def update_file():
    with open("record.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def delete_all_tasks():
    global tasks
    tasks = [] 
    list_update()  

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    root.destroy()

root = tk.Tk()

font_name = "Lobster"
font_size = 30
font = (font_name, font_size)

font2_name = "Consolas"
font2_size = 11
font2_style = "bold"
font2 = (font2_name, font2_size,font2_style)

font3_name = "Consolas"
font3_size = 12
font3 = (font3_name, font3_size)

background_color = "#ECECEC"
header_background = "#4E6E5D"
header_foreground = "#FFFFFF"
label_foreground = "#000000"
button_background = "#0074E4"  
button_foreground = "#FFFFFF"  
listbox_background = "#FFFFFF"
listbox_foreground = "#000000"

root.geometry("500x450+750+250")
root.title("To Do List")
root.resizable(0,0)
root.configure(bg="#FAEBD7")

header_frame = tk.Frame(root, bg= header_background)
functions_frame = tk.Frame(root, bg = "#FAEBD7")  
listbox_frame = tk.Frame(root,bg="#FAEBD7")

header_frame.pack(fill="both")
functions_frame.pack(side = "left",expand = True, fill = "both")  
listbox_frame.pack(side = "right", expand = True, fill = "both")

header_label = ttk.Label(
    header_frame,
    text="To Do List",
    font=font,
    background=header_background,
    foreground=header_foreground
)

header_label.pack(padx = 20, pady = 20)

task_label = ttk.Label(   
    functions_frame,  
    text = "Enter the Task:",  
    font = font2,  
    background = background_color,  
    foreground = label_foreground   
    )  

task_label.place(x = 30, y = 40)   

task_field = ttk.Entry(  
    functions_frame,  
    font = font3,
    width = 18,  
    background = "#FFF8DC",  
    foreground = "#A52A2A"  
    )  
task_field.place(x = 30, y = 80)  

add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task,
        style="TButton"
    )  
del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task ,
        style="TButton" 
    )  
del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks,
        style="TButton"  
    )  
exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close,
        style="TButton"  
    )  

add_button.place(x = 30, y = 120)  
del_button.place(x = 30, y = 160)  
del_all_button.place(x = 30, y = 200)  
exit_button.place(x = 30, y = 240)  

task_listbox = tk.Listbox(
    listbox_frame,
    width=26,
    height=13,
    selectmode='SINGLE',
    background=listbox_background,
    foreground=listbox_foreground,
    selectbackground=button_background,
    selectforeground=button_foreground
) 
s = ttk.Style()
s.configure("Custom.TButton", background=button_background, foreground=button_foreground)

task_listbox.place(x = 10, y = 70)  

root.mainloop()

