import tkinter as tk

class pizzeria:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.gameManager()

    def gameManager(self):
        self.createMap()
        self.buttons()

    def createMap(self):
        self.root.title("Bonnie's Pizzeria simulator") #titolo
        #creazione delle varie stanze
        self.kitchen = self.canvas.create_rectangle(650, 375, 800, 475, fill="yellow")
        self.gamingRoom = self.canvas.create_rectangle(225, 375, 375, 475, fill="lightyellow")
        self.pirateCove = self.canvas.create_rectangle(250, 275, 450, 325, fill="lightpink")
        self.showStage = self.canvas.create_rectangle(450, 150, 550, 200, fill="lightgrey")
        self.personalOffice = self.canvas.create_rectangle(250, 150, 350, 200, fill="lightgreen")
        self.bathroom = self.canvas.create_rectangle(425, 400, 500, 450, fill="lightgrey")
        self.diningRoom = self.canvas.create_rectangle(300, 200, 700, 400, fill="lightblue")
        #the names of the rooms
        self.canvas.create_text(500, 300, text="Dining Room", font=("Arial", 12))
        self.canvas.create_text(500, 175, text="Show Stage", font=("Arial", 12))
        self.canvas.create_text(250, 300, text="Pirate Cove", font=("Arial", 12))
        self.canvas.create_text(300, 425, text="Gaming Room", font=("Arial", 12))
        self.canvas.create_text(300, 175, text="Personal Office", font=("Arial", 12))
        self.canvas.create_text(450, 425, text="Bathroom", font=("Arial", 12))
        self.canvas.create_text(725, 425, text="Kitchen", font=("Arial", 12))


    def buttons(self):
        #creazione bottoni
        self.upgradeButton = tk.Button(self.root, text="Upgrade pizzeria", command=lambda: print("Game started!"))
        self.workerbutton = tk.Button(self.root, text="find workers", command=lambda: print("Game started!"))
        self.showStageButton = tk.Button(self.root, text="activate show stage", command=lambda: print("Game started!"))
        self.statsButton = tk.Button(self.root, text="see the pizzeria's stats", command=lambda: print("Game started!"))

        self.upgradeButton.place(x=800, y=50)
        self.workerbutton.place(x=800, y=100)
        self.showStageButton.place(x=800, y=150)
        self.statsButton.place(x=800, y=200)



if __name__ == "__main__":#questo fa partire il gioco
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1000, height=600)
    canvas.pack()
    app = pizzeria(canvas, root) #root=self.canvas
    root.mainloop()