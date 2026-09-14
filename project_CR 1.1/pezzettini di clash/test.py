import tkinter as tk
import numpy as np

# crea il canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=625)
canvas.pack()



cordinate_number = 0
# 4 variabili ovvero le cordinate del knigth in alto a sinistra, tutte le altre cordinate si baseranno su queta, ma con -"numero" o +"numero" 
cord1x = 40
cord1y = 315
cord2x = 70
cord2y = 345



# nuovo deck, questa volta più diversificata
basicDeck = np.array([
    ["knightF", "valkyrieF", "pekkaF", "mini_pekka_f", "hogRiderF", "wallBreakerF", "berserkelF", "goblinGangF"],  # Nomi
    [1766, 1908, 3706, 1200, 1696, 336, 1330, 1000],  # Vita
    [220, 267, 1081, 720, 421, 672, 285, 160],  # Danni
    [-5, -5, -3, -5, -10, -10, -10, -7],  # Velocità(dritta)
    [5, 5, 3, 5, 10, 10, 10 , 7],  # Velocità(a sinistra)
    [3, 4, 7, 4, 4, 2, 6, 3],  # Costo
])

# cordinate, ma ce ne sono 4*4*8 = 128 variabili, tra qui 124 con un +"numero", mi sa che è meglio cambiare modo
# Copilot, mentre scrivevo il commento sopra, mi consigliò un ciclo for, ma quando scrivevo il commento sto qua, me lo sconsiglia... 
cords = np.array([
    [cord1x, cord1y, cord2x, cord2y],  # Cordinate knight 1
    [cord1x, cord1y +115, cord2x , cord2y + 115],  # Cordinate knight 2
    [cord1x + 220, cord1y, cord2x + 160, cord2y],  # Cordinate knight 3
    [cord1x + 220, cord1y + 115, cord2x + 160, cord2y + 115],  # Cordinate knight 4
])



#alcune variabili usate momentanealmente per non trovarmi tutto il codice in giallo
cordinates = [[40, 315, 70, 345],[40, 430, 70, 460],[260, 315, 230, 345],[260, 430, 230, 460]]
cordinate_number=0
left_tower_alive = True
right_tower_alive = True
king_health = 6000
health = 3052
right_health = 3052
def reupdate_tower():
    print("")
right_health_text = canvas.create_text(40, 10, text=str(right_health), fill="white", font=("Arial", 12))
def reupdate_right_tower():
    print("")  
def romove_elixir():
    print("")
left_health_text = canvas.create_text(260, 10, text=str(health), fill="white", font=("Arial", 12))
def reupdate_king_tower():
    print("")
king_health_text = canvas.create_text(150, 10, text=str(king_health), fill="white", font=("Arial", 12))





class Troop:
    def __init__(self, canvas, name, health, damage, speed, cost, spawn_point):
        self.canvas = canvas
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.cost = cost
        self.spawn_point = spawn_point
        self.troop = self.canvas.create_oval(spawn_point, fill='grey')
        self.health_text = self.canvas.create_text(spawn_point[0], spawn_point[1] - 10, text=str(self.health), fill="white", font=("Arial", 12))

    def move(self):
        x1, y1, x2, y2 = self.canvas.coords(self.troop)
        if y1 > 115:
            self.canvas.move(self.troop, 0, self.speed)
        elif y1 <= 115:
            if (cordinate_number == 0 or cordinate_number == 1):
                if left_tower_alive:
                    self.canvas.delete(self.troop)
                    self.canvas.delete(self.health_text)
                    global health
                    health = health - self.damage
                    reupdate_tower()
                    return
                else:
                    self.canvas.move(self.troop, 10, self.speed)
            elif (cordinate_number == 2 or cordinate_number == 3):
                if right_tower_alive:
                    self.canvas.delete(self.troop)
                    self.canvas.delete(right_health_text)
                    global right_health
                    right_health = right_health - self.damage
                    reupdate_right_tower()
                    return
                else:
                    self.canvas.move(self.troop, -10, self.speed)
        if y1 <= 20 and y1 >= 10:
            self.canvas.delete(self.troop)
            self.canvas.delete(king_health_text)
            global king_health
            king_health = king_health - self.damage
            reupdate_king_tower()
            return
        self.canvas.after(100, self.move)

def spawn_troop(name):
    troop_data = basicDeck[:, basicDeck[0] == name].flatten()
    if troop_data.size > 0:
        name, health, damage, speed, cost, spawn_point = troop_data
        troop = Troop(canvas, name, int(health), int(damage), int(speed), int(cost), cordinates[cordinate_number])
        troop.move()

# Esempio di utilizzo della funzione spawn_troop
spawn_troop("valkyrieF")

root.mainloop()