import tkinter as tk
import numpy as np

# crea il canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=625)
canvas.pack()

# Variabili globali per lo stato delle torri
right_tower_alive = True
left_tower_alive = True
king_tower_alive = True

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

troopStats = {  #questo implementa le statistiche delle truppe
    "knightF": {"speed": 2, "health": 100, "damage": 50, "range": 1, "type": "troop", "color": "grey", "size": "medium", "elixir": 3},
    "valkyrieF": {"speed": 2, "health": 120, "damage": 60, "range": 1, "type": "troop", "color": "orange", "size": "medium", "elixir": 4},
    "pekkaF": {"speed": 1, "health": 200, "damage": 100, "range": 1, "type": "troop", "color": "black", "size": "big", "elixir": 7},
    "mini_pekka_f": {"speed": 2, "health": 150, "damage": 80, "range": 1, "type": "troop", "color": "black", "size": "medium", "elixir": 4},
    "hogRiderF": {"speed": 3, "health": 90, "damage": 70, "range": 1, "type": "troop", "color": "brown", "size": "medium", "elixir": 4},
    "wallBreakerF": {"speed": 3, "health": 50, "damage": 150, "range": 1, "type": "troop", "color": "white", "size": "small", "elixir": 2},
    "fireballF": {"speed": 0, "health": 0, "damage": 400, "range": 0, "type": "spell", "color": "red", "size": "superbig", "elixir": 4},
    "zapF": {"speed": 0, "health": 0, "damage": 200, "range": 0, "type": "spell", "color": "light blue", "size": "medium", "elixir": 2}
}

sizes = {"small": 10, "medium": 15, "big": 20, "superbig": 40}
troops_in_game = []
id_counter = 0
x_mouse_click = 100
y_mouse_click = 100
elixir = 6
deck = ["knightF", "valkyrieF", "pekkaF", "mini_pekka_f"]

def on_mouse_click(event): #questo serve per prendere le coordinate del click dove piazzare le truppe
    global x_mouse_click, y_mouse_click
    print("clicked at", event.x, event.y)
    x_mouse_click, y_mouse_click = event.x, event.y #salva x e y del click per dopo
    chooseTroop(event)
    spawn_troop(chosenTroop)

def chooseTroop(event): #scegliere che truppa delle 4 piazzare, si sceglie con i 4 tasti e si piazza con il mouse
    global chosenTroop
    if event.keysym in ["1", "2", "3", "4"]:
        chosenTroop = int(event.keysym)

def spawn_troop(key): #questo tiene la logica per ciclare il mazzo e printaremnuove carte
    global elixir, deck, id_counter
    if y_mouse_click < 330 and troopStats[deck[key-1]]["type"] == "troop":
        print("You can't place troops here")
        return
    if remove_elixir(troopStats[deck[key-1]]["elixir"]):
        print("spawned:", deck[key-1])
        deck.append(deck[key-1])
        troop_specific_stats = troopStats[deck[key-1]]
        deck.pop(key-1)
        print(" ".join(str(deck[i]) for i in range(4)))
        initiate_troop(troop_specific_stats["speed"], troop_specific_stats["health"], troop_specific_stats["damage"], troop_specific_stats["type"], troop_specific_stats["color"], troop_specific_stats["size"], id_counter)
    else:
        print("Not enough elixir")

def initiate_troop(speed, health, damage, type, color, size, id): #questo piazza effetivamente la truppa sul canvass
    global troops_in_game, id_counter
    x_position = x_mouse_click
    y_position = y_mouse_click
    x0 = x_position - sizes[size]
    y0 = y_position - sizes[size]
    x1 = x_position + sizes[size]
    y1 = y_position + sizes[size]
    troop_id = canvas.create_oval(x0, y0, x1, y1, fill=color, tags=id) #crea la truppa sul canvas con il tag "id"
    if type == "troop":
        if y_position < 330: #controlla che non piazzi truppe sopra il ponte
            troops_in_game.append([troop_id, int(x_position), int(y_position), int(health), int(damage), int(speed), type])
            print("placment non")
        else:
            troops_in_game.append([troop_id, int(x_position), int(y_position), int(health), int(damage), int(speed), type])
    elif type == "spell":
        damage_troops(x0, y0, x1, y1, damage)
        canvas.after(1000, lambda: canvas.delete(troop_id)) #se è una spell fa il danno e poi la cancella
    id_counter += 1 #aumenta lid per la prossima truppa

def troop_handler():
    if not troops_in_game:
        canvas.after(100, troop_handler)
        return
    for troop in troops_in_game:
        if troop[3] <= 0: #se la vita=0 la cancella
            canvas.delete(troop[0])
            troops_in_game.remove(troop)
        else:
            troop_mover()
    canvas.after(100, troop_handler)

def troop_mover():
    global right_tower_alive, left_tower_alive
    if not troops_in_game: #se non ci sono truppe non fare niente
        return
    for troop in troops_in_game:
        id = troop[0]
        x_position = troop[1]
        y_position = troop[2]
        speed = troop[5]
        if 245 > x_position > 150:
            x_position += speed
            canvas.move(id, speed, 0)
        elif 150 >= x_position > 55:
            x_position -= speed
            canvas.move(id, -speed, 0)
        else:
            if y_position > 150:
                y_position -= speed
                canvas.move(id, 0, -speed)
            else:
                if x_position < 150:
                    if left_tower_alive:
                        damage_troops(x_position-20, y_position, x_position+20, y_position+40, troop[4])
                    else:
                        return
                        #go to king tower
                else:
                    if right_tower_alive:
                        damage_troops(x_position-20, y_position, x_position+20, y_position+40, troop[4])
                    else:
                        return
                        #go to king tower
        troop[1] = x_position
        troop[2] = y_position

def remove_elixir(amount):
    global elixir
    if elixir >= amount:
        elixir -= amount
        return True
    return False

def damage_troops(x0, y0, x1, y1, damage):
    # Implementa la logica per danneggiare le truppe
    pass

createMap()
canvas.bind("<Button-1>", on_mouse_click)
root.bind("<Key>", chooseTroop)
troop_handler()
root.mainloop()