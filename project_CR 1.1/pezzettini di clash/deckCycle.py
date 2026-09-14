import tkinter as tk

# crea il canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

def main():
    deck = ["knightF", "valkyrieF", "pekkaF", "mini_pekka_f", "hogRiderF", "wallBreakerF", "berserkelF", "goblinGangF"]
    print(deck[0], deck[1], deck[2], deck[3])

    class PlaceTroop:
        def __init__(self, deck, event, key):
            self.deck = deck
            self.event = event
            self.key = key

        def chooseTroop(self, event):
            if event.keysym in ["1", "2", "3", "4"]:
                self.spawnTroop(int(event.keysym))

        def spawnTroop(self, key):
            key -= 1
            print("card placed:", self.deck[key])
            self.deck.append(self.deck[key])
            self.deck.pop(key)
            print(" ".join(str(self.deck[i]) for i in range(4)))

    place_troop = PlaceTroop(deck, None, None)

    def changeCard(cardIndex):
        print(f"Card {cardIndex + 1} used: {deck[cardIndex]}")
        deck.append(deck[cardIndex])
        deck.pop(cardIndex)
        print(" ".join(str(deck[i]) for i in range(4)))

    button1 = tk.Button(root, text="card1", bg="yellow", activebackground="yellow", command=lambda: changeCard(0))
    button2 = tk.Button(root, text="card2", bg="light blue", activebackground="blue", command=lambda: changeCard(1))
    button3 = tk.Button(root, text="card3", bg="grey", activebackground="grey", command=lambda: changeCard(2))
    button4 = tk.Button(root, text="card4", bg="green", activebackground="green", command=lambda: changeCard(3))

    canvas.create_window(50, 100, window=button1)
    canvas.create_window(100, 100, window=button2)
    canvas.create_window(150, 100, window=button3)
    canvas.create_window(200, 100, window=button4)

    root.bind("<Key>", place_troop.chooseTroop)
    root.mainloop()

main()