# CanvasManager.py
# In verità l'obbiettivo era di spezzare il codice del 1.2 in diversi script e runnarli in _Main.py, ma a quanto pare è tutta una istanza di CanvasManager
import tkinter as tk
import time
import os
import Troop as Troop
from PIL import Image, ImageTk

class Canvas:
    def __init__(self, troop, sprites):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=300, height=700)
        # store width/height for later use (create_map expects these)
        self.width = int(self.canvas['width'])
        self.height = int(self.canvas['height'])
        self.canvas.pack()
        self.deckMain = ["zapF", "knightF", "valkyrieF", "pekkaF",
            "miniPekkaF", "hogRiderF", "wallBreakerF", "fireballF"]

        self.intros()
        

        self.troopStats = troop.troopStats 
        self.sizes = troop.sizes

        self.sprites = sprites.images
        self._link_sprites()  # ← add this

        self.root.bind("<Key>", self.choose_troop)
        self.canvas.bind("<Button-1>", self.on_mouse_click)

        print("Canvas initialized")
        print("Chiunque abbia fatto scritto i commenti di project CR 1.2 deve suicidarsi")

    # [SerializeField] private Gameobject self;
    def stateItself(self, canvas):
        self.canvasSelf = canvas
        print(self.canvasSelf)
        
    def intros(self): #l'introduzione del gioco(homepage)
        self.clear()
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
            if len(self.deckMain) <8:   #sta roba controlla che tu abbia un mazzo
                print("You must edit a valid deck before starting the game")
                return
            else:
                self.canvas.delete(yellowSquare) #distruggi intro
                self.canvas.delete(greySquare)
                self.canvas.delete(blueSquare)
                self.canvas.delete(clashText1)
                self.canvas.delete(clashText2)
                accesButton.destroy()
                controllButton.destroy()
                self.clear()
                self.canvas.pack_forget()
                self.GameManager()
        
        def deck_edit(): #sta roba ti crea il mazzo
            self.deck = [ "zapF","knightF", "valkyrieF", "pekkaF", "mini_pekka_f", "hogRiderF", "wallBreakerF", "fireballF"]
            self.editDeck()

        # bottoni
        accesButton = tk.Button(self.root, text="Click to battle", bg="yellow", activebackground="yellow",command=delete_intro)
        controllButton = tk.Button(self.root, text="Edit Deck",bg="light blue", activebackground="blue", command=deck_edit)
        creditsButton = tk.Button(self.root, text="Edit controlls", bg="grey", activebackground="grey", command=credits)
        self.canvas.create_window(150, 400, window=controllButton)
        self.canvas.create_window(150, 300, window=accesButton)
        self.canvas.create_window(225, 50, window=creditsButton) #questo crea i bottoni


    def editDeck(self):
        self.clear()

        self.deck = self.deckMain.copy()
        
        troops = [
            "zapF", "knightF", "valkyrieF", "pekkaF",
            "miniPekkaF", "hogRiderF", "wallBreakerF", "fireballF",
            "archerF", "giantF", "witchF", "skeletonF",
            "bomberF", "musketeerF", "dragonF", "goblinF"
        ]
        
        deck_text = self.canvas.create_text(150, 20, text=f"Deck:" f"{len(self.deckMain)}/8", fill="black", font=("Arial", 12))
        deck_display = self.canvas.create_text(150, 45, text=", ".join(self.deck), fill="black", font=("Arial", 9))

        def add_to_deck(troop, btn):
            if len(self.deck) >= 8:
                print("Deck pieno!")
                return
            if troop in self.deck:
                print(f"{troop} già nel deck")
                return
            self.deck.append(troop)
            btn.config(bg="grey", state="disabled")
            self.deckMain = self.deck
            self.canvas.itemconfig(deck_text, text=f"Deck: {len(self.deck)}/8")
            self.canvas.itemconfig(deck_display, text=", ".join(self.deck))
            print("Deck:", self.deck)

        # griglia 4x4 di bottoni
        for i, troop in enumerate(troops):
            row = i // 4
            col = i % 4
            x = 40 + col * 70
            y = 80 + row * 50
            btn = tk.Button(self.root, text=troop, font=("Arial", 7), width=8, bg="light blue")
            btn.config(command=lambda t=troop, b=btn: add_to_deck(t, b))
            if troop in self.deckMain:  # se la truppa è già nel deck, disabilita subito
                btn.config(bg="grey", state="disabled")
            self.canvas.create_window(x, y, window=btn)

        returnButton = tk.Button(self.root, text="Return", bg="light blue", activebackground="blue", command=lambda: self.turnBack(self.intros))
        self.canvas.create_window(150, 600, window=returnButton)


    
    def turnBack(self, function):
        self.clear()
        function()
    
    def clear(self):
        self.canvas.delete("all")

    def run(self):
        self.root.mainloop()

    def GameManager(self):
        self.createMap()
        self.CreateUI()
        self.update_elixir() #comincia elisir
        self.showElixirBar() # funzione per inizializarre l'elisir in modalità barra
        self.timer(3,0) #comincia il timer. minuti,secondi
        self.TroopManager()

    def TroopManager(self):
        self.x_mouse_click = 0
        self.y_mouse_click = 0
        self.selected_card = [self.deckMain[0], self.deckMain[1], self.deckMain[2], self.deckMain[3]]
        firstPicked, secondPicked, thirdPicked, fourthPicked = False, False, False, False
        self.card1 = self.canvas.create_text(75, 660, text=(f"click 1: {self.deckMain[0]}:{self.troopStats[self.deckMain[0]]['elixir']}"), fill="black", font=("Arial", 12))
        self.card2 = self.canvas.create_text(225, 660, text=(f"click 2: {self.deckMain[1]}:{self.troopStats[self.deckMain[1]]['elixir']}"), fill="black", font=("Arial", 12))
        self.card3 = self.canvas.create_text(75, 690, text=(f"click 3: {self.deckMain[2]}:{self.troopStats[self.deckMain[2]]['elixir']}"), fill="black", font=("Arial", 12))
        self.card4 = self.canvas.create_text(225, 690, text=(f"click 4: {self.deckMain[3]}:{self.troopStats[self.deckMain[3]]['elixir']}"), fill="black", font=("Arial", 12))

    def createMap(self): #image loading, canvas.create e variable loading, quindi come l'init della versione 1.1
            # ricerca e caricamento delle immagini
            # NOTE: RenderingManager provides a dict of lists in self.sprites
            textures_specifics = [
                ["battleField.png", [0, 0, "nw"]],
                ["princessTower.png", [60, 155, "center"]],  # leftPrincessTower
                ["princessTower.png", [240, 155, "center"]],  # rightPrincessTower
                ["kingTower.png", [150, 75, "center"]],  # kingTower
                ["princessTowerBlue.png", [60, 535, "center"]],  # leftPrincessTowerBlue
                ["princessTowerBlue.png", [240, 535, "center"]],  # rightPrincessTowerBlue
                ["kingTowerBlue.png", [150, 570, "center"]],  # kingTowerBlue
            ] 
            # Build a flattened list of available image paths from the provided sprites
            available_paths = []
            if isinstance(self.sprites, dict):
                for lst in self.sprites.values():
                    if isinstance(lst, (list, tuple)):
                        available_paths.extend(lst)
            elif isinstance(self.sprites, (list, tuple)):
                available_paths.extend(self.sprites)

            canvas = self.canvas
            canvas.pack()
            self.canvas.images = []  # keep references to PhotoImage objects
            self.textures = []  # store texture info

            for specifics in textures_specifics:
                filename = specifics[0]
                texture_name = filename.split('.')[0]
                # find the first available path matching the filename
                found_path = None
                for p in available_paths:
                    try:
                        if os.path.basename(p) == filename:
                            found_path = p
                            break
                    except Exception:
                        continue
                if not found_path:
                    print(f"Warning: texture '{filename}' not found in provided sprites")
                    continue

                # resize battlefield to canvas size, others to default 100x100
                resize = (self.width, self.height) if filename == "battleField.png" else (100, 100)
                try:
                    image = Image.open(found_path)
                    resized = image.resize(resize)
                    tk_image = ImageTk.PhotoImage(resized)
                except Exception as e:
                    print(f"Error loading image {found_path}: {e}")
                    continue

                pos = specifics[1][:2]
                anchor = specifics[1][2] if len(specifics[1]) > 2 else 'center'
                try:
                    tex_id = canvas.create_image(*pos, image=tk_image, anchor=anchor)
                except Exception as e:
                    print(f"Error placing image on canvas: {e}")
                    continue

                self.canvas.images.append(tk_image)
                self.textures.append({"name": texture_name, "id": tex_id, "path": found_path})

            print(self.textures)
            
            

    def CreateUI(self):
        # implementation stato delle torri (vive o morte) e la loro vita
        # Non sono sicuro perchè la funzione fu riscritta da Copilot sosì lunga, ma se funziona non toccare

        # Red towers (legacy names kept as aliases for compatibility)(tecnica speciale che fonde snake_case con camelCase)
        self.red_rightTowerAlive = True
        self.red_leftTowerAlive = True
        self.red_kingTowerAlive = True

        # Update red tower stats here. If you want different numbers, edit these values.
        self.red_leftHealth = 3052
        self.red_rightHealth = 3052
        self.red_kingHealth = 6000

        # Keep legacy attribute names pointing to red towers for backwards compatibility
        self.leftTowerAlive = self.red_leftTowerAlive
        self.rightTowerAlive = self.red_rightTowerAlive
        self.kingTowerAlive = self.red_kingTowerAlive
        self.leftHealth = self.red_leftHealth
        self.rightHealth = self.red_rightHealth
        self.kingHealth = self.red_kingHealth

        # Canvas background for red tower health (so text is readable)
        self.red_leftHealthBg = self.canvas.create_rectangle(30, 105, 90, 125, fill="#ff6767")
        self.red_rightHealthBg = self.canvas.create_rectangle(215, 105, 275, 125, fill="#ff6767")
        self.red_kingHealthBg = self.canvas.create_rectangle(120, 5, 180, 25, fill="#ff6767")
        # Canvas text for red towers (top of the arena)
        self.leftHealthText = self.canvas.create_text(60, 115, text=str(self.leftHealth), fill="black", font=("Arial", 12))
        self.rightHealthText = self.canvas.create_text(245, 115, text=str(self.rightHealth), fill="black", font=("Arial", 12))
        self.kingHealthText = self.canvas.create_text(150, 15, text=str(self.kingHealth), fill="black", font=("Arial", 12))

        # L'UI delle truppe blu
        # Blue towers (enemy/other side) - mirror stats by default; you can tune separately
        self.blue_rightTowerAlive = True
        self.blue_leftTowerAlive = True
        self.blue_kingTowerAlive = True
        self.blue_leftHealth = 3052
        self.blue_rightHealth = 3052
        self.blue_kingHealth = 6000

        # Copri lo sfondo del healthText
        self.blue_leftHealthBg = self.canvas.create_rectangle(30, 530, 90, 550, fill="#93cdff")
        self.blue_rightHealthBg = self.canvas.create_rectangle(215, 530, 275, 550, fill="#87c1f3")
        self.blue_kingHealthBg = self.canvas.create_rectangle(120, 580, 180, 600, fill="#8dc3f3")
        # Positions chosen to match the tower textures placed in createMap
        self.leftHealthBlueText = self.canvas.create_text(60, 540, text=str(self.blue_leftHealth), fill="black", font=("Arial", 12))
        self.rightHealthBlueText = self.canvas.create_text(245, 540, text=str(self.blue_rightHealth), fill="black", font=("Arial", 12))
        self.kingHealthBlueText = self.canvas.create_text(150, 590, text=str(self.blue_kingHealth), fill="black", font=("Arial", 12))

        # copri lo sfondo e creare le caselle per mostrare le carte in mano
        self.cardAreaBg = self.canvas.create_rectangle(0, 650, 300, 700, fill="white")
        self.cardAreaSeparator = self.canvas.create_line(150, 650, 150, 700, fill="black")
        self.cardAreaTopLine = self.canvas.create_line(0, 630, 300, 630, fill="black")
        self.cardAreaBottomLine = self.canvas.create_line(0, 675, 300, 675, fill="black")

        # Anche per il timer: background and initial texts
        # create a persistent background so timer text stays readable
        self.timerBg = self.canvas.create_rectangle(255, 0, 300, 30, fill="white")
        self.canvas.create_text(278, 10, text=":", fill="black", font=("Arial", 12))
        # initial minute/second text (GameManager starts timer with timer(3,0))
        self.minText = self.canvas.create_text(270, 10, text=str(3), fill="black", font=("arial", 12))
        self.secText = self.canvas.create_text(290, 10, text=str(0), fill="black", font=("arial", 12))

        # troop system state (ported from OldClash1,2)
        self.troops_in_game = []  # each entry: [canvas_id, x, y, health, damage, speed, type]
        self.id = 0

        # attempt to map tower canvas IDs from self.textures (order is the same as create_map's textures_specifics)
        try:
            # textures: [battleField, leftPrincess, rightPrincess, kingTower, leftPrincessBlue, rightPrincessBlue, kingTowerBlue]
            self.leftPrincessTower = self.textures[1]['id']
            self.rightPrincessTower = self.textures[2]['id']
            self.kingTower = self.textures[3]['id']
            self.leftPrincessTowerBlue = self.textures[4]['id']
            self.rightPrincessTowerBlue = self.textures[5]['id']
            self.kingTowerBlue = self.textures[6]['id']
        except Exception:
            # fallback to None if textures missing
            print("fellbacked to None")
            self.leftPrincessTower = None
            self.rightPrincessTower = None
            self.kingTower = None
            self.leftPrincessTowerBlue = None
            self.rightPrincessTowerBlue = None
            self.kingTowerBlue = None


    #Placca dell'eisir e timer
    def update_elixir(self): #questo serve per aggiornare l'elixir
        try:
            try:
                self.canvas.delete(self.elixir_text)
            except AttributeError:
                self.elixir_text = self.canvas.create_text(145, 623, text=str("current elixir: 6"), fill="black", font=("Arial", 12))
            self.elixir += 1
            if self.elixir > 10:
                self.elixir = 10
            self.elixir_text = self.canvas.create_text(145, 623, text=f"current elixir: {self.elixir}", fill="black", font=("Arial", 12))
        except AttributeError:
            self.elixir= 6
        self.canvas.after(2800, self.update_elixir)

    def remove_elixir(self,remove): #rimuove l'elisir e controlla che tu possa farlo
        if (self.elixir - remove>=0):
            self.elixir -= remove
            self.canvas.delete(self.elixir_text)
            self.elixir_text = self.canvas.create_text(145, 623, text=f"current elixir: {self.elixir}", fill="black", font=("Arial", 12))
            return True
        else:
            return False
    
    def showElixirBar(self): #questo serve per mostrare l'elisir in modalità barra
        try:
            self.canvas.delete(self.elixirUI)
        except AttributeError:
            pass
        self.elixirUI = self.canvas.create_rectangle(0, 630, 30*self.elixir, 650, fill="purple")
        for line in range(10):
            self.canvas.create_line(30*line, 630, 30*line, 650, fill="black")
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
        self.minText = self.canvas.create_text(270, 10, text=str(self.min), fill="black", font=("arial", 12))
        self.secText = self.canvas.create_text(290, 10, text=str(self.sec), fill="black", font=("arial", 12))
        self.canvas.after(1000, lambda: self.timer(self.min, self.sec)) #questo aggiorna il timer ogni secondo


    def on_mouse_click(self, event):
        try:
            if self.key in [1, 2, 3, 4]:
                self.x_mouse_click = event.x
                self.y_mouse_click = event.y
                if self.y_mouse_click < 330 and self.troopStats[self.deckMain[self.key-1]]["type"] == "troop":
                    print("You can't place troops here")
                    return
                if self.remove_elixir(self.troopStats[self.deckMain[self.key-1]]["elixir"]):
                    troop_name = self.deckMain[self.key-1]  # save before cycling
                    self.DeckCycle(troop_name, (self.key-1)) # ← was self.deckMain[self.key]
                    self.spawnTroop(troop_name, self.x_mouse_click, self.y_mouse_click)
                else: print("No enough elixir")
        except Exception as error:
            print(error)

    def choose_troop(self, event): #scegliere che truppa delle 4 piazzare
        self.key = int(event.keysym) if event.keysym in ["1", "2", "3", "4"] else None
        if self.key:
            selected_card = [self.card1, self.card2, self.card3, self.card4]
            for i, card in enumerate(selected_card, start=1):
                self.canvas.itemconfig(card, fill="red" if self.key == i else "black")

    def DeckCycle(self, card, order): #Cicla le carte del deck. Porta la usata in fondo e sostituisce con la 5a carta del deck
        print("spawned:", card)
        print(self.deckMain)
        self.deckMain.append(self.deckMain[order])   # append the played card to the back
        self.deckMain[order] = self.deckMain[4]      # replace its slot with the 5th card
        self.deckMain.pop(4)
        print(" ".join(str(self.deckMain[i]) for i in range(4)))
        self.canvas.delete(self.card1, self.card2, self.card3, self.card4)
        self.canvas.create_line(0, 647, 300, 647, fill="black")
        self.card1 = self.canvas.create_text(75, 660, text=(f"click 1: {self.deckMain[0]}:{self.troopStats[self.deckMain[0]]['elixir']}"), fill="black", font=("Arial", 12))
        self.card2 = self.canvas.create_text(225, 660, text=(f"click 2: {self.deckMain[1]}:{self.troopStats[self.deckMain[1]]['elixir']}"), fill="black", font=("Arial", 12))
        self.card3 = self.canvas.create_text(75, 690, text=(f"click 3: {self.deckMain[2]}:{self.troopStats[self.deckMain[2]]['elixir']}"), fill="black", font=("Arial", 12))
        self.card4 = self.canvas.create_text(225, 690, text=(f"click 4: {self.deckMain[3]}:{self.troopStats[self.deckMain[3]]['elixir']}"), fill="black", font=("Arial", 12))


    def spawnTroop(self, name, x, y):
        stats = self.troopStats[name]
        print(f"sprite_path for {name}:", stats.get("sprite_path", "MISSING"))  # ← debug
        troop = Troop.Troop(self.canvas, stats, self.sizes, x, y, name, self.id, stats["speed"], 0, self.canvasSelf)
        self.troops_in_game.append(troop)
        self.id += 1



    def troop_mover(self):
        return
        for troop in self.troops_in_game:
            x = troop.x
            y = troop.y
            speed = troop.speed

            if 245 > x > 150 or x < 54:
                if y > 160:
                    troop.move(speed, 0)
                else:
                    if x > 190:
                        troop.move(-speed, 0)
                    else:
                        self.damage_tower(x - 45, y - 10, x, y + 10, troop.damage)

            elif 150 >= x > 55 or x > 246:
                if y > 160:
                    troop.move(-speed, 0)
                else:
                    if x < 110:
                        troop.move(speed, 0)
                    else:
                        self.damage_tower(x, y - 10, x + 45, y + 10, troop.damage)

            else:
                if y > 160:
                    troop.move(0, -speed)
                else:
                    if x < 150:
                        if self.leftTowerAlive:
                            self.damage_tower(x - 10, y, x + 10, y + 20, troop.damage)
                        else:
                            if y > 50:
                                troop.move(0, -speed)
                            else:
                                troop.move(speed, 0)
                    else:
                        if self.rightTowerAlive:
                            self.damage_tower(x - 10, y, x + 10, y + 20, troop.damage)
                        else:
                            if y > 50:
                                troop.move(0, -speed)
                            else:
                                troop.move(-speed, 0)

    def damage_tower(self, x0, y0, x1, y1, damage, troopType, cooldown, neededCooldown, troopId):
        if cooldown<=neededCooldown:
            return
        if troopType == "troop":
            if x0 > 200 and self.red_rightTowerAlive:
                self.red_rightHealth -= damage
            if x0 <= 100 and self.red_leftTowerAlive:
                self.red_leftHealth -= damage
            if y1 <= 110 and self.red_kingTowerAlive:
                self.red_kingHealth -= damage
        elif troopType == "spell":
            x = self.x_mouse_click
            y = self.y_mouse_click
            # Right Princess Tower bounds based on createMap positioning
            if 150 < x < 275 and 75 < y < 150 and self.red_rightTowerAlive:
                self.red_rightHealth -= damage
            # Left Princess Tower bounds based on createMap positioning
            if 20 < x < 75 and 75 < y < 150 and self.red_leftTowerAlive:
                self.red_leftHealth -= damage
            # King Tower bounds based on createMap positioning
            if 100 < x < 200 and 25 < y < 125 and self.red_kingTowerAlive:
                self.red_kingHealth -= damage

        self.update_healths()
        if troopId is not None:
            for t in self.troops_in_game:
                if t.id == troopId:
                    t.attackCooldown = 0
                    break

    def update_healths(self):
        self.canvas.itemconfig(self.leftHealthText, text=str(self.red_leftHealth))
        self.canvas.itemconfig(self.rightHealthText, text=str(self.red_rightHealth))
        self.canvas.itemconfig(self.kingHealthText, text=str(self.red_kingHealth))

        if self.red_leftHealth <= 0 and self.red_leftTowerAlive:
            self.red_leftTowerAlive = False
            self.leftTowerAlive = False
            self.canvas.delete(self.leftPrincessTower)
            self.canvas.delete(self.leftHealthText, self.red_leftHealthBg)

        if self.red_rightHealth <= 0 and self.red_rightTowerAlive:
            self.red_rightTowerAlive = False
            self.rightTowerAlive = False
            self.canvas.delete(self.rightPrincessTower)
            self.canvas.delete(self.rightHealthText, self.red_rightHealthBg)

        if self.red_kingHealth <= 0 and self.red_kingTowerAlive:
            self.red_kingTowerAlive = False
            self.canvas.delete(self.kingTower)
            self.canvas.delete(self.kingHealthText, self.red_kingHealthBg)
            self.canvas.after(2000, self.end_game)

    def end_game(self):
        self.canvas.delete("all")
        self.root.destroy()

    def _link_sprites(self):
        all_paths = []
        for paths in self.sprites.values():
            all_paths.extend(paths)

        path_by_filename = {}
        for path in all_paths:
            filename = os.path.basename(path)
            path_by_filename[filename] = path

        for troop_name, stats in self.troopStats.items():
            # strip only the trailing "F", not any F inside the name
            base = troop_name[:-1] if troop_name.endswith("F") else troop_name
            base = base[0].lower() + base[1:]
            filename = base + ".png"
            if filename in path_by_filename:
                stats["sprite_path"] = path_by_filename[filename]
                print(f"Linked: {troop_name} → {stats['sprite_path']}")
            else:
                print(f"Warning: no sprite found for {troop_name} (looked for '{filename}')")
