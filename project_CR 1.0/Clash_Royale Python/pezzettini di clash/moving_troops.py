import tkinter as tk
import time
import os


#game intro
os.system('"C:\\Users\\leizh\\OneDrive\\Desktop\\project-CR\\clash royale game intro.mp4"')
time.sleep(16)
os.system('taskkill /F /IM Microsoft.Media.Player.exe')

#crea il canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=600)
canvas.pack()

# Crea la mappa:
# il fiume
canvas.create_rectangle(0, 0, 600, 600, fill="blue")
# Due campi verdi
canvas.create_rectangle(0, 0, 300, 275, fill="green")
canvas.create_rectangle(300, 325, 0, 600, fill="green")
# Due ponti
canvas.create_rectangle(30, 275, 80, 325, fill="brown")
canvas.create_rectangle(270, 275, 220, 325, fill="brown")
# Torri nemiche
canvas.create_rectangle(115, 15, 185, 85, fill="red")
canvas.create_rectangle(30, 100, 80, 150, fill="red")
canvas.create_rectangle(270, 100, 220, 150, fill="red")
# Le tue torri
canvas.create_rectangle(115, 515, 185, 585, fill="light blue")
canvas.create_rectangle(30, 500, 80, 450, fill="light blue")
canvas.create_rectangle(270, 500, 220, 450, fill="light blue")
# Posti di evocazione
canvas.create_oval(50, 440, 60, 450, fill="white")
canvas.create_oval(250, 440, 240, 450, fill="white")
canvas.create_oval(50, 335, 60, 325, fill="white")
canvas.create_oval(250, 335, 240, 325, fill="white")

# Definizione della distruzione del canvas:
def clear_canvas(canvas):
    canvas.delete("all")

#cordinate dei posti di evocazione
cordinate_1 = [40, 260] 
cordinate_2 = [430, 430]
cordinate_3 = [70, 230]
cordinate_4 = [460, 460]

# Definizione delle truppe da battaglia:
def move_knight():
    canvas.move(knight, 0, -10)
    root.after(100, move_knight)
def knight():
    global knight
    knight = canvas.create_oval(cordinate_1[0], cordinate_2[0], cordinate_3[0], cordinate_4[0], fill='grey')
    move_knight()

def move_valkyrie():
    canvas.move(valkyrie, 0, -10)
    root.after(100, move_valkyrie)
def valkyrie():
    global valkyrie
    valkyrie = canvas.create_oval(cordinate_1[0], cordinate_2[0], cordinate_3[0], cordinate_4[0], fill='orange')
    move_valkyrie()

def move_elite_barbs():
    canvas.move(elite_barbs, 0, -10)
    root.after(100, move_knight)
def elite_barbs():
    global elite_barbs
    elite_barbs = canvas.create_oval(cordinate_1[0], cordinate_2[0], cordinate_3[0], cordinate_4[0], fill='yellow')
    move_elite_barbs()

def move_pekka():
    canvas.move(pekka, 0, -10)
    root.after(100, move_pekka)
def pekka():
    global pekka
    pekka = canvas.create_oval(cordinate_1[0], cordinate_2[0], cordinate_3[0], cordinate_4[0], fill='purple')
    move_pekka()

def move_mini_pekka():
    canvas.move(mini_pekka, 0, -10)
    root.after(100, move_knight)
def mini_pekka():
    global mini_pekka
    mini_pekka = canvas.create_oval(cordinate_1[0], cordinate_2[0], cordinate_3[0], cordinate_4[0], fill='light blue')
    move_mini_pekka()

def move_lumberjack_unraged():
        canvas.move(lumberjack_unraged, 0, -10)
        root.after(100, move_lumberjack_unraged)
def lumberjack_unraged():
    global lumberjack_unraged
    lumberjack_unraged = canvas.create_oval(cordinate_1[0], cordinate_2[0], cordinate_3[0], cordinate_4[0], fill='pink')
    move_lumberjack_unraged()

def move_giant_skelly_unbombed():
        canvas.move(giant_skelly_unbombed, 0, -10)
        root.after(100, move_giant_skelly_unbombed)
def giant_skelly_unbombed():
    global giant_skelly_unbombed
    giant_skelly_unbombed = canvas.create_oval(cordinate_1[0], cordinate_2[0], cordinate_3[0], cordinate_4[0], fill='off white')
    move_giant_skelly_unbombed()

def move_miner():
        canvas.move(miner, 0, -10)
        root.after(100, move_miner)
def miner():
    global miner
    miner = canvas.create_oval(cordinate_1[0], cordinate_2[0], cordinate_3[0], cordinate_4[0], fill='black')
    move_miner()

# Definizione dei autori di clash royale python 1.0
def credits():
    print("")
    print("Clash Royale Python 1.0")
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
    time.sleep(1/5)
    print("")
    time.sleep(1/5)
    print("Chand Sipione")
    time.sleep(1/5)
    print("game account tag uyql8gpuv")
    time.sleep(1/5)
    print("")
    time.sleep(1)
    print("join our clan! It's called clsastrunz")
    time.sleep(1)
    print("")
    time.sleep(1)
    print("Idea from:")
    time.sleep(1)
    print("Giovanni DeSabbata")
    time.sleep(1/5)
    print("Aman Hossain")
    time.sleep(1/5)
    print("Chand Sipione")
    time.sleep(1/5)
    print("Samuele Driussi")
    time.sleep(1/5)
    print("ZhenTing Lei")
    time.sleep(1)
    print("")
    time.sleep(1)
    print("help and supports:")
    time.sleep(1)
    print("Copilot")
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

# Saluto dai programmatori
print("Hello from the programmers")
time.sleep(3)

#creazione mazzo(non randomico)
tanky_deck = ["knight", "valkyrie", "pekka", "mini_pekka", "lumberjack_unraged", "elite_barbs", "giant_skelly_unbombed", "miner"]
print(tanky_deck[0], tanky_deck[1], tanky_deck[2], tanky_deck[3])


# Il card cycle
def card_cycle(event):
    if event.keysym == "1":
        tanky_deck.append(tanky_deck[0])
        tanky_deck.pop(0)

        if tanky_deck[0] == "knight":
            knight()
        elif tanky_deck[0] == "valkyrie":
            valkyrie()
        elif tanky_deck[0] == "pekka":
            pekka()
        elif tanky_deck[0] == "mini_pekka":
            mini_pekka()
        elif tanky_deck[0] == "lumberjack_unranged":
            lumberjack_unraged()
        elif tanky_deck[0] == "elite_barbs":
            elite_barbs()
        elif tanky_deck[0] == "giant_skelly_umbombed":
            giant_skelly_unbombed()
        elif tanky_deck[0] == "miner":
            miner()
        print(tanky_deck[0], tanky_deck[1], tanky_deck[2], tanky_deck[3])

    elif event.keysym == "2":
        tanky_deck.append(tanky_deck[1])
        tanky_deck.pop(2)

        if tanky_deck[1] == "knight":
            knight()
        elif tanky_deck[1] == "valkyrie":
            valkyrie()
        elif tanky_deck[1] == "pekka":
            pekka()
        elif tanky_deck[1] == "mini_pekka":
            mini_pekka()
        elif tanky_deck[1] == "lumberjack_unranged":
            lumberjack_unraged()
        elif tanky_deck[1] == "elite_barbs":
            elite_barbs()
        elif tanky_deck[1] == "giant_skelly_umbombed":
            giant_skelly_unbombed()
        elif tanky_deck[1] == "miner":
            miner()
        print(tanky_deck[0], tanky_deck[1], tanky_deck[2], tanky_deck[3])

    elif event.keysym == "3":
        tanky_deck.append(tanky_deck[2])
        tanky_deck.pop(3)
        
        if tanky_deck[2] == "knight":
            knight()
        elif tanky_deck[2] == "valkyrie":
            valkyrie()
        elif tanky_deck[2] == "pekka":
            pekka()
        elif tanky_deck[2] == "mini_pekka":
            mini_pekka()
        elif tanky_deck[2] == "lumberjack_unranged":
            lumberjack_unraged()
        elif tanky_deck[2] == "elite_barbs":
            elite_barbs()
        elif tanky_deck[2] == "giant_skelly_umbombed":
            giant_skelly_unbombed()
        elif tanky_deck[2] == "miner":
            miner()
        print(tanky_deck[0], tanky_deck[1], tanky_deck[2], tanky_deck[3])

    elif event.keysym == "4":
        tanky_deck.append(tanky_deck[3])
        tanky_deck.pop(3)

        if tanky_deck[3] == "knight":
            knight()
        elif tanky_deck[3] == "valkyrie":
            valkyrie()
        elif tanky_deck[3] == "pekka":
            pekka()
        elif tanky_deck[3] == "mini_pekka":
            mini_pekka()
        elif tanky_deck[3] == "lumberjack_unranged":
            lumberjack_unraged()
        elif tanky_deck[3] == "elite_barbs":
            elite_barbs()
        elif tanky_deck[3] == "giant_skelly_umbombed":
            giant_skelly_unbombed()
        elif tanky_deck[3] == "miner":
            miner()
        print(tanky_deck[0], tanky_deck[1], tanky_deck[2], tanky_deck[3])
    # Emotes
    elif event.keysym == "h":
        os.system('""C:\\Users\\leizh\\OneDrive\\Desktop\\project-CR\\emotes\\heheheha.png""')
        time.sleep(2)
        os.system('taskkill /F /IM PhotosService.exe')
    elif event.keysym == "j":
        os.system('""C:\\Users\\leizh\\OneDrive\\Desktop\\project-CR\\emotes\\happy_king.png""')
        time.sleep(2)
        os.system('taskkill /F /IM Microsoft.Media.Player.exe')
    elif event.keysym == "k":
        os.system('""C:\\Users\\leizh\\OneDrive\\Desktop\\project-CR\\emotes\\angry_king.png""')
        time.sleep(2)
        os.system('taskkill /F /IM Microsoft.Media.Player.exe')
    elif event.keysym == "l":
        os.system('""C:\\Users\\leizh\\OneDrive\\Desktop\\project-CR\\emotes\\king_crying_emote.png""')
        time.sleep(2)
        os.system('taskkill /F /IM Microsoft.Media.Player.exe')
    # Se si esce dal gioco, si vedono i crediti
    elif event.keysym == "m":
        clear_canvas(canvas)
        credits()


# Avviazione:

root.bind("<Key>", card_cycle)
root.mainloop()