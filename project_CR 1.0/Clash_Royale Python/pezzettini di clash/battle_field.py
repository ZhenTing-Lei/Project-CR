# Il lavoro in costruzione:

import tkinter as tk
import time
import os

# Il campo di clash, posizione di evocazione e il knight
# +
#game intro
#crea il canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=600)
canvas.pack()

# Crea il fiume(blu), due ponti(marrone) e sei torri(i quadrati)
canvas.create_rectangle(0, 0, 600, 600, fill="blue")
canvas.create_rectangle(0, 0, 300, 275, fill="green")
canvas.create_rectangle(300, 325, 0, 600, fill="green")
canvas.create_rectangle(30, 275, 80, 325, fill="brown")
canvas.create_rectangle(270, 275, 220, 325, fill="brown")
canvas.create_rectangle(115, 15, 185, 85, fill="red")
canvas.create_rectangle(30, 100, 80, 150, fill="red")
canvas.create_rectangle(270, 100, 220, 150, fill="red")
canvas.create_rectangle(115, 515, 185, 585, fill="light blue")
canvas.create_rectangle(30, 500, 80, 450, fill="light blue")
canvas.create_rectangle(270, 500, 220, 450, fill="light blue")
canvas.create_oval(50, 440, 60, 450, fill="white")
canvas.create_oval(250, 440, 240, 450, fill="white")
canvas.create_oval(50, 335, 60, 325, fill="white")
canvas.create_oval(250, 335, 240, 325, fill="white")

#timer di 3 minuti
def update_timer():
    elapsed_time = time.time() - start_time
    remaining_time = max(0, 180 - elapsed_time)  # Assicura che il tempo rimanente sia non negativo

    # Formatta il tempo rimanente come MM:SS
    minutes, seconds = divmod(int(remaining_time), 60)
    current_time = f"{minutes:02}:{seconds:02}"

    canvas.delete("timer")  # Cancella il testo precedente
    canvas.create_text(280, 20, text=current_time, anchor="ne", font=("Arial", 12), fill="black", tags="timer")
    root.after(1000, update_timer)  # Aggiorna ogni secondo

#cordinate del posto di evocazione
cordinate_1 = [40, 260] 
cordinate_2 = [430, 430]
cordinate_3 = [70, 230]
cordinate_4 = [460, 460]

def spawn_circle(event):
    global knight # uso la variabile globale
    global moving # uso la variabile globale
    if event.keysym =="a":
        x = int(0)
        canvas.create_oval(50, 440, 60, 450, fill="black")
        canvas.create_oval(250, 440, 240, 450, fill="white")
        canvas.create_oval(50, 335, 60, 325, fill="white")
        canvas.create_oval(250, 335, 240, 325, fill="white")
    elif event.keysym =="b":
        x = int(1)
        canvas.create_oval(50, 440, 60, 450, fill="white")
        canvas.create_oval(250, 440, 240, 450, fill="black")
        canvas.create_oval(50, 335, 60, 325, fill="white")
        canvas.create_oval(250, 335, 240, 325, fill="white")

    elif event.keysym == "1":
        knight = canvas.create_oval(cordinate_1[0], cordinate_2[0], cordinate_3[0], cordinate_4[0], fill='grey') # creo il cerchio
        moving = True # imposto la variabile a True
        move_circle() # chiamo la funzione che muove il cerchio
def move_circle():
    global knight
    global moving
    if moving: # se la variabile è True
        time.sleep(1)
        canvas.move(knight, 0, -10)
        x1, y1, x2, y2 = canvas.coords(knight) # ottengo le coordinate del cerchio
        if y2 > 600: # se il cerchio arriva alla torre
            moving = False # imposto la variabile a False   
        else: # altrimenti
            root.after(100, move_circle) # richiamo la funzione dopo 100 millisecondi
root.bind('<KeyPress>', spawn_circle) # assegno la funzione all'evento

# Inizia il timer
start_time = time.time()

# Crea un display del cronometro nella parte in alto a destra
update_timer()
root.bind('<KeyPress>', spawn_circle) # assegno la funzione all'evento
root.mainloop()