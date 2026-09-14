# pagina iniziale del gioco e crediti
import tkinter as tk
import time
import os

#crea il canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=625)
canvas.pack()

yellowSquare = canvas.create_rectangle(75, 275, 225, 325, fill="yellow")
greySquare = canvas.create_rectangle(150, 25, 300, 75, fill="grey")
trashTime = 123456789

def credits():
    print("")
    print("Clash Royale Python 1.1")
    time.sleep(1)
    print("")
    print("Credits:")
    print("")
    time.sleep(1)
    print("Programmers:")
    time.sleep(1)
    print("ZhenTing Lei")
    time.sleep(1/5)
    print("game account tag l9v9qcqc")
    time.sleep(1/5)
    print("")
    time.sleep(1/5)
    print("Giovanni DeSabbata")
    time.sleep(1/5)
    print("game account tag gj9ljcq8g")
    time.sleep(1)
    print("")
    print("join our clan! It's called COP gaming")
    time.sleep(1)
    print("")
    print("help and supports:")
    time.sleep(1)
    print("Copi_lot")
    time.sleep(1)
    print("")
    time.sleep(1)
    print("Clash Royale game rights:")
    time.sleep(1/5)
    print("Sup\nerc\nell")
    time.sleep(1/5)
    print("")
    print("more info on:")
    time.sleep(1/5)
    print("https://supercell.com/en/")
    time.sleep(1/5)
    print("")
    time.sleep(1)
    print("thanks for playing❤️ !")
    time.sleep(5)
    print("Game ended, iif you want to play again, restart the game")

def delete_intro():
    global trashTime
    canvas.delete(yellowSquare)
    canvas.delete(greySquare)
    accesButton.destroy()
    controllButtom.destroy()
    trashTime = 0

accesButton = tk.Button(root, text="Click to battle", command=delete_intro, bg="yellow", activebackground="yellow")
controllButtom = tk.Button(root, text="Edit controls", bg="grey", activebackground="grey", command=credits)
canvas.create_window(225, 50, window=controllButtom)
canvas.create_window(150, 300, window=accesButton)

def infiniteWaiting():
    global trashTime
    if trashTime != 0:
        time.sleep(1)
        trashTime -= 1

infiniteWaiting()


print("Game started")
root.mainloop()