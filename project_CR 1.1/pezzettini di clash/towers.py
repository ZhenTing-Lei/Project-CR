import tkinter as tk

class Tower:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            self.canvas.delete(self.id)

    def is_in_range(self, target):
        if not self.target_list:
            self.target_list.append(target)

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=300, height=625)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 0, 600, 600, fill="blue")
        self.canvas.create_rectangle(0, 0, 300, 275, fill="green")
        self.canvas.create_rectangle(300, 325, 0, 600, fill="green")
        self.canvas.create_rectangle(30, 275, 80, 325, fill="brown")
        self.canvas.create_rectangle(270, 275, 220, 325, fill="brown")
        self.king_tower = Tower(self.canvas, 115, 15, 185, 85, "red")
        self.princess_tower = Tower(self.canvas, 30, 100, 80, 150, "red")
        self.right_princess_tower = Tower(self.canvas, 270, 100, 220, 150, "red")
        self.right_tower_alive = True
        self.left_tower_alive = True
        self.king_tower_alive = True
        self.canvas.create_rectangle(115, 515, 185, 585, fill="light blue")
        self.canvas.create_rectangle(30, 500, 80, 450, fill="light blue")
        self.canvas.create_rectangle(270, 500, 220, 450, fill="light blue")
        self.canvas.create_oval(50, 335, 60, 325, fill="black")
        self.canvas.create_oval(250, 335, 240, 325, fill="white")
        self.canvas.create_oval(50, 440, 60, 450, fill="white")
        self.canvas.create_oval(250, 440, 240, 450, fill="white")

        self.attack_button = tk.Button(self.window, text="Tower 1 Attacks Tower 2", command=self.try_attack)
        self.attack_button.pack()

        self.window.mainloop()

    def try_attack(self):
        self.king_tower.take_damage(10)
        self.update_ui()

    def update_ui(self):
        # Update the UI elements here
        pass

if __name__ == "__main__":
    game = Game()