#dopo 8 mesi e 10 giorni, si ricomicia ad lavorare su questo progetto, sperando di ottimizzarlo e aggiungere funzioni migliori
#Finito, in meno di un mese, dal 24/02/2025 al 22/03/2025, il progetto è stato completato, con l'aggiunta di nuove funzioni e la correzione di errori
import tkinter as tk
import time

class ClashRoyaleApp: #l'esistenza intera del codice
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=300, height=660)
        self.canvas.pack()
        self.deck = []
        self.intros()

    def intros(self): #l'introduzione del gioco(homepage)
        yellowSquare = self.canvas.create_rectangle(75, 275, 225, 325, fill="yellow")
        greySquare = self.canvas.create_rectangle(150, 25, 300, 75, fill="grey")
        blueSquare = self.canvas.create_rectangle(80, 380, 220, 420, fill="light blue")
        clashText1 = self.canvas.create_text(150, 100, text=str("welcome to:"), fill="black", font=("Arial", 12))
        clashText2 = self.canvas.create_text(150, 150, text=str("Clash royale \n simulator"), fill="black", font=("Arial", 30))

        def credits(): #questo stampa i crediti
            credits_window = tk.Toplevel(self.root)
            credits_window.title("Credits")
            credits_window.geometry("400x500")
            credits_text = tk.Text(credits_window, wrap="word")
            credits_text.pack(expand=True, fill="both")
            credits = [
            "Sorry, but for now we've just got some credits:"
            "",
            "Clash Royale Python 1.1",
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
 
        def delete_intro():#cancella l'introduzione e fa partire il gioco
            if self.deck == []:   #sta roba controlla che tu abbia un mazzo
                print("You must edit your deck before starting the game")
                return
            else:
                self.canvas.delete(yellowSquare) #distruggi intro
                self.canvas.delete(greySquare)
                self.canvas.delete(blueSquare)
                self.canvas.delete(clashText1)
                self.canvas.delete(clashText2)
                accesButton.destroy()
                controllButton.destroy()
                self.canvas.delete("all")
                self.canvas.pack_forget()
                print("Prepare yourself, the game is initializing...")
                time.sleep(3)
                self.main()
        
        def deck_edit(): #sta roba ti crea il mazzo
            self.deck = [ "zapF","knightF", "valkyrieF", "pekkaF", "mini_pekka_f", "hogRiderF", "wallBreakerF", "fireballF"]
            print("Deck edited")
            print("Your deck is:", self.deck)

        # bottoni
        accesButton = tk.Button(self.root, text="Click to battle", bg="yellow", activebackground="yellow",command=delete_intro)
        controllButton = tk.Button(self.root, text="Edit Deck",bg="light blue", activebackground="blue", command=deck_edit)
        creditsButton = tk.Button(self.root, text="Edit controlls", bg="grey", activebackground="grey", command=credits)
        self.canvas.create_window(150, 400, window=controllButton)
        self.canvas.create_window(150, 300, window=accesButton)
        self.canvas.create_window(225, 50, window=creditsButton) #questo crea i bottoni

    def main(self): #sta roba ti parte il gioco, prima includeva tutto e partiva il gioco da solo, ma per colpa di Gio, ora non è più così grande
        self.canvas = tk.Canvas(self.root, width=300, height=670)
        self.canvas.pack()
        self.create_map()
        place_troop = self.GamePlay(self.deck, self.canvas, self.root)
        self.root.bind("<Key>", place_troop.choose_troop)
        self.canvas.bind("<Button-1>", place_troop.on_mouse_click)
        self.root.mainloop()

    def create_map(self): #sta roba ti crea la mappa
        self.canvas.create_rectangle(0, 0, 600, 600, fill="blue")
        self.canvas.create_rectangle(0, 0, 300, 275, fill="green")
        self.canvas.create_rectangle(300, 325, 0, 600, fill="green")
        self.canvas.create_rectangle(30, 275, 80, 325, fill="brown")
        self.canvas.create_rectangle(270, 275, 220, 325, fill="brown")
        self.canvas.create_rectangle(115, 515, 185, 585, fill="light blue")
        self.canvas.create_rectangle(30, 500, 80, 450, fill="light blue")
        self.canvas.create_rectangle(270, 500, 220, 450, fill="light blue")
        self.canvas.create_text(235, 50, text=str("time    :"), fill="black", font=("arial", 12)) #testo sul canvas del t e un :(timer)

    class GamePlay: #questo è il gioco vero e proprio
        def __init__(self, deck, canvas, root): #questo implementa le variabili che ci servono dopo, ovvero la parte più caotica del codice
            #canvas e root
            self.canvas = canvas
            self.root = root
            #stats delle torri
            self.rightTowerAlive = True
            self.leftTowerAlive = True
            self.kingTowerAlive = True
            self.kingTower = self.canvas.create_rectangle(115, 15, 185, 85, fill="red")
            self.leftPrincessTower = self.canvas.create_rectangle(30, 100, 80, 150, fill="red")
            self.rightPrincessTower = self.canvas.create_rectangle(270, 100, 220, 150, fill="red")
            self.leftHealth = 3052
            self.leftHealthText = self.canvas.create_text(55, 100, text=str(self.leftHealth), fill="white", font=("Arial", 12))
            self.rightHealth = 3052
            self.rightHealthText = self.canvas.create_text(245, 100, text=str(self.rightHealth), fill="white", font=("Arial", 12))
            self.kingHealth = 6000
            self.kingHealthText = self.canvas.create_text(150, 15, text=str(self.kingHealth), fill="white", font=("Arial", 12))
            #deck, truppe e posizionamento
            self.deck = deck
            self.troop_stats = {  #questo implementa le statistiche delle truppe
            "knightF": {"speed": 2, "health": 100, "damage": 50, "range": 1,"type":"troop","color":"grey","size":"medium","elixir":3},
            "valkyrieF": {"speed": 2, "health": 120, "damage": 60, "range": 1,"type":"troop","color":"orange","size":"medium","elixir":4},
            "pekkaF": {"speed": 1, "health": 200, "damage": 100, "range": 1,"type":"troop","color":"black","size":"big","elixir":7},
            "mini_pekka_f": {"speed": 2, "health": 150, "damage": 80, "range": 1,"type":"troop","color":"black","size":"medium","elixir":4},
            "hogRiderF": {"speed": 3, "health": 90, "damage": 70, "range": 1,"type":"troop","color":"brown","size":"medium","elixir":4},
            "wallBreakerF": {"speed": 3, "health": 50, "damage": 150, "range": 1,"type":"troop","color":"white","size":"small","elixir":2},
            "fireballF": {"speed": 0,"health": 0, "damage": 400, "range": 0,"type":"spell","color":"red","size":"superbig","elixir":4},
            "zapF": {"speed": 0, "health": 0, "damage": 200, "range": 0,"type":"spell","color":"light blue","size":"medium","elixir":2}
            }#nota: per adesso il range è irrilevante in quanto tutte le truppe sono a corpo a corpo o spell
            self.sizes={"small":10,"medium":15,"big":20,"superbig":40} #questo implementa le dimensioni delle truppe
            self.troops_in_game = [] #lista delle truppe in gioco (potrebbe creare errori con matrix o valori vuoti allo start)
            self.id = 0 #id delle truppe
            self.x_mouse_click = 100 #posizione iniziale delle truppe, da sostituire con un errore
            self.y_mouse_click = 100 #da sostituire con un errore
            #elisirrr e timer, ma anche parte di deck
            self.elixir = 6 #elisir iniziale
            self.update_elixir() #comincia elisir
            self.troop_handler() #gestisce le truppe
            print(" ".join(str(self.deck[i]) for i in range(4))) #stampa prime 4 carte del mazzo
            self.min = 3 #tempo rimanente in minuti
            self.sec = 0 #rempo rimanente in secondi
            self.minText = self.canvas.create_text(250, 50, text=str("3"), fill="black", font=("arial", 12)) #testo sul canvas dei minuti
            self.secText = self.canvas.create_text(270, 50, text=str("0"), fill="black", font=("arial", 12)) #testo sul canvas dei secondi
            self.timer() #comincia il timer
            self.elixirUI = canvas.create_rectangle(0, 600, 180, 650, fill="purple") # l'elisir in modalità barra
            for line in range(10): # ciclo for per una parte dell'elisir in modalità  barra
                self.canvas.create_line(30*line, 600, 30*line, 625, fill="black")
            self.showElixirBar() # funzione per inizializarre l'elisir in modalità barra
            for line2 in range(2):
                self.canvas.create_line(150*line2, 625, 150*line2, 670, fill="black")
            self.canvas.create_line(0, 647, 300, 647, fill="black")
            #carte sul tk
            self.card1 = canvas.create_text(75, 635, text=(f"click 1: {self.deck[0]}):{self.troop_stats[self.deck[0]]['elixir']}"), fill="black", font=("Arial", 12))
            self.card2 = canvas.create_text(225, 635, text=(f"click 2: {self.deck[1]}:{self.troop_stats[self.deck[1]]['elixir']}"), fill="black", font=("Arial", 12))
            self.card3 = canvas.create_text(75, 660, text=(f"click 3: {self.deck[2]}:{self.troop_stats[self.deck[2]]['elixir']}"), fill="black", font=("Arial", 12))
            self.card4 = canvas.create_text(225, 660, text=(f"click 4: {self.deck[3]}:{self.troop_stats[self.deck[3]]['elixir']}"), fill="black", font=("Arial", 12))
            #punto spawn truppe
            self.spawnPoint = canvas.create_oval(100, 100, 110, 110, fill="black") #punto di spawn delle truppe
            
        def update_elixir(self): #questo serve per aggiornare l'elixir
            try:
                self.canvas.delete(self.elixir_text)
            except AttributeError:
                pass
            self.elixir += 1
            if self.elixir > 10:
                self.elixir = 10
            self.elixir_text = self.canvas.create_text(145, 594, text=str(self.elixir), fill="black", font=("Arial", 12))
            self.canvas.after(2800, self.update_elixir)

        def remove_elixir(self,remove): #rimuove l'elisir e controlla che tu possa farlo
            if (self.elixir - remove>=0):
                self.elixir -= remove
                self.canvas.delete(self.elixir_text)
                self.elixir_text = self.canvas.create_text(145, 590, text=str(self.elixir), fill="black", font=("Arial", 12))
                return True
            else:
                return False
        
        def showElixirBar(self): #questo serve per mostrare l'elisir in modalità barra
            try:
                self.canvas.delete(self.elixirUI)
            except AttributeError:
                pass
            self.elixirUI = self.canvas.create_rectangle(0, 600, 30*self.elixir, 625, fill="purple")
            for line in range(10):
                self.canvas.create_line(30*line, 600, 30*line, 625, fill="black")
            self.canvas.after(100, self.showElixirBar)

        def timer(self): #questo serve per aggiornare l'elixir
            try:
                self.canvas.delete(self.minText)
                self.canvas.delete(self.secText)
            except AttributeError:
                pass
            if self.sec>0:
                self.sec -= 1
            else:
                self.sec = 60
                self.min -= 1 
            self.minText = self.canvas.create_text(250, 50, text=str(self.min), fill="black", font=("arial", 12))
            self.secText = self.canvas.create_text(270, 50, text=str(self.sec), fill="black", font=("arial", 12))
            self.canvas.after(1000, self.timer)

        def on_mouse_click(self, event): #questo serve per prendere le coordinate del click dove piazzare le truppe
            print("spawn point:", event.x, event.y)
            self.canvas.delete(self.spawnPoint)
            self.spawnPoint = self.canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="black")
            self.x_mouse_click = event.x #salva x del click per dopo
            self.y_mouse_click = event.y #salva y del click per dopo

        def choose_troop(self, event): #scegliere che truppa delle 4 piazzare
            if event.keysym in ["1", "2", "3", "4"]:
                self.spawn_troop(int(event.keysym))

        def spawn_troop(self, key): #questo tiene la logica per ciclare il mazzo e printaremnuove carte
            if self.y_mouse_click < 330 and self.troop_stats[self.deck[key-1]]["type"] == "troop":
                print("You can't place troops here")
                return
            if self.remove_elixir(self.troop_stats[self.deck[key-1]]["elixir"]):
                print("spawned:", self.deck[key-1])
                self.deck.append(self.deck[key-1])
                self.troop_specific_stats = self.troop_stats[self.deck[key-1]]
                self.deck.pop(key-1)
                print(" ".join(str(self.deck[i]) for i in range(4)))
                self.canvas.delete(self.card1, self.card2, self.card3, self.card4)
                self.canvas.create_line(0, 647, 300, 647, fill="black")
                self.card1 = self.canvas.create_text(75, 635, text=(f"click 1: {self.deck[0]}:{self.troop_stats[self.deck[0]]['elixir']}"), fill="black", font=("Arial", 12))
                self.card2 = self.canvas.create_text(225, 635, text=(f"click 2: {self.deck[1]}:{self.troop_stats[self.deck[1]]['elixir']}"), fill="black", font=("Arial", 12))
                self.card3 = self.canvas.create_text(75, 660, text=(f"click 3: {self.deck[2]}:{self.troop_stats[self.deck[2]]['elixir']}"), fill="black", font=("Arial", 12))
                self.card4 = self.canvas.create_text(225, 660, text=(f"click 4: {self.deck[3]}:{self.troop_stats[self.deck[3]]['elixir']}"), fill="black", font=("Arial", 12))
                self.initiate_troop(self.troop_specific_stats["speed"],self.troop_specific_stats["health"], self.troop_specific_stats["damage"], self.troop_specific_stats["type"], self.troop_specific_stats["color"], self.troop_specific_stats["size"], self.id)
            else:
                print("Not enough elixir")

        def initiate_troop(self,speed, health, damage, type, color, size ,id): #questo piazza effetivamente la truppa sul canvass
            x_position = self.x_mouse_click
            y_position = self.y_mouse_click
            x0 = x_position - self.sizes[size]
            y0 = y_position - self.sizes[size]
            x1 = x_position + self.sizes[size]
            y1 = y_position + self.sizes[size]
            troop_id = self.canvas.create_oval(x0, y0, x1, y1, fill=color, tags=id) #crea la truppa sul canvas con il tag "id"
            if type == "troop":
                if y_position < 330: #controlla che non piazzi truppe sopra il ponte
                    self.troops_in_game.append([troop_id, int(x_position), int(y_position), int(health),int(damage),int(speed),(type)])
                    print("placment non")
                else:
                    self.troops_in_game.append([troop_id, int(x_position), int(y_position), int(health),int(damage),int(speed),(type)])
            elif type == "spell":
                self.damage_troops(x0, y0, x1, y1, damage)
                self.canvas.after(1000, lambda: self.canvas.delete(troop_id)) #se è una spell fa il danno e poi la cancella
            self.id += 1 #aumenta lid per la prossima truppa
        
        def troop_handler(self): #questo controlla la vita delle truppe e la loro rimozione a 0 pv
            if not self.troops_in_game:
                self.canvas.after(100, self.troop_handler)
                return

            # Process all troops in the game
            for troop in self.troops_in_game[:]:  # Use a copy of the list to avoid modification issues
                if troop[3] <= 0:  # If the troop's health is 0, remove it
                    self.canvas.delete(troop[0])
                    self.troops_in_game.remove(troop)
            self.troop_mover()
            self.canvas.after(100, self.troop_handler)

        def troop_mover(self): #questo muove le truppe, secondo Zhen è un pathfiner, per Gio è brutforcing
            #non ci ho voglia di scrivere questo fa bla bal, quello fa bla bla
            if not self.troops_in_game:
                return
            for troop in self.troops_in_game:
                id = troop[0]
                x_position = troop[1]
                y_position = troop[2]
                speed = troop[5]
                if 245 > x_position > 150 or x_position < 54:
                    if y_position > 160:
                        x_position += speed
                        self.canvas.move(id, speed, 0)
                    else:
                        if x_position>190:
                            x_position -= speed
                            self.canvas.move(id, -speed, 0)
                        else:
                            self.damage_troops(x_position - 45, y_position-10, x_position, y_position + 10, troop[4])
                        
                elif 150 >= x_position > 55 or x_position > 246:
                    if y_position > 160:
                        x_position -= speed
                        self.canvas.move(id, -speed, 0)
                    else:
                        if x_position<110:
                            x_position += speed
                            self.canvas.move(id, speed, 0)
                        else:
                            self.damage_troops(x_position, y_position-10, x_position+45, y_position + 10, troop[4])
                else:
                    if y_position > 160:
                        y_position -= speed
                        self.canvas.move(id, 0, -speed)
                    else:
                        if x_position < 150:
                            if self.leftTowerAlive:
                                self.damage_troops(x_position - 10, y_position, x_position + 10, y_position + 20, troop[4])
                            else:
                                if y_position>50:
                                    y_position -= speed
                                    self.canvas.move(id, 0, -speed)
                                else:
                                    x_position += speed
                                    self.canvas.move(id, speed, 0)
                        else:
                            if self.rightTowerAlive:
                                self.damage_troops(x_position - 10, y_position, x_position + 10, y_position + 20, troop[4])
                            else:
                                if y_position>50:
                                    y_position -= speed
                                    self.canvas.move(id, 0, -speed)
                                else:
                                    x_position -= speed
                                    self.canvas.move(id, -speed, 0)
                                

                # Update the troop's position in the list
                troop[1] = x_position
                troop[2] = y_position

        def damage_troops(self, x0, y0, x1, y1, damage): #questo fa il danno alle torri
            # Right Princess Tower
            if x0 < 245 < x1 and y0 < 170 < y1 and self.rightTowerAlive:
                self.rightHealth -= damage
            # Left Princess Tower
            if x0 < 55 < x1 and y0 < 170 < y1 and self.leftTowerAlive:
                self.leftHealth -= damage
            # King Tower
            if x0 < 150 < x1 and y0 < 50 < y1 and self.kingTowerAlive:
                self.kingHealth -= damage
            self.update_healths()

        def update_healths(self): #questo riscrive la vita delle torri
            self.canvas.delete(self.leftHealthText)
            self.canvas.delete(self.rightHealthText)
            self.canvas.delete(self.kingHealthText)
            self.leftHealthText = self.canvas.create_text(55, 100, text=str(self.leftHealth), fill="white", font=("Arial", 12))
            self.rightHealthText = self.canvas.create_text(245, 100, text=str(self.rightHealth), fill="white", font=("Arial", 12))
            self.kingHealthText = self.canvas.create_text(150, 15, text=str(self.kingHealth), fill="white", font=("Arial", 12))
            if self.leftHealth <= 0:
                self.leftTowerAlive = False
            if self.rightHealth <= 0:
                self.rightTowerAlive = False
            if self.kingHealth <= 0:
                self.kingTowerAlive = False
            if not self.leftTowerAlive:
                self.canvas.delete(self.leftPrincessTower)
                self.canvas.delete(self.leftHealthText)
            if not self.rightTowerAlive:
                self.canvas.delete(self.rightPrincessTower)
                self.canvas.delete(self.rightHealthText)
            if not self.kingTowerAlive:
                self.canvas.delete(self.kingTower)
                self.canvas.delete(self.kingHealthText)
                print("You won!")
                root.after(3000, self.end_game)
        
        def end_game(self): #questo deleta il canvas se finisci il gioco
            self.canvas.delete("all")
            self.root.destroy()


if __name__ == "__main__":#questo fa partire il gioco
    root = tk.Tk()
    app = ClashRoyaleApp(root)
    root.mainloop()