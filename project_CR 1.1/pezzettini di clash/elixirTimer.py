# imports e robe per startare il gioco
import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=670)
canvas.pack()

# elisirrrr e alcune righe nel canvas
elixir = 6
elixirText = canvas.create_text(150, 660, text="6", font=("Helvetica"))
canvas.create_line(0, 650, 300, 650)
elixirUI = canvas.create_rectangle(0, 600, 30*elixir, 650, fill="red")
for line in range(0, 10):
    canvas.create_line(30*line, 600, 30*line, 650, fill="black")
# variabili per timer
remTimeMin = 3
remTimeSec = 0
canvas.create_text(235, 50, text=str("time    :"), fill="black", font=("arial", 12))
minText = canvas.create_text(250, 50, text=str(remTimeMin), fill="black", font=("arial", 12))
secText = canvas.create_text(270, 50, text=str(remTimeSec), fill="black", font=("arial", 12))

# credo che usare una classe per tutto non sia fattibile o efficiente, ma teniamo la cosa così...
class ElixirManager:
    def __init__(self, elixir):
        self.elixir = elixir
    
    def add_elixir(self):
        if self.elixir < 10:
            self.elixir += 1

#update elixir, una per mostrare l'elixir in immagine, una per mostrare in numeri
elixir_manager = ElixirManager(elixir)
def elixirShowUp():
    global elixirUI
    canvas.delete(elixirUI)
    elixirUI = canvas.create_rectangle(0, 600, 30*elixir_manager.elixir, 650, fill="purple")
    for line in range(10):
        canvas.create_line(30*line, 600, 30*line, 650, fill="black")
    root.after(100, elixirShowUp)
def update_elixir():
    global elixirText
    elixir_manager.add_elixir()
    canvas.delete(elixirText)
    elixirText = canvas.create_text(150, 660, text=str(elixir_manager.elixir), font=("Helvetica"))
    root.after(2800, update_elixir)

def timer():
    global remTimeMin, remTimeSec, minText, secText
    if remTimeSec<1 and remTimeMin>0:
        remTimeMin -= 1
        remTimeSec = 60
        canvas.delete(minText)
        canvas.delete(secText)
        minText = canvas.create_text(250, 50, text=str(remTimeMin), fill="black", font=("arial", 12))
        secText = canvas.create_text(270, 50, text=str(remTimeSec), fill="black", font=("arial", 12))
    else:
        remTimeSec -= 1
        canvas.delete(secText)
        secText = canvas.create_text(270, 50, text=str(remTimeSec), fill="black", font=("arial", 12))
    root.after(1000, timer)

timer()
elixirShowUp()
update_elixir()
root.mainloop()