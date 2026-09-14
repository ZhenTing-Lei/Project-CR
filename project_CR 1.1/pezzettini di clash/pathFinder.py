import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=670)
canvas.pack()
canvas.create_line(55, 0, 55, 670)
canvas.create_line(245, 0, 245, 670)
pathFound = False
velX = 0
velY = 0
rightTowerAlive = True
leftTowerAlive = False
kingTowerAlive = True
def createMap():
    canvas.create_rectangle(0, 0, 600, 600, fill="blue")
    # Due campi verdi
    canvas.create_rectangle(0, 0, 300, 275, fill="green")
    canvas.create_rectangle(300, 325, 0, 600, fill="green")
    # Due ponti
    canvas.create_rectangle(30, 275, 80, 325, fill="brown")
    canvas.create_rectangle(270, 275, 220, 325, fill="brown")
    # Torri nemiche(con vita)
    king_tower = canvas.create_rectangle(115, 15, 185, 85, fill="red")
    princess_tower=canvas.create_rectangle(30, 100, 80, 150, fill="red")
    right_princess_tower = canvas.create_rectangle(270, 100, 220, 150, fill="red")
    right_tower_alive = True
    left_tower_alive = True
    king_tower_alive= True
    # Le tue torri(senza vita)
    canvas.create_rectangle(115, 515, 185, 585, fill="light blue")
    canvas.create_rectangle(30, 500, 80, 450, fill="light blue")
    canvas.create_rectangle(270, 500, 220, 450, fill="light blue")
    # Posti di evocazione
    canvas.create_oval(50, 335, 60, 325, fill="black")
    canvas.create_oval(250, 335, 240, 325, fill="white")
    canvas.create_oval(50, 440, 60, 450, fill="white")
    canvas.create_oval(250, 440, 240, 450, fill="white")

def onMouseClick(event): #questo serve per prendere le coordinate del click dove piazzare le truppe
    global cordX, cordY, pathFound, troop
    print("clicked at", event.x, event.y)
    cordX = event.x #salva x del click per dopo
    cordY = event.y #salva y del click per dopo
    troop = canvas.create_oval(cordX-10, cordY-10, cordX+10, cordY+10, fill="red")
    pathFound = False
    pathFinder()

def pathFinder():
    global cordX, cordY, troop, pathFound, velX, velY, troopCordX, troopCordY
    troopCordX, troopCordY, x2, y2 = canvas.coords(troop)
    if troopCordY > 150: #nel campo alleato
        if cordX < 150: #campo sinistro
            velX = -5
        elif cordX > 150: #campo destro
            velX = 5
        if (troopCordX > 50 and troopCordX < 60) or (troopCordX > 240 and troopCordX < 250): # se si trova sulla retta via
            pathFound = True
        if not pathFound: #se non è sulla retta via
            canvas.move(troop, velX, -5)
        elif pathFound:
            velX = 0
            velY = -10
            moveTroop()
    elif troopCordY < 160 and troopCordY > 50: #campo nemico, dopo aver distrutto le torri della principessa
        if cordX < 150 and leftTowerAlive==False:
            velX = 5
        elif cordX > 150 and rightTowerAlive==False:
            velX = -5
        velY = -5
        moveTroop()
    else:
        velX, velY = 0, 0
        moveTroop()
    root.after(100, pathFinder)

def moveTroop():
    global troop, velY, velX
    canvas.move(troop, velX, velY)

createMap()
canvas.bind("<Button-1>", onMouseClick)
root.mainloop()