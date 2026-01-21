#Commento dal 31/05/2024: prima versione di project CR(questo è un lavoro risalente a gennaio del 2024)

import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

def move(score):
    if score.char == "1":
        print("hai piazzato un gigante")
        gigante = canvas.create_oval(50, 50, 100, 0, fill="dark orange")
    elif score.char == "2":
        print("hai piazzato una principessa")
        principessa = canvas.create_oval( 50, 50, 100, 100, fill="red")
    elif score.char == "3":
        print("hai piazzato gli arcieri")
        arcieri = canvas.create_oval(50, 50, 225, 225, fill="blue")
    elif score.char == "4":
        print("hai piazzato un bowler")
        bowler = canvas.create_oval(50, 50, 225, 225, fill="violet")

def update(score, limit):
    score += 1
    if score <= limit:
        ScoreL.configure(text=score)
        canvas.after(1000, update, score, limit)
    else: score = score+0

ScoreL = tk.Label(root, text=0)
ScoreL.pack()

limit = 10
score = 0

canvas.after(1000, update, score, limit)



canvas.bind("<Key>", move)
canvas.focus_set()

root.mainloop()