import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=625)
canvas.pack()

def update_elixir():
    global elixir
    global elixir_text
    canvas.delete(elixir_text)
    elixir += 1
    elixir_text = canvas.create_text(245, 100, text=str(elixir), fill="black", font=("Arial", 12))
    root.after(2800, update_elixir)
elixir = 0
elixir_text = canvas.create_text(245, 100, text=str(elixir), fill="black", font=("Arial", 12))

def spending_elixir(event):
    global elixir_text
    global elixir
    if event.keysym=="a":
        canvas.delete(elixir_text)
        elixir=elixir-1
        elixir_text = canvas.create_text(245, 100, text=str(elixir), fill="black", font=("Arial", 12))

# Avvia l'incremento iniziale
update_elixir()
root.bind("<Key>", spending_elixir)
root.mainloop()