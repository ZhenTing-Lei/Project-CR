import tkinter as tk
import time
from PIL import Image, ImageTk  # Import Pillow

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=660)
canvas.pack()
root.title("troops")

#aggiunta delle image e delle grandezze. Mi sa che mi tocca aggiungerle, vado su clash royale, friendly match e rubo, cioè, prendo le sprites
blueTroopsStats = {  # Statistiche delle truppe blu
    "knightF": {"name": "knight", "speed": 2, "health": 100, "damage": 50, "range": 1, "type": "troop", "color": "grey", "size": "medium", "elixir": 3},
    "valkyrieF": {"name": "valkyrie", "speed": 2, "health": 120, "damage": 60, "range": 1, "type": "troop", "color": "orange", "size": "medium", "elixir": 4},
    "pekkaF": {"name": "pekka", "speed": 1, "health": 200, "damage": 100, "range": 1, "type": "troop", "color": "black", "size": "big", "elixir": 7},
    "mini_pekka_f": {"name": "mini_pekka", "speed": 2, "health": 150, "damage": 80, "range": 1, "type": "troop", "color": "black", "size": "medium", "elixir": 4},
    "hogRiderF": {"name": "hogrider", "speed": 3, "health": 90, "damage": 70, "range": 1, "type": "troop", "color": "brown", "size": "medium", "elixir": 4},
    "wallBreakerF": {"name": "wallbreaker", "speed": 3, "health": 50, "damage": 150, "range": 1, "type": "troop", "color": "white", "size": "small", "elixir": 2},
    "fireballF": {"name": "fireball", "speed": 0, "health": 0, "damage": 400, "range": 0, "type": "spell", "color": "red", "size": "superbig", "elixir": 4},
    "zapF": {"name": "zap", "speed": 0, "health": 0, "damage": 200, "range": 0, "type": "spell", "color": "light blue", "size": "medium", "elixir": 2}
}

redTroopsStats = {  # Statistiche delle truppe rosse
    "knightEnemyF": {"name": "knight", "speed": 2, "health": 100, "damage": 50, "range": 1, "type": "troop", "color": "grey", "size": "medium", "elixir": 3},
    "valkyrieEnemyF": {"name": "valkyrie", "speed": 2, "health": 120, "damage": 60, "range": 1, "type": "troop", "color": "orange", "size": "medium", "elixir": 4},
    "pekkaEnemyF": {"name": "pekka", "speed": 1, "health": 200, "damage": 100, "range": 1, "type": "troop", "color": "black", "size": "big", "elixir": 7},
    "mini_pekka_enemy_f": {"name": "mini_pekka", "speed": 2, "health": 150, "damage": 80, "range": 1, "type": "troop", "color": "black", "size": "medium", "elixir": 4},
    "hogRiderEnemyF": {"name": "hogrider", "speed": 3, "health": 90, "damage": 70, "range": 1, "type": "troop", "color": "brown", "size": "medium", "elixir": 4},
    "wallBreakerEnemyF": {"name": "wallbreaker", "speed": 3, "health": 50, "damage": 150, "range": 1, "type": "troop", "color": "white", "size": "small", "elixir": 2},
    "fireballEnemyF": {"name": "fireball", "speed": 0, "health": 0, "damage": 400, "range": 0, "type": "spell", "color": "red", "size": "superbig", "elixir": 4},
    "zapEnemyF": {"name": "zap", "speed": 0, "health": 0, "damage": 200, "range": 0, "type": "spell", "color": "light blue", "size": "medium", "elixir": 2}
}



root.mainloop()