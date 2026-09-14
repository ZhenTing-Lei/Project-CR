import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=660)
canvas.pack()

cord1 = canvas.create_oval(50, 135, 60, 125, fill="white")
cord2 = canvas.create_oval(50, 240, 60, 250, fill="white")
cord3 = canvas.create_oval(250, 135, 240, 125, fill="white")
cord4 = canvas.create_oval(250, 240, 240, 250, fill="white")

deck = ["knight", "zap", "fireball", "hogRider", "miniPekka", "pekka", "valkyrie", "wallBreaker"]
enemyAtLeft, enemyAtRight = False, False
def botSpawnTroops():
    global enemyAtLeft, enemyAtRight, point
    if enemyAtLeft:
        point = random.choice([cord1, cord2])
        enemyAtLeft = False
        print("troop spawned in the left")
    elif enemyAtRight:
        point = random.choice([cord3, cord4])
        enemyAtRight = False
        print("troop spawned in the right")
    canvas.create_oval(canvas.coords(point), fill="red")  # Draw a red circle at the chosen point
    print(f"troop {deck[0]} spawned at {point}")
    deck.append(deck.pop(0))  # Move the first troop to the end of the deck

def checkAttacks(event):
    global enemyAtLeft, enemyAtRight
    if event.keysym:  # Check if a key is pressed
        if random.choice([True, False]):  # Randomly choose left or right
            enemyAtLeft = True
        else:
            enemyAtRight = True
        botSpawnTroops()

root.bind("<Key>", checkAttacks)
root.mainloop()