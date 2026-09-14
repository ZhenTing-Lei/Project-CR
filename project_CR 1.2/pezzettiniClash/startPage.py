#start page
import tkinter as tk
import random
import time
import numpy as np

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=660)
canvas.pack()

#solo carte del 2016, per abbassare la complessità
cards = {
    # Truppe
    "knightF": {"name": "knight", "speed": 2, "health": 100, "damage": 50, "range": 1, "type": "troop", "color": "grey", "size": "medium", "elixir": 3},
    "archerF": {"name": "archer", "speed": 2, "health": 50, "damage": 30, "range": 3, "type": "troop", "color": "green", "size": "small", "elixir": 3},
    "goblinF": {"name": "goblin", "speed": 3, "health": 40, "damage": 30, "range": 1, "type": "troop", "color": "green", "size": "small", "elixir": 2},
    "spearGoblinF": {"name": "spear_goblin", "speed": 3, "health": 40, "damage": 20, "range": 5, "type": "troop", "color": "green", "size": "small", "elixir": 2},
    "giantF": {"name": "giant", "speed": 1, "health": 300, "damage": 50, "range": 1, "type": "troop", "color": "blue", "size": "big", "elixir": 5},
    "mini_pekka_f": {"name": "mini_pekka", "speed": 2, "health": 150, "damage": 80, "range": 1, "type": "troop", "color": "black", "size": "medium", "elixir": 4},
    "valkyrieF": {"name": "valkyrie", "speed": 2, "health": 120, "damage": 60, "range": 1, "type": "troop", "color": "orange", "size": "medium", "elixir": 4},
    "pekkaF": {"name": "pekka", "speed": 1, "health": 200, "damage": 100, "range": 1, "type": "troop", "color": "black", "size": "big", "elixir": 7},
    "hogRiderF": {"name": "hog_rider", "speed": 3, "health": 90, "damage": 70, "range": 1, "type": "troop", "color": "brown", "size": "medium", "elixir": 4},
    "balloonF": {"name": "balloon", "speed": 2, "health": 150, "damage": 200, "range": 1, "type": "troop", "color": "red", "size": "big", "elixir": 5},
    "wizardF": {"name": "wizard", "speed": 2, "health": 80, "damage": 100, "range": 3, "type": "troop", "color": "purple", "size": "medium", "elixir": 5},
    "musketeerF": {"name": "musketeer", "speed": 2, "health": 80, "damage": 100, "range": 6, "type": "troop", "color": "pink", "size": "medium", "elixir": 4},
    "skeletonF": {"name": "skeleton", "speed": 3, "health": 20, "damage": 10, "range": 1, "type": "troop", "color": "white", "size": "small", "elixir": 1},
    "skeletonArmyF": {"name": "skeleton_army", "speed": 3, "health": 20, "damage": 10, "range": 1, "type": "troop", "color": "white", "size": "small", "elixir": 3},
    "princeF": {"name": "prince", "speed": 2, "health": 150, "damage": 120, "range": 1, "type": "troop", "color": "yellow", "size": "big", "elixir": 5},
    "babyDragonF": {"name": "baby_dragon", "speed": 2, "health": 100, "damage": 50, "range": 3, "type": "troop", "color": "green", "size": "medium", "elixir": 4},
    "witchF": {"name": "witch", "speed": 2, "health": 80, "damage": 30, "range": 3, "type": "troop", "color": "purple", "size": "medium", "elixir": 5},
    "golemF": {"name": "golem", "speed": 1, "health": 500, "damage": 100, "range": 1, "type": "troop", "color": "dark grey", "size": "superbig", "elixir": 8},
    "barbariansF": {"name": "barbarians", "speed": 2, "health": 100, "damage": 50, "range": 1, "type": "troop", "color": "yellow", "size": "medium", "elixir": 5},
    # Incantesimi
    "fireballF": {"name": "fireball", "speed": 0, "health": 0, "damage": 400, "range": 0, "type": "spell", "color": "red", "size": "superbig", "elixir": 4},
    "zapF": {"name": "zap", "speed": 0, "health": 0, "damage": 200, "range": 0, "type": "spell", "color": "light blue", "size": "medium", "elixir": 2},
    "arrowsF": {"name": "arrows", "speed": 0, "health": 0, "damage": 300, "range": 0, "type": "spell", "color": "red", "size": "superbig", "elixir": 3},
    "rocketF": {"name": "rocket", "speed": 0, "health": 0, "damage": 500, "range": 0, "type": "spell", "color": "black", "size": "superbig", "elixir": 6},
    "freezeF": {"name": "freeze", "speed": 0, "health": 0, "damage": 0, "range": 0, "type": "spell", "color": "white", "size": "medium", "elixir": 4},
    # Edifici
    "cannonF": {"name": "cannon", "speed": 0, "health": 300, "damage": 50, "range": 6, "type": "building", "color": "grey", "size": "medium", "elixir": 3},
    "teslaF": {"name": "tesla", "speed": 0, "health": 300, "damage": 50, "range": 6, "type": "building", "color": "light grey", "size": "medium", "elixir": 4},
    "infernoTowerF": {"name": "inferno_tower", "speed": 0, "health": 300, "damage": 50, "range": 6, "type": "building", "color": "black", "size": "medium", "elixir": 5},
    "bombTowerF": {"name": "bomb_tower", "speed": 0, "health": 300, "damage": 50, "range": 6, "type": "building", "color": "brown", "size": "medium", "elixir": 4},
    "goblinHutF": {"name": "goblin_hut", "speed": 0, "health": 300, "damage": 0, "range": 0, "type": "building", "color": "green", "size": "medium", "elixir": 5},
    "barbarianHutF": {"name": "barbarian_hut", "speed": 0, "health": 300, "damage": 0, "range": 0, "type": "building", "color": "yellow", "size": "big", "elixir": 7},
    "xBowF": {"name": "x_bow", "speed": 0, "health": 300, "damage": 50, "range": 11, "type": "building", "color": "grey", "size": "big", "elixir": 6},
    "mortarF": {"name": "mortar", "speed": 0, "health": 300, "damage": 50, "range": 11, "type": "building", "color": "brown", "size": "big", "elixir": 4},
}
sizes={"small":10,"medium":15,"big":20,"superbig":40} #questo implementa le dimensioni delle truppe

#deck
deck = [ "zapF","knightF", "valkyrieF", "pekkaF", "mini_pekka_f", "hogRiderF", "wallBreakerF", "fireballF"]

def intros(): #l'introduzione del gioco(homepage)
    yellowSquare = canvas.create_rectangle(75, 275, 225, 325, fill="yellow")
    greySquare = canvas.create_rectangle(175, 5, 275, 75, fill="grey")
    blueSquare = canvas.create_rectangle(50, 360, 250, 480, fill="light blue")
    clashText1 = canvas.create_text(150, 100, text=str("welcome to:"), fill="black", font=("Arial", 12))
    clashText2 = canvas.create_text(150, 150, text=str("Clash royale \n simulator"), fill="black", font=("Arial", 30))

    #funzioni per i bottoni
    def deckCheck(): #sta roba ti crea il mazzo
        global deck
        print("Deck edited")
        print("Your deck is:", deck)
    def deckEdit():
        global deck
        deck = []  # Cancella il mazzo esistente
        all_cards = list(cards.keys())  # Ottieni tutte le chiavi (nomi delle carte) dal dizionario cards
        deck = random.sample(all_cards, 8)  # Seleziona 8 carte casuali
        print("Deck edited")
        print("Your new deck is:", deck)
    def credits(): #questo stampa i crediti
        credits_window = tk.Toplevel(root)
        credits_window.title("Credits")
        credits_window.geometry("400x500")
        credits_text = tk.Text(credits_window, wrap="word")
        credits_text.pack(expand=True, fill="both")
        credits = [
        "Sorry, but for now we've just got some credits:"
        "",
        "Clash Royale Python 1.2",
        "",
        "Programmers:",
        "",
        "ZhenTing Lei\ngame account tag l9v9qcqc",
        "",
        "Giovanni De Sabbata\ngame account tag gj9ljcq8g",
        "",
        "join our clan! It's called COP gaming"
        "",
        "help and supports:",
        "Copi_lot",
        "",
        "Clash Royale game rights:",
        "Sup\nerc\nell",
        "more info on:",
        "https://supercell.com/en/",
        "",
        "thanks for playing❤️ !"
        ]
        for line in credits:
            credits_text.insert("end", line + "\n")
            credits_text.update()
            time.sleep(1)
        credits_text.insert("end", "Closing in 3 seconds...")
        credits_text.update()
        time.sleep(3)
        credits_window.destroy()
    def deleteIntro():#cancella l'introduzione, dopo dovrà anche partire il gioco
        if deck == []:#sta roba controlla che tu abbia un mazzo
            print("You must edit your deck before starting the game")
            return
        else:
            canvas.delete(yellowSquare) #distruggi intro
            canvas.delete(greySquare)
            canvas.delete(blueSquare)
            canvas.delete(clashText1)
            canvas.delete(clashText2)
            accesButton.destroy()
            controllButton.destroy()
            canvas.delete("all")
            canvas.pack_forget()
            print("Prepare yourself, the game is initializing...")
            time.sleep(3)

    #creazione dei bottoni
    changeButton = tk.Button(root, text="Edick Deck",bg="light blue", activebackground="blue", command=deckEdit)
    controllButton = tk.Button(root, text="Check Deck",bg="light blue", activebackground="blue", command=deckCheck)
    creditsButton = tk.Button(root, text="Credits",bg="grey", activebackground="grey", command=credits)
    accesButton = tk.Button(root, text="Click to battle", bg="yellow", activebackground="yellow",command=deleteIntro)
    tutorialButton = tk.Button(root, text="Tutorial",bg="grey", activebackground="grey", command=deckCheck)
    #posizionamento dei bottoni
    canvas.create_window(150, 400, window=changeButton)
    canvas.create_window(150, 450, window=controllButton)
    canvas.create_window(225, 25, window=creditsButton)
    canvas.create_window(150, 300, window=accesButton)
    canvas.create_window(225, 60, window=tutorialButton)

#avviation
intros()
root.mainloop()