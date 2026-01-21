# Il deck(tanky deck) e il ciclo di carte

import tkinter as tk

tanky_deck = ["knight", "valkyrie", "pekka", "mini_pekka", "lumberjack_unraged", "elite_barbs", "giant_skelly_unbombed", "miner"]

def card_cycle(event):
    


    if event.keysym == "1":
        tanky_deck.append(tanky_deck[0])
        tanky_deck.pop(0)

        

    elif event.keysym == "2":
        tanky_deck.append(tanky_deck[1])
        tanky_deck.pop(1)


    elif event.keysym == "3":
        tanky_deck.append(tanky_deck[2])
        tanky_deck.pop(2)

        

    elif event.keysym == "4":
        tanky_deck.append(tanky_deck[3])
        tanky_deck.pop(3)

    
    print(f" {tanky_deck[0]}\n {tanky_deck[1]}\n {tanky_deck[2]}\n {tanky_deck[3]}\n")
    
        

root = tk.Tk()
root.bind("<Key>", card_cycle)
root.mainloop()