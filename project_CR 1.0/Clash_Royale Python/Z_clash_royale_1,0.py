#finalmente, dopo 6 mesi di duro lavoro, siamo riusciti a ricreare Clash Royale usando PYthon, fatto dal 25/01/2024 al 10/06/2024 

import tkinter as tk
import time
import os

#game intro
os.system('C:/Users/leizh/OneDrive/Desktop/project-CR/intro.mp4')
time.sleep(15)
os.system('taskkill /F /IM Microsoft.Media.Player.exe')
print("welcome on this new game, this is a simple clash royale simulator, we hope you'll enjoy this game")
time.sleep(1)

#crea il canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=625)
canvas.pack()

# Crea la mappa:
#il fiume
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
#cordinate dei posti di evocazione
cordinates = [[40, 315, 70, 345],[40, 430, 70, 460],[260, 315, 230, 345],[260, 430, 230, 460]]
cordinate_number=0


#elisirr(FINALMENTE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)(ispirato al sistema delle truppe)
def update_elixir():
    global elixir
    global elixir_text
    canvas.delete(elixir_text)
    elixir += 1
    elixir_text = canvas.create_text(145, 610, text=str(elixir), fill="black", font=("Arial", 12))
    root.after(2800, update_elixir)
elixir = 6
elixir_text = canvas.create_text(145, 610, text=str(elixir), fill="black", font=("Arial", 12))

#timer, tre minuti(ispirato al sistema dell'elisirr)
def conto_alla_rovescia():
    global remaining_time
    global remaining_time_text
    canvas.delete(remaining_time_text)
    remaining_time = remaining_time-1
    remaining_time_text = canvas.create_text(250, 50, text=str(remaining_time), fill="black", font=("arial", 12))
    root.after(1000, conto_alla_rovescia)
remaining_time = 300
remaining_time_text = canvas.create_text(250, 50, text=str(remaining_time), fill="black", font=("arial", 12))
canvas.create_text(245, 25, text="remaining time:", fill="black", font=("arial", 12))

#funzioni di rigeneramento delle torri dopo essere attaccate
def reupdate_tower():
    global health
    global health_text
    global left_tower_alive
    if health<1 and left_tower_alive==True:
        canvas.delete(princess_tower)
        left_tower_alive=False
        print("you've taken down one red tower, congratulations")
    else:
        health_text = canvas.create_text(55, 100, text=str(health), fill="white", font=("Arial", 12))
def reupdate_right_tower():
    global right_health
    global right_health_text
    global right_tower_alive
    if right_health<1:
        canvas.delete(right_princess_tower)
        right_tower_alive = False
        print("you've taken down one red tower, congratulations")
    else:
        right_health_text = canvas.create_text(245, 100, text=str(right_health), fill="white", font=("Arial", 12))
def reupdate_king_tower():
    global king_health
    global king_health_text
    global king_tower_alive
    if king_health<1:
        canvas.delete(king_tower)
        canvas.create_rectangle(0, 0, 300, 700, fill="white")
        print("you won the game")
        os.system('"C://Users//leizh//OneDrive//Desktop//project-CR//you_winned.png"')
        credits()
    else:
        king_health_text = canvas.create_text(150, 15, text=str(king_health), fill="white", font=("Arial", 12))



# Definizione delle truppe da battaglia:
def move_knight_f():
    global health_text
    global health
    global right_health
    global right_health_text
    global right_tower_alive
    global left_tower_alive
    global king_health
    global king_health_text
    x1, knight_cords, x2, y2 = canvas.coords(knight)
    if knight_cords>115:
        canvas.move(knight, 0, -10)
    elif knight_cords <= 115:
        if (cordinate_number==0 or cordinate_number==1):
            if left_tower_alive==True:
                canvas.delete(knight)
                canvas.delete(health_text)
                health=health-1500
                reupdate_tower()
                return
            elif left_tower_alive==False:
                canvas.move(knight, 10, -10)
        elif (cordinate_number==2 or cordinate_number==3):
            if right_tower_alive==True:
                canvas.delete(knight)
                canvas.delete(right_health_text)
                right_health=right_health-1500
                reupdate_right_tower()
                return
            elif right_tower_alive==False:
                canvas.move(knight, -10, -10)
    if knight_cords<=20 and knight_cords>=10:
        canvas.delete(knight)
        canvas.delete(king_health_text)
        king_health = king_health-1500
        reupdate_king_tower()
        return
    root.after(100, move_knight_f)
def knight_f():
    global knight
    knight = canvas.create_oval(cordinates[cordinate_number], fill='grey')
    move_knight_f()

def move_valkyrie_f():
    global health_text, health, valkyrie_cords, right_health, right_health_text, right_tower_alive, left_tower_alive, king_health, king_health_text
    x1, valkyrie_cords, x2, y2 = canvas.coords(valkyrie)
    if valkyrie_cords>115:
        canvas.move(valkyrie, 0, -10)
    elif valkyrie_cords <= 115:
        if (cordinate_number==0 or cordinate_number==1):
            if left_tower_alive==True:
                canvas.delete(valkyrie)
                canvas.delete(health_text)
                health=health-1600
                reupdate_tower()
                return
            elif left_tower_alive==False:
                canvas.move(valkyrie, 10, -10)
        elif (cordinate_number==2 or cordinate_number==3):
            if right_tower_alive==True:
                canvas.delete(valkyrie)
                canvas.delete(right_health_text)
                right_health=right_health-1600
                reupdate_right_tower()
                return
            elif right_tower_alive==False:
                canvas.move(valkyrie, -10, -10)
    if valkyrie_cords<=20 and valkyrie_cords>=10:
        canvas.delete(valkyrie)
        canvas.delete(king_health_text)
        king_health = king_health-1600
        reupdate_king_tower()
        return
    root.after(100, move_valkyrie_f)
def valkyrie_f():
    global valkyrie
    valkyrie = canvas.create_oval(cordinates[cordinate_number], fill='dark orange')
    move_valkyrie_f()

def move_miner_f():
    global health_text
    global health
    global miner_cords
    global right_health
    global right_health_text
    global king_health
    global king_health_text
    x1, miner_cords, x2, y2 = canvas.coords(miner)
    if miner_cords>115:
        canvas.move(miner, 0, -10)
    elif miner_cords <= 115:
        if (cordinate_number==0 or cordinate_number==1):
            if left_tower_alive==True:
                canvas.delete(miner)
                canvas.delete(health_text)
                health=health-1000
                reupdate_tower()
                return
            elif left_tower_alive==False:
                canvas.move(miner, 10, -10)
        elif (cordinate_number==2 or cordinate_number==3):
            if right_tower_alive==True:
                canvas.delete(miner)
                canvas.delete(right_health_text)
                right_health=right_health-1000
                reupdate_right_tower()
                return
            elif right_tower_alive==False:
                canvas.move(miner, -10, -10)
    if miner_cords<=20 and miner_cords>=10:
        canvas.delete(miner)
        canvas.delete(king_health_text)
        king_health = king_health-1000
        reupdate_king_tower()
        return
    root.after(100, move_miner_f)
def miner_f():
    global miner
    miner = canvas.create_oval(cordinates[cordinate_number], fill='dark green')
    move_miner_f()

def move_elite_barb_f():
    global health_text
    global health
    global elite_barb_cords
    global right_health
    global right_health_text
    global king_health
    global king_health_text
    x1, elite_barb_cords, x2, y2 = canvas.coords(elite_barb)
    if elite_barb_cords>115:
        canvas.move(elite_barb, 0, -10)
    elif elite_barb_cords <= 115:
        if (cordinate_number==0 or cordinate_number==1):
            if left_tower_alive==True:
                canvas.delete(elite_barb)
                canvas.delete(health_text)
                health=health-3500
                reupdate_tower()
                return
            elif left_tower_alive==False:
                canvas.move(elite_barb, 10, -10)
        elif (cordinate_number==2 or cordinate_number==3):
            if right_tower_alive==True:
                canvas.delete(elite_barb)
                canvas.delete(right_health_text)
                right_health=right_health-3500
                reupdate_right_tower()
                return
            elif right_tower_alive==False:
                canvas.move(elite_barb, -10, -10)
    if elite_barb_cords<=20 and elite_barb_cords>=10:
        canvas.delete(elite_barb)
        canvas.delete(king_health_text)
        king_health = king_health-3500
        reupdate_king_tower()
        return
    root.after(100, move_elite_barb_f)
def elite_barb_f():
    global elite_barb
    elite_barb = canvas.create_oval(cordinates[cordinate_number], fill='black')
    move_elite_barb_f()

def move_pekka_f():
    global health_text
    global health
    global pekka_cords
    global right_health
    global right_health_text
    global king_health
    global king_health_text
    x1, pekka_cords, x2, y2 = canvas.coords(pekka)
    if pekka_cords>115:
        canvas.move(pekka, 0, -10)
    elif pekka_cords <= 115:
        if (cordinate_number==0 or cordinate_number==1):
            if left_tower_alive==True:
                canvas.delete(pekka)
                canvas.delete(health_text)
                health=health-4500
                reupdate_tower()
                return
            elif left_tower_alive==False:
                canvas.move(pekka, 10, -10)
        elif (cordinate_number==2 or cordinate_number==3):
            if right_tower_alive==True:
                canvas.delete(pekka)
                canvas.delete(right_health_text)
                right_health=right_health-4500
                reupdate_right_tower()
                return
            elif right_tower_alive==False:
                canvas.move(pekka, -10, -10)
    if pekka_cords<=20 and pekka_cords>=10:
        canvas.delete(pekka)
        canvas.delete(king_health_text)
        king_health = king_health-4500
        reupdate_king_tower()
        return
    root.after(100, move_pekka_f)
def pekka_f():
    global pekka
    pekka = canvas.create_oval(cordinates[cordinate_number], fill='violet')
    move_pekka_f()

def move_mini_pekka_f():
    global health_text
    global health
    global mini_pekka_cords
    global right_health
    global right_health_text
    global king_health
    global king_health_text
    x1, mini_pekka_cords, x2, y2 = canvas.coords(mini_pekka)
    if mini_pekka_cords>115:
        canvas.move(mini_pekka, 0, -10)
    elif mini_pekka_cords <= 115:
        if (cordinate_number==0 or cordinate_number==1):
            if left_tower_alive==True:
                canvas.delete(mini_pekka)
                canvas.delete(health_text)
                health=health-4000
                reupdate_tower()
                return
            elif left_tower_alive==False:
                canvas.move(mini_pekka, 10, -10)
        elif (cordinate_number==2 or cordinate_number==3):
            if right_tower_alive==True:
                canvas.delete(mini_pekka)
                canvas.delete(right_health_text)
                right_health=right_health-4000
                reupdate_right_tower()
                return
            elif right_tower_alive==False:
                canvas.move(mini_pekka, -10, -10)
    if mini_pekka_cords<=20 and mini_pekka_cords>=10:
        canvas.delete(mini_pekka)
        canvas.delete(king_health_text)
        king_health = king_health-4000
        reupdate_king_tower()
        return
    root.after(100, move_mini_pekka_f)
def mini_pekka_f():
    global mini_pekka
    mini_pekka = canvas.create_oval(cordinates[cordinate_number], fill='blue')
    move_mini_pekka_f()


def move_lumberjack_f():
    global health_text
    global health
    global right_health
    global right_health_text
    global lumberjack_cords
    global king_health
    global king_health_text
    x1, lumberjack_cords, x2, y2 = canvas.coords(lumberjack)
    if lumberjack_cords>115:
        canvas.move(lumberjack, 0, -10)
    elif lumberjack_cords <= 115:
        if (cordinate_number==0 or cordinate_number==1):
            if left_tower_alive==True:
                canvas.delete(lumberjack)
                canvas.delete(health_text)
                health=health-2500
                reupdate_tower()
                rage=canvas.create_oval(x1-15, lumberjack_cords-15, x2+15, y2+15, fill='purple')
                canvas.lower(rage)
                canvas.tag_raise(rage)
                return
            elif left_tower_alive==False:
                canvas.move(lumberjack, 10, -10)
        elif (cordinate_number==2 or cordinate_number==3):
            if right_tower_alive==True:
                canvas.delete(lumberjack)
                canvas.delete(right_health_text)
                right_health=right_health-2500
                reupdate_right_tower()
                rage=canvas.create_oval(x1-15, lumberjack_cords-15, x2+15, y2+15, fill='purple')
                canvas.lower(rage)
                canvas.tag_raise(rage)
                return
            elif right_tower_alive==False:
                canvas.move(lumberjack, -10, -10)
    if lumberjack_cords<=20 and lumberjack_cords>=10:
        canvas.delete(lumberjack)
        canvas.delete(king_health_text)
        king_health = king_health-2500
        reupdate_king_tower()
        return
    root.after(100, move_lumberjack_f)
def lumberjack_f():
    global lumberjack
    lumberjack = canvas.create_oval(cordinates[cordinate_number], fill='pink')
    move_lumberjack_f()


def move_giant_f():
    global health_text
    global health
    global giant_cords
    global right_health
    global right_health_text
    global king_health
    global king_health_text
    x1, giant_cords, x2, y2 = canvas.coords(giant)
    if giant_cords>115:
        canvas.move(giant, 0, -10)
    elif giant_cords <= 115:
        if (cordinate_number==0 or cordinate_number==1):
            if left_tower_alive==True:
                canvas.delete(giant)
                canvas.delete(health_text)
                health=health-3500
                reupdate_tower()
                return
            elif left_tower_alive==False:
                canvas.move(giant, 10, -10)
        elif (cordinate_number==2 or cordinate_number==3):
            if right_tower_alive==True:
                canvas.delete(giant)
                canvas.delete(right_health_text)
                right_health=right_health-3500
                reupdate_right_tower()
                return
            elif right_tower_alive==False:
                canvas.move(giant, -10, -10)
    if giant_cords<=20 and giant_cords>=10:
        canvas.delete(giant)
        canvas.delete(king_health_text)
        king_health = king_health-3500
        reupdate_king_tower()
        return
    root.after(100, move_giant_f)
def giant_f():
    global giant
    giant = canvas.create_oval(cordinates[cordinate_number], fill='orange')
    move_giant_f()


#definizione del toglimento d'elisir, ne bastano quattro perchè ci sono solo truppe da tre, quattro, sei o sette elisir
def remove_three_elixir():
    global elixir_text
    global elixir
    canvas.delete(elixir_text)
    elixir=elixir-3
    elixir_text = canvas.create_text(145, 610, text=str(elixir), fill="black", font=("Arial", 12))
def remove_four_elixir():
    global elixir_text
    global elixir
    canvas.delete(elixir_text)
    elixir=elixir-4
    elixir_text = canvas.create_text(145, 610, text=str(elixir), fill="black", font=("Arial", 12))
def remove_six_elixir():
    global elixir_text
    global elixir
    canvas.delete(elixir_text)
    elixir=elixir-6
    elixir_text = canvas.create_text(145, 610, text=str(elixir), fill="black", font=("Arial", 12))
def remove_seven_elixir():
    global elixir_text
    global elixir
    canvas.delete(elixir_text)
    elixir=elixir-7
    elixir_text = canvas.create_text(145, 610, text=str(elixir), fill="black", font=("Arial", 12))

# I autori di clash royale python 1.0, compreso copi_lot
def credits():
    print("")
    print("Clash Royale Python 1.0")
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
    time.sleep(1/5)
    print("")
    print("Aman Hossain")
    time.sleep(1/5)
    print("game account tag ")
    time.sleep(1/5)
    print("")
    print("Chand Sipione")
    time.sleep(1/5)
    print("game account tag uyql8gpuv")
    print("")
    time.sleep(1)
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
    print("Game ended, please exit")


#deck fatto per il card cycle, tutti tank e truppe da una persona
tanky_deck = ["knight","valkyrie","pekka","mini_pekka","lumberjack_unraged","elite_barbs","giant","miner"]
print(tanky_deck[0],tanky_deck[1],tanky_deck[2],tanky_deck[3])

# tutte le robe del gioco in un def da mettere all'inizializzazione
def game_play(event):
    #card cycle, la parte più storta e inefficiente del programma
    global cordinate_number
    if event.keysym == "1":
        if tanky_deck[0] == "knight":
            knight_f()
            remove_three_elixir()
        if tanky_deck[0] == "valkyrie":
            valkyrie_f()
            remove_four_elixir()
        if tanky_deck[0] == "pekka":
            pekka_f()
            remove_seven_elixir()
        if tanky_deck[0] == "mini_pekka":
            mini_pekka_f()
            remove_four_elixir()
        if tanky_deck[0] == "lumberjack_unraged":
            lumberjack_f()
            remove_four_elixir()
        if tanky_deck[0] == "elite_barbs":
            elite_barb_f()
            remove_six_elixir()
        if tanky_deck[0] == "giant_skelly":
            giant_f()
            remove_six_elixir()
        if tanky_deck[0] == "miner":
            miner_f()
            remove_three_elixir()
        tanky_deck.append(tanky_deck[0])
        tanky_deck.pop(0)
        print(tanky_deck[0],tanky_deck[1],tanky_deck[2],tanky_deck[3])

    elif event.keysym == "2":
        if tanky_deck[1] == "knight":
            knight_f()
            remove_three_elixir()
        elif tanky_deck[1] == "valkyrie":
            valkyrie_f()
            remove_four_elixir()
        elif tanky_deck[1] == "pekka":
            pekka_f()
            remove_seven_elixir()
        elif tanky_deck[1] == "mini_pekka":
            mini_pekka_f()
            remove_four_elixir()
        elif tanky_deck[1] == "lumberjack_unraged":
            lumberjack_f()
            remove_four_elixir()
        elif tanky_deck[1] == "elite_barbs":
            elite_barb_f()
            remove_six_elixir()
        elif tanky_deck[1] == "giant":
            giant_f()
            remove_six_elixir()
        elif tanky_deck[1] == "miner":
            miner_f()
            remove_three_elixir()
        tanky_deck.append(tanky_deck[1])
        tanky_deck.pop(1)
        print(tanky_deck[0],tanky_deck[1],tanky_deck[2],tanky_deck[3])

    elif event.keysym == "3":
        if tanky_deck[2] == "knight":
            knight_f()
            remove_three_elixir()
        elif tanky_deck[2] == "valkyrie":
            valkyrie_f()
            remove_four_elixir()
        elif tanky_deck[2] == "pekka":
            pekka_f()
            remove_seven_elixir()
        elif tanky_deck[2] == "mini_pekka":
            mini_pekka_f()
            remove_four_elixir()
        elif tanky_deck[2] == "lumberjack_unraged":
            lumberjack_f()
            remove_four_elixir()
        elif tanky_deck[2] == "elite_barbs":
            elite_barb_f()
            remove_six_elixir()
        elif tanky_deck[2] == "giant":
            giant_f()
            remove_six_elixir()
        elif tanky_deck[2] == "miner":
            miner_f()
            remove_three_elixir()
        tanky_deck.append(tanky_deck[2])
        tanky_deck.pop(2)
        print(tanky_deck[0],tanky_deck[1],tanky_deck[2],tanky_deck[3])

    elif event.keysym == "4":
        if tanky_deck[3] == "knight":
            knight_f()
            remove_three_elixir()
        elif tanky_deck[3] == "valkyrie":
            valkyrie_f()
            remove_four_elixir()
        elif tanky_deck[3] == "pekka":
            pekka_f()
            remove_seven_elixir()
        elif tanky_deck[3] == "mini_pekka":
            mini_pekka_f()
            remove_four_elixir()
        elif tanky_deck[3] == "lumberjack_unraged":
            lumberjack_f()
            remove_four_elixir()
        elif tanky_deck[3] == "elite_barbs":
            elite_barb_f()
            remove_six_elixir()
        elif tanky_deck[3] == "giant":
            giant_f()
            remove_six_elixir()
        elif tanky_deck[3] == "miner":
            miner_f()
            remove_three_elixir()
        tanky_deck.append(tanky_deck[3])
        tanky_deck.pop(3)
        print(tanky_deck[0],tanky_deck[1],tanky_deck[2],tanky_deck[3])


    # Per cambiare la posizione di evocazione
    elif event.keysym == "a":
        cordinate_number = 0
        canvas.create_oval(50, 335, 60, 325, fill="black")
        canvas.create_oval(250, 335, 240, 325, fill="white")
        canvas.create_oval(50, 440, 60, 450, fill="white")
        canvas.create_oval(250, 440, 240, 450, fill="white")
    elif event.keysym == "s":
        cordinate_number = 1
        canvas.create_oval(50, 335, 60, 325, fill="white")
        canvas.create_oval(50, 440, 60, 450, fill="black")
        canvas.create_oval(250, 335, 240, 325, fill="white")
        canvas.create_oval(250, 440, 240, 450, fill="white")        
    elif event.keysym == "d":
        cordinate_number = 2
        canvas.create_oval(50, 335, 60, 325, fill="white")
        canvas.create_oval(50, 440, 60, 450, fill="white")
        canvas.create_oval(250, 335, 240, 325, fill="black")
        canvas.create_oval(250, 440, 240, 450, fill="white")
    elif event.keysym == "f":
        cordinate_number = 3
        canvas.create_oval(50, 335, 60, 325, fill="white")
        canvas.create_oval(250, 335, 240, 325, fill="white")
        canvas.create_oval(50, 440, 60, 450, fill="white")
        canvas.create_oval(250, 440, 240, 450, fill="black")


    # Emotes(funziona) e chiusura(non funziona)
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
    elif event.keysym == "m":
        canvas.create_rectangle(0, 0, 300, 600, fill="white")
        print("game ended")
        time.sleep(3)
        credits()


#vita delle torri, sul canvas e sulla RAM
health = 3052
health_text = canvas.create_text(55, 100, text=str(health), fill="white", font=("Arial", 12))
right_health = 3052
right_health_text = canvas.create_text(245, 100, text=str(right_health), fill="white", font=("Arial", 12))
king_health = 6000
king_health_text = canvas.create_text(150, 15, text=str(king_health), fill="white", font=("Arial", 12))

# Avviazione:
update_elixir()
conto_alla_rovescia()
root.bind("<Key>", game_play)
root.mainloop()  