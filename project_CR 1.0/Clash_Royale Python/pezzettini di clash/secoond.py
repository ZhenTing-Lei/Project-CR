#commento dal 31/05/2024: questa è la seconda versione di project CR(risale al febbraio del 2024)

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

global arcieri # dichiaro la variabile globale
global moving # dichiaro una variabile booleana che indica se il cerchio si sta muovendo o no

def spawn_circle(event):
    global arcieri # uso la variabile globale
    global moving # uso la variabile globale
    if event.keysym == "1":
        arcieri = canvas.create_oval(50, 50, 100, 100, fill='red') # creo il cerchio
        moving = True # imposto la variabile a True
        move_circle() # chiamo la funzione che muove il cerchio

def move_circle():
    global arcieri # uso la variabile globale
    global moving # uso la variabile globale
    if moving: # se la variabile è True
        canvas.move(arcieri, 0, 10) # sposto il cerchio di 10 pixel verso basso
        x1, y1, x2, y2 = canvas.coords(arcieri) # ottengo le coordinate del cerchio
        if x2 > 400: # se il cerchio ha superato il bordo destro del canvas
            canvas.move(0, 0) # si ferma
            moving = False # imposto la variabile a False
        else: # altrimenti
            root.after(100, move_circle) # richiamo la funzione dopo 100 millisecondi

root.bind('<KeyPress>', spawn_circle) # assegno la funzione all'evento
root.mainloop()