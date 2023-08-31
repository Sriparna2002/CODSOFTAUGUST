# Import important libraries 
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import random

# Define Questions
question = [
     "1. How many Keywords are there in C Programming language ?",
     "2. Which of the following functions takes A console Input in Python ?",
     "3. Which of the following is the capital of India ?",
     "4. Which of The Following is must to Execute a Python Code ?",
     "5. The Taj Mahal is located in  ?",
     "6. The append Method adds value to the list at the  ?",
     "7. Which of the following is not a costal city of india ?",
     "8. Which of The following is executed in browser(client side) ?",
     "9. Which of the following keyword is used to create a function in Python ?",
     "10. To Declare a Global variable in python we use the keyword ?",
]

# Define options
options = [
     ["23","32","33","43",],
     ["get()","input()","gets()","scan()",],
     ["Mumbai","Delhi","Chennai","Lucknow",],
     ["TURBO C","Py Interpreter","Notepad","IDE",],
     ["Patna","Delhi","Benaras","Agra",],
     ["custom location","end","center","beginning",],
     ["Bengluru","Kochin","Mumbai","vishakhapatnam",],
     ["perl","css","python","java",],
     ["function","void","fun","def",],
     ["all","var","let","global",],
]

# Define correct answers
answers = [1,1,1,1,3,1,0,1,3,3] 


footer_labels = []
def wrong_answer():                                # record wrong answers and print correct answers
    global footer_labels,Score_button
    question_label.destroy()
    option1.destroy()
    option2.destroy()
    option3.destroy()
    option4.destroy()

    for i in range(5):
        if user_answer[i] != answers[indexes[i]]:
            correct_answer = options[indexes[i]][answers[indexes[i]]]
            selected_option = options[indexes[i]][user_answer[i]]
            footer_label = ttk.Label(
                root,
                text=f"Question {i+1}:\n"
                     f"Your Answer: {selected_option}\n"
                     f"Correct Answer: {correct_answer}\n",
                font=font3,
                background=background_color,
                foreground="brown"
            )
            footer_label.pack()
            footer_labels.append(footer_label) 

        Score_button = ttk.Button(  
        root,  
        text = "Score",  
        width = 50,  
        command = lambda: result(score), 
        style="Custom.TButton"
    )  
    Score_button.pack(pady=50)


indexes = []
def gen():                                          # Generate random questions 
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

excellent_label = None
good_label = None
fail_label = None

def restart_quiz():                                # restart quiz 
    global footer_labels, user_answer, radiovar, ques, score, restart_button , excellent_label, good_label, fail_label
    for label in footer_labels:
        label.destroy()
    Score_button.destroy()
    result_label.destroy()
    restart_button.destroy()

    if excellent_label:
        excellent_label.destroy()
    if good_label:
        good_label.destroy()
    if fail_label:
        fail_label.destroy()

    user_answer.clear()
    radiovar.set(-1)
    ques = 1
    score = 0

    gen()
    startquiz()
    
def result(score):                                # Display the score
    global result_label, restart_button, excellent_label, good_label,  fail_label
    for label in footer_labels:
        label.destroy()
    Score_button.destroy()

    result_label = ttk.Label(
    root,
    text="Wow!!!\nYou Have Successfully Completed The Quiz\n"f"Your Score:\n{score}/5",
    font=font,
    background=background_color,
    foreground="Dark blue"
    )
    result_label.pack(pady=50)

    if score >= 4:                                # Display the Feedback condition wise
        excellent_label = ttk.Label(
            root,
            text="Excellent!",
            font=font2,
            background=background_color,
            foreground="green"
        )
        excellent_label.pack(pady=20)
    elif score >=3 and score <= 4:
        good_label = ttk.Label(
            root,
            text="Good effort!",
            font=font2,
            background=background_color,
            foreground="green"
        )
        good_label.pack(pady=20)
    else:
        fail_label= ttk.Label(
            root,
            text="You are fail Batter Luck Next Time!!!",
            font=font2,
            background=background_color,
            foreground="green"
        )   
        fail_label.pack(pady=20)

    restart_button = ttk.Button(                        # restart button
        root,
        text="Restart Quiz",
        width=50,
        command=restart_quiz,
        style="Custom.TButton"
    )
    restart_button.pack(pady=20)

def calculated():                                       # calculate the given answers is correct or not
    global indexes, user_answer, answers
    x = 0
    global score
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 1
        x += 1
    print(score)  
    wrong_answer()
        

user_answer =[]
radiovar = None
ques = 1

def selected():                                     # Select one redio button 
    global radiovar, user_answer
    global question_label, option1, option2, option3, option4
    global ques
    x = radiovar.get()
    radiovar.set(-1)
    user_answer.append(x)
    if ques < 5:  
        question_label.config(text=question[indexes[ques]])
        option1['text'] = options[indexes[ques]][0]
        option2['text'] = options[indexes[ques]][1]
        option3['text'] = options[indexes[ques]][2]
        option4['text'] = options[indexes[ques]][3]
        ques += 1
    else:
        calculated()


def startquiz():                                   # display the questions
    global question_label,option1,option2,option3,option4, radiovar
    question_label = ttk.Label(
        root,
        text=question[indexes[0]],
        font=font3,
        width=500,
        anchor="center",
        wraplength=400,
        background=background_color,
        foreground="brown"
    )
    question_label.pack(pady=(100,30))

    radiovar = tk.IntVar()
    radiovar.set(-1)

    option1 = tk.Radiobutton(                   # diaplay answers 
        root,
        text=options[indexes[0]][0],
        font=font3,
        value=0,
        variable=radiovar,
        background=background_color,
        command=selected
    )
    option1.pack(pady=5)

    option2 = tk.Radiobutton(
        root,
        text=options[indexes[0]][1],
        font=font3,
        value=1,
        variable=radiovar,
        background=background_color,
        command=selected
    )
    option2.pack(pady=5)

    option3 = tk.Radiobutton(
        root,
        text=options[indexes[0]][2],
        font=font3,
        value=2,
        variable=radiovar,
        background=background_color,
        command=selected
    )
    option3.pack(pady=5)

    option4 = tk.Radiobutton(
        root,
        text=options[indexes[0]][3],
        font=font3,
        value=3,
        variable=radiovar,
        background=background_color,
        command=selected
    )
    option4.pack(pady=5)

def start():                                  # start the question window
    image_label.destroy()
    text_label.destroy()
    Des_label.destroy()
    Rules_label.destroy()
    Start_button.destroy()
    gen()
    startquiz()

root = tk.Tk()                                  # make tkinter window

# define fonts
font_name = "Lobster"
font_size = 30
font = (font_name, font_size)

font2_name = "Consolas"
font2_size = 25
font2_style = "bold"
font2 = (font2_name, font2_size, font2_style)

font3_name = "Consolas"
font3_size = 12
font3_style = "bold"
font3 = (font3_name, font3_size,font3_style)

# Define background colous 
background_color = "Pink"
header_background = "light blue"
label_foreground = "Dark blue"
button_background = "#0074E4"
button_foreground = "#FFFFFF"

# set tkinter window
root.geometry("800x600")
root.title("Quiz Game")
root.resizable(0, 0)
root.configure(bg="Pink")

# set image
img1 = "1.png"
image = tk.PhotoImage(file=img1)

width, height = 150, 100
resized_image = image.subsample(int(image.width() / width), int(image.height() / height))

image_label = ttk.Label(
    root,
    image=resized_image,
    background=background_color,
)
image_label.pack(pady=(40, 0))

text_label = ttk.Label(
    root,
    text="Quiz Game",
    font=font,
    background=background_color,
    foreground="Red"
)
text_label.pack(padx=20, pady=5)

Des_label = ttk.Label(   
    root,  
    text = " Read The Rules Carefully And\nClick Start Once You Have Ready",  
    font = font3,  
    background = background_color,  
    foreground = label_foreground   
)  
Des_label.pack(padx=50,pady=20)

Rules_label = ttk.Label(   
    root,  
    text = "This Quiz Game Contains 5 Questions\nSelect Any One Option Given There\nAnd That Will Be Your Final Answer ",  
    font = font3,  
    background = background_color,  
    foreground = "Dark Green"   
)  
Rules_label.pack(padx=50,pady=20)

custom_style = ttk.Style()
custom_style.configure("Custom.TButton", background="Dark Blue", foreground="Black")

Start_button = ttk.Button(  
        root,  
        text = "Start",  
        width = 50,  
        command = start,
        style="Custom.TButton"
)  

Start_button.pack(padx=50)

root.mainloop()
