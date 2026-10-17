#da mettere a posto i time sleep
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import time

class ClashRoyaleApp: #l'esistenza intera del codice
    def __init__(self, root):
        self.root = root
        self.width = 300
        self.height = 670
        self.canvas = tk.Canvas(root, width=self.width, height=self.height)
        self.canvas.pack()
        self.deck = []
        self.intros()

    #sti def servono da mettere nei bottoni
    def intros(self): #pagina iniziale(non essential)
        yellowSquare = self.canvas.create_rectangle(75, 275, 225, 325, fill="yellow")
        greySquare = self.canvas.create_rectangle(175, 5, 275, 75, fill="grey")
        blueSquare = self.canvas.create_rectangle(80, 380, 220, 420, fill="light blue")
        clashText1 = self.canvas.create_text(150, 100, text=str("welcome to:"), fill="black", font=("Arial", 12))
        clashText2 = self.canvas.create_text(150, 150, text=str("Clash royale \n simulator"), fill="black", font=("Arial", 30))
        clashText3 = self.canvas.create_text(150, 200, text=str("version 1.2"), fill="black", font=("Arial", 8))

        def credits(): #questo stampa i crediti
            credits_window = tk.Toplevel(self.root)
            credits_window.title("Credits")
            credits_window.geometry("400x500")
            credits_text = tk.Text(credits_window, wrap="word")
            credits_text.pack(expand=True, fill="both")
            credits = [
                "...",
                "No one asked for this, but here are the credits:",
                "",
                "",
                "Clash Royale Python 1.2",
                "",
                "Programmers:",
                "",
                "ZhenTing Lei\ngame account tag l9v9qcqc",
                "",
                "Giovanni De Sabbata\ngame account tag gj9ljcq8g",
                "",
                "join our clan! It's called COP gaming",
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
                time.sleep(0.5)
            credits_text.insert("end", "Closing in 3 seconds...")
            credits_text.update()
            time.sleep(3)
            credits_window.destroy()

        def tutorial(): #questo spiega come funziona il gioco 
            tutorial_window = tk.Toplevel(self.root)
            tutorial_window.title("Tutorial")
            tutorial_window.geometry("400x500")
            tutorial_text = tk.Text(tutorial_window, wrap="word")
            tutorial_text.pack(expand=True, fill="both")
            credits = [
            "Hey pal, this is a simple clash royale simulator(in this case, completely f2p)",
            "",
            "If you hadn't play the original game before, try it",
            "",
            "After that, here are the general indications:",
            "Use the tast 1, 2, 3 and 4 to choose the troop",
            "after that, press the mouse to spawn it on the arena(the elixir might not be enough, so be carefull)",
            "destry the opponent's tower for victory",
            "The enemy is surely 100% human and will try stop you, good luck",
            "😁👍"
            ]
            for line in credits:
                tutorial_text.insert("end", line + "\n")
                tutorial_text.update()
                time.sleep(1)
            tutorial_text.update()
            time.sleep(6)
            tutorial_window.destroy()

        def loading():
                loading_window = tk.Toplevel(self.root)
                loading_window.title("...")
                loading_window.geometry("100x200")
                loading_text = tk.Text(loading_window, wrap="word")
                loading_text.pack(expand=True, fill="both")
                loading = [
                    "match loading...",
                    "...",
                    "done"
                ]
                for line in loading:
                    loading_text.insert("end", line + "\n")
                    loading_text.update()
                    time.sleep(1)
                loading_text.update()
                loading_window.destroy()


        def deckConfirm(): #sta roba ti crea il mazzo
            self.deck = [ "zapF","knightF", "valkyrieF", "pekkaF", "miniPekkaF", "hogRiderF", "wallBreakerF", "fireballF"]
            print("Deck confirmed as:", self.deck)

        def deleteIntro():#cancella l'introduzione 
            if self.deck == []:#sta roba controlla che tu abbia un mazzo
                print("You must edit your deck before starting the game")
                return
            else:
                self.canvas.delete(yellowSquare) #distruggi intro
                self.canvas.delete(greySquare)
                self.canvas.delete(blueSquare)
                self.canvas.delete(clashText1)
                self.canvas.delete(clashText2)
                self.canvas.delete(clashText3)
                accesButton.destroy()
                self.canvas.delete("all")
                self.canvas.pack_forget()
                loading()
                self.main()


        #creazione dei bottoni
        creditsButton = tk.Button(self.root, text="Credits", bg="grey", activebackground="grey", command=credits)
        tutorialButton = tk.Button(self.root, text="Tutorial",bg="grey", activebackground="grey", command=tutorial)
        accesButton = tk.Button(self.root, text="Click to battle", bg="yellow", activebackground="yellow",command=deleteIntro)
        deckButtom = tk.Button(self.root, text="Confirm deck",bg="light blue", activebackground="light blue", command=deckConfirm)
        #posizionamento dei bottoni
        self.canvas.create_window(225, 25, window=creditsButton)
        self.canvas.create_window(225, 60, window=tutorialButton)
        self.canvas.create_window(150, 300, window=accesButton)
        self.canvas.create_window(150, 400, window=deckButtom)



    def main(self): #sta roba ti crea la finestra di gioco, prima includeva tutto e partiva il gioco da solo, ma per colpa di Gio, ora non è più così grande
        self.canvas = tk.Canvas(self.root, width=self.width , height= self.height)
        self.canvas.pack()
        place_troop = self.GamePlay(self.deck, self.canvas, self.root)
        self.root.bind("<Key>", place_troop.choose_troop)
        self.canvas.bind("<Button-1>", place_troop.on_mouse_click)
        self.root.mainloop()
        

    #main
    class GamePlay:
        def __init__(self, deck, canvas, root): #questo implementa le  informazioni del canvas, map size e deck
            self.canvas = canvas
            self.root = root
            self.deck = deck
            self.width = 300
            self.height = 670
            self.game_manager() #comincia il gioco

        def game_manager(self): #gestisce il gioco, se provi a cambiare l'ordine delle funzioni, non parte più
            self.troop_manager() #qui stanno tutte le cose necessarie per modificare le truppe, compreso le sprites
            self.create_map() #crea la mappa
            self.update_elixir() #comincia elisir
            self.showElixirBar() # funzione per inizializarre l'elisir in modalità barra
            self.timer(3,0) #comincia il timer minuti,secondi
            self.initialize_variables() #stampa il deck e dà  l'id
            self.troop_handler() #gestisce le truppe
            




        #placca della map creation, variable implementation e troop rendering
        def initialize_variables(self):
            print(" ".join(str(self.deck[i]) for i in range(4))) #stampa prime 4 carte del mazzo
            self.troops_in_game = [] #lista delle truppe in gioco (potrebbe creare errori con matrix o valori vuoti allo start)
            self.id = 0 #id delle truppe

        def troop_manager(self):
            self.troop_stats = {  #questo implementa le statistiche delle truppe
            "knightF": {"speed": 2, "health": 100, "damage": 50, "range": 1,"type":"troop","color":"grey","size":"medium","elixir":3},
            "valkyrieF": {"speed": 2, "health": 120, "damage": 60, "range": 1,"type":"troop","color":"orange","size":"medium","elixir":4},
            "pekkaF": {"speed": 1, "health": 200, "damage": 100, "range": 1,"type":"troop","color":"black","size":"big","elixir":7},
            "miniPekkaF": {"speed": 2, "health": 150, "damage": 80, "range": 1,"type":"troop","color":"black","size":"medium","elixir":4},
            "hogRiderF": {"speed": 3, "health": 90, "damage": 70, "range": 1,"type":"troop","color":"brown","size":"medium","elixir":4},
            "wallBreakerF": {"speed": 3, "health": 50, "damage": 150, "range": 1,"type":"troop","color":"white","size":"small","elixir":2},
            "fireballF": {"speed": 0,"health": 0, "damage": 400, "range": 0,"type":"spell","color":"red","size":"superbig","elixir":4},
            "zapF": {"speed": 0, "health": 0, "damage": 200, "range": 0,"type":"spell","color":"light blue","size":"medium","elixir":2}
            }#nota: per adesso il range è irrilevante in quanto tutte le truppe sono a corpo a corpo o spell
            self.sizes={"small":10,"medium":15,"big":20,"superbig":40} #questo implementa le dimensioni delle truppe
            troop_sprites_specifics = [
            # truppe blu
            ["knight.png", [150, 300, "center"]],
            ["zap.png", [150, 300, "center"]],
            ["fireball.png", [150, 300, "center"]],
            ["hogRider.png", [150, 300, "center"]],
            ["miniPekka.png", [150, 300, "center"]],
            ["pekka.png", [150, 300, "center"]],
            ["valkyrie.png", [150, 300, "center"]],
            ["wallBreaker.png", [150, 300, "center"]],
            ]
            troop_sprites_needed = [sprite[0] for sprite in troop_sprites_specifics]
            paths = self.find_paths(troop_sprites_needed)
            if paths is None:
                return
            #crea una nuova roba ai vettori per conservare le sprites
            for sprite, path in zip(troop_sprites_needed, paths):
                troop_name = sprite.split(".")[0] + "F"
                if troop_name in self.troop_stats:
                    self.troop_stats[troop_name]["sprite_path"] = path

        def create_map(self): #image loading, canvas.create e variable loading, quindi come l'init della versione 1.1
            #ricerca e caricamento delle immagini
            textures_specifics = [
                ["battleField.png", [0, 0, "nw"]],
                ["princessTower.png", [60, 150, "center"]],  # leftPrincessTower
                ["princessTower.png", [240, 150, "center"]],  # rightPrincessTower
                ["kingTower.png", [150, 75, "center"]],  # kingTower
                ["princessTowerBlue.png", [60, 510, "center"]],  # leftPrincessTowerBlue
                ["princessTowerBlue.png", [240, 510, "center"]],  # rightPrincessTowerBlue
                ["kingTowerBlue.png", [150, 570, "center"]],  # kingTowerBlue
            ] 
            textures_nedded = [texture[0] for texture in textures_specifics]
            paths = self.find_paths(textures_nedded)
            if paths==None:
                return
            canvas = self.canvas
            canvas.pack()
            self.canvas.images = [] #salva le immagini in un array per evitare che vengano cancellate
            self.textures=[] #crea un array per conservare le texture e manipolarle in futuro
            for path, specifics in zip(paths, textures_specifics): #ridimensiona e crea le textures
                texture_name = specifics[0].split(".")[0]  # Extract the name of the texture without the file extension
                resize = (self.width, self.height) if specifics[0] == "battleField.png" else (100, 100)  # Ridimensiona le immagini in base alla grandezza del canvas
                texture_id = self.load_and_place_image(canvas, path, resize, specifics[1][:2], specifics[1][2])
                self.textures.append({"name": texture_name, "id": texture_id})  # Save the texture name and its canvas ID
            print(self.textures)
            #implementation stato delle torri(vive o morte) e la loro vita
            self.rightTowerAlive = True
            self.leftTowerAlive = True
            self.kingTowerAlive = True
            self.leftHealth = 3052
            self.leftHealthText = self.canvas.create_text(55, 100, text=str(self.leftHealth), fill="white", font=("Arial", 12))
            self.rightHealth = 3052
            self.rightHealthText = self.canvas.create_text(245, 100, text=str(self.rightHealth), fill="white", font=("Arial", 12))
            self.kingHealth = 6000
            self.kingHealthText = self.canvas.create_text(150, 15, text=str(self.kingHealth), fill="white", font=("Arial", 12))
            #copri lo sfondo e creare le caselle per mostrare le carte in mano
            self.canvas.create_rectangle(0, 600, 300, 670, fill="white")
            self.canvas.create_line(150, 625, 150, 670, fill="black")
            self.canvas.create_line(0, 647, 300, 647, fill="black")
            #carte sul tk
            firstPicked, secondPicked, thirdPicked, fourthPicked = False, False, False, False
            self.card1 = canvas.create_text(75, 635, text=(f"click 1: {self.deck[0]}:{self.troop_stats[self.deck[0]]['elixir']}"), fill="red" if firstPicked else "black", font=("Arial", 12))
            self.card2 = canvas.create_text(225, 635, text=(f"click 2: {self.deck[1]}:{self.troop_stats[self.deck[1]]['elixir']}"), fill="red" if secondPicked else "black", font=("Arial", 12))
            self.card3 = canvas.create_text(75, 660, text=(f"click 3: {self.deck[2]}:{self.troop_stats[self.deck[2]]['elixir']}"), fill="red" if thirdPicked else "black", font=("Arial", 12))
            self.card4 = canvas.create_text(225, 660, text=(f"click 4: {self.deck[3]}:{self.troop_stats[self.deck[3]]['elixir']}"), fill="red" if fourthPicked else "black", font=("Arial", 12))
            self.canvas.create_text(235, 50, text=str("time    :"), fill="black", font=("arial", 12)) #testo sul canvas del timer

        #le tre funzioni che trovano ed implementano le sprites(neanche Gio, il creatore, sarebbe in grado di spiegare come funzionano...)
        def find_paths(self, textures_nedded):
            paths_found = []
            for drive in ["/home", "/mnt", "/media", "/usr", "/opt","/tmp","J://", "I://", "H://", "G://", "F://", "E://", "D://", "C://"]: #array con tutti i drive in cui vogliamo cercare(messe dall piu piccolo al piu grande per maggiore efficienza)
                if os.path.exists(drive): #controlla se il drive esiste
                    print(f"Searching in {drive}...")
                if drive == "C://":
                    specificPath = "/home/domain/lei.zhenting/Documenti/Python/Project_CR 1.3-20260422T080209Z-3-001/Project_CR 1.3/Renderers/mainRenderers"  # percorso specifico per le texture
                    if os.path.exists(specificPath):  # controlla se il percorso specifico esiste
                        print(f"Searching in specific path: {specificPath}...")
                        pathsFound = []  # Define pathsFound
                        texturesNeeded = textures_nedded  # Assign texturesNeeded from textures_nedded
                        for texture in texturesNeeded:  # ripete il procedimento per tutte le texture che ci servono
                            path = self.texture_finder(texture, specificPath)  # Use self.texture_finder
                            if path:
                                pathsFound.append(path)  # aggiunge la directory alla lista di directory trovate
                                print(f"textures found:({len(pathsFound)}/{len(texturesNeeded)}){texture, path}")
                            if len(pathsFound) == len(texturesNeeded):  # se ha trovato tutte le texture
                                print("All textures found.")
                                return pathsFound
                        print(f"No textures found in {specificPath}")
                    for texture in textures_nedded: #ripete il procedimento per tutte le texture che ci servono
                        path=self.texture_finder(texture, drive)
                        if path:  
                            paths_found.append(path) #se trova una texture che ci serve aggiunge la directory alla lista di directory trovate  
                            print(f"textures found:({len(paths_found)}/{len(textures_nedded)}){texture,path}")
                            time.sleep(0)
                        if len(paths_found) == len(textures_nedded): #se ha trovato tutte le texture
                            print("All textures found.")
                            time.sleep(0)
                            return paths_found
                    if len(paths_found) == 0:
                        print(f"None of the textures were found in {drive}.")
                        time.sleep(0)
                else:
                    time.sleep(0)
                    print(f"directory '{drive}' does not exist") #se la directory non esiste manda un feedback
            risposta = messagebox.askyesno("Conferma", "Non tutte le texture sono state trovate vuoi continuare lo stesso?")
            if risposta:
                return paths_found #fa partire il gioco con le texture trovate
            return None
        def texture_finder(self,texture_to_find, drive):
            try:
                for root, _, files in os.walk(drive, topdown=True):
                    if texture_to_find in set(files):  # Convert to set for faster lookup
                        return os.path.join(root, texture_to_find)
            except PermissionError:
                pass  # Skip directories without permission
            return None
        def load_and_place_image(self,canvas, path, resize_dims, position, anchor): #formatta le immagini e le piazza dove sono necessarie basandosi sui valori di textures_specifics
            try:
                image = Image.open(path)
            except FileNotFoundError:
                print(f"Error: File not found at path {path}")
                return None
            except Exception as e:
                print(f"Error: Unable to open image at path {path}. Exception: {e}")
                return None
            resized_image = image.resize(resize_dims)
            tk_image = ImageTk.PhotoImage(resized_image)
            id=self.canvas.create_image(*position, image=tk_image, anchor=anchor) #crea limmagine sul canvas
            self.canvas.images.append(tk_image) #salva limmagine per evitare che loggetto si corrompa
            return id #restituisce limmagine prontaper essere usata

        


        #Placca dell'eisir e timer
        def update_elixir(self): #questo serve per aggiornare l'elixir
            try:
                try:
                    self.canvas.delete(self.elixir_text)
                except AttributeError:
                    #non si sa perchè ma al primo shot c'è un vuoto del elixir text di 2.8 secondi, usiamolo per far uno scherzo...
                    self.elixir_text = self.canvas.create_text(145, 590, text=str("int main() elixir loading.........\n*****'attribute error'***** possible"), fill="black", font=("Arial", 12))
                self.elixir += 1
                if self.elixir > 10:
                    self.elixir = 10
                self.elixir_text = self.canvas.create_text(145, 590, text=f"current elixir: {self.elixir}", fill="black", font=("Arial", 12))
            except AttributeError:
                self.elixir= 6
            self.canvas.after(2800, self.update_elixir)

        def remove_elixir(self,remove): #rimuove l'elisir e controlla che tu possa farlo
            if (self.elixir - remove>=0):
                self.elixir -= remove
                self.canvas.delete(self.elixir_text)
                self.elixir_text = self.canvas.create_text(145, 590, text=f"current elixir: {self.elixir}", fill="black", font=("Arial", 12))
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

        def timer(self,minuti,secondi): #questo serve per aggiornare l'elixir
            self.min = minuti
            self.sec = secondi
            try:
                self.canvas.delete(self.minText)
                self.canvas.delete(self.secText)
            except AttributeError: #se c'è un errore, pazienza
                pass
            if self.sec>0:
                self.sec -= 1
            else:
                self.sec = 60
                self.min -= 1 
            if self.min < 0:
                self.min = 0
                self.sec = 0
                self.end_game()
            self.minText = self.canvas.create_text(250, 50, text=str(self.min), fill="black", font=("arial", 12))
            self.secText = self.canvas.create_text(270, 50, text=str(self.sec), fill="black", font=("arial", 12))
            self.canvas.after(1000, lambda: self.timer(self.min, self.sec)) #questo aggiorna il timer ogni secondo




        #placca del troop system(al momento disable perchè completamente rubato dal 1.1 senza modifiche o ottimizzazioni al nuovo ambiente)
        def on_mouse_click(self, event): #questo serve per prendere le coordinate del click dove piazzare le truppe
            if self.key in [1, 2, 3, 4]: #controlla che tu abbia premuto un tasto valido
                self.x_mouse_click = event.x #salva x del click per dopo
                self.y_mouse_click = event.y #salva y del click per dopo
                self.spawn_troop(self.key)

        def choose_troop(self, event): #scegliere che truppa delle 4 piazzare
            self.key = int(event.keysym) if event.keysym in ["1", "2", "3", "4"] else None
            if self.key:
                selected_card = [self.card1, self.card2, self.card3, self.card4]
                for i, card in enumerate(selected_card, start=1):
                    self.canvas.itemconfig(card, fill="red" if self.key == i else "black")

        def spawn_troop(self, key): #questo tiene la logica per ciclare il mazzo e printaremnuove carte
            try:
                if self.y_mouse_click < 330 and self.troop_stats[self.deck[key-1]]["type"] == "troop":
                    print("You can't place troops here")
                    return
                if self.remove_elixir(self.troop_stats[self.deck[key-1]]["elixir"]):
                    print("spawned:", self.deck[key-1])
                    self.deck.append(self.deck[key-1])
                    self.troop_specific_stats = self.troop_stats[self.deck[key-1]]
                    self.deck.pop(key-1)
                    print(" ".join(str(self.deck[i]) for i in range(4)))
                    self.initiate_troop(self.troop_specific_stats["speed"],self.troop_specific_stats["health"], self.troop_specific_stats["damage"], self.troop_specific_stats["type"], self.troop_specific_stats["color"], self.troop_specific_stats["size"],self.troop_specific_stats["elixir"], self.id)
                    self.canvas.delete(self.card1, self.card2, self.card3, self.card4)
                    self.canvas.create_line(0, 647, 300, 647, fill="black")
                    self.card1 = self.canvas.create_text(75, 635, text=(f"click 1: {self.deck[0]}:{self.troop_stats[self.deck[0]]['elixir']}"), fill="black", font=("Arial", 12))
                    self.card2 = self.canvas.create_text(225, 635, text=(f"click 2: {self.deck[1]}:{self.troop_stats[self.deck[1]]['elixir']}"), fill="black", font=("Arial", 12))
                    self.card3 = self.canvas.create_text(75, 660, text=(f"click 3: {self.deck[2]}:{self.troop_stats[self.deck[2]]['elixir']}"), fill="black", font=("Arial", 12))
                    self.card4 = self.canvas.create_text(225, 660, text=(f"click 4: {self.deck[3]}:{self.troop_stats[self.deck[3]]['elixir']}"), fill="black", font=("Arial", 12))
                else:
                    print("Not enough elixir")
            except AttributeError:
                print("You must click on the map to place a troop")
                return

        def initiate_troop(self,speed, health, damage, type, color, size, cost , id): #questo piazza effetivamente la truppa sul canvass
            x_position = self.x_mouse_click
            y_position = self.y_mouse_click
            x0 = x_position - self.sizes[size]
            y0 = y_position - self.sizes[size]
            x1 = x_position + self.sizes[size]
            y1 = y_position + self.sizes[size]
            #5 righe per creare l'immagine sul canvas
            troop_sprite = Image.open(self.troop_specific_stats["sprite_path"])
            troop_sprite_resized = troop_sprite.resize((self.sizes[size] * 5, self.sizes[size] * 5))
            troop_sprite_tk = ImageTk.PhotoImage(troop_sprite_resized)
            troop_id = self.canvas.create_image(x_position, y_position, image=troop_sprite_tk, tags=id)
            self.canvas.images.append(troop_sprite_tk)  # Prevent garbage collection of the image
            if type == "troop":
                if y_position < 330: #controlla che non piazzi truppe sopra il ponte
                    self.troops_in_game.append([troop_id, int(x_position), int(y_position), int(health),int(damage),int(speed),(type)])
                    print("placment non")
                else:
                    self.troops_in_game.append([troop_id, int(x_position), int(y_position), int(health),int(damage),int(speed),(type)])
            elif type == "spell":
                self.damage_troops_on_tower(x0, y0, x1, y1, damage)
                self.canvas.after(1000, lambda: self.canvas.delete(troop_id)) #se è una spell fa il danno e poi la cancella
            self.id += 1 #aumenta lid per la prossima truppa
        
        #deletta le truppe morte e muove quelle vive
        def troop_handler(self):
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

        def troop_mover(self):
            if not self.troops_in_game:  # If there are no troops, do nothing
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
                            self.damage_troops_on_tower(x_position - 45, y_position-10, x_position, y_position + 10, troop[4])
                        
                elif 150 >= x_position > 55 or x_position > 246:
                    if y_position > 160:
                        x_position -= speed
                        self.canvas.move(id, -speed, 0)
                    else:
                        if x_position<110:
                            x_position += speed
                            self.canvas.move(id, speed, 0)
                        else:
                            self.damage_troops_on_tower(x_position, y_position-10, x_position+45, y_position + 10, troop[4])
                else:
                    if y_position > 160:
                        y_position -= speed
                        self.canvas.move(id, 0, -speed)
                    else:
                        if x_position < 150:
                            if self.leftTowerAlive:
                                self.damage_troops_on_tower(x_position - 10, y_position, x_position + 10, y_position + 20, troop[4])
                            else:
                                if y_position>50:
                                    y_position -= speed
                                    self.canvas.move(id, 0, -speed)
                                else:
                                    x_position += speed
                                    self.canvas.move(id, speed, 0)
                        else:
                            if self.rightTowerAlive:
                                self.damage_troops_on_tower(x_position - 10, y_position, x_position + 10, y_position + 20, troop[4])
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

        def damage_troops_on_tower(self, x0, y0, x1, y1, damage): #questo fa il danno alle torri
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

        def update_healths(self):
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
                root.after(2000, self.end_game)
        

        #gioco finito
        def end_game(self):
            self.canvas.delete("all")
            self.root.destroy()
                




if __name__ == "__main__":#questo fa partire il gioco
    root = tk.Tk()
    app = ClashRoyaleApp(root)
    root.mainloop()