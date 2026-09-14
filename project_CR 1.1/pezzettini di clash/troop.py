import tkinter as tk
import numpy as np

# crea il canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=625)
canvas.pack()
def createMap():
    global right_tower_alive, left_tower_alive, king_tower_alive
    canvas.create_rectangle(0, 0, 600, 600, fill="blue")
    # Due campi verdi
    canvas.create_rectangle(0, 0, 300, 275, fill="green")
    canvas.create_rectangle(300, 325, 0, 600, fill="green")
    # Due ponti
    canvas.create_rectangle(30, 275, 80, 325, fill="brown")
    canvas.create_rectangle(270, 275, 220, 325, fill="brown")
    # Torri nemiche(con vita)
    king_tower = canvas.create_rectangle(115, 15, 185, 85, fill="red")
    princess_tower = canvas.create_rectangle(30, 100, 80, 150, fill="red")
    right_princess_tower = canvas.create_rectangle(270, 100, 220, 150, fill="red")
    right_tower_alive = True
    left_tower_alive = True
    king_tower_alive = True
    # Le tue torri(senza vita)
    canvas.create_rectangle(115, 515, 185, 585, fill="light blue")
    canvas.create_rectangle(30, 500, 80, 450, fill="light blue")
    canvas.create_rectangle(270, 500, 220, 450, fill="light blue")
    # Posti di evocazione
    canvas.create_oval(50, 335, 60, 325, fill="black")
    canvas.create_oval(250, 335, 240, 325, fill="white")
    canvas.create_oval(50, 440, 60, 450, fill="white")
    canvas.create_oval(250, 440, 240, 450, fill="white")
