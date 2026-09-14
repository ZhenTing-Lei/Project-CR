import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import time

def textures_manager():
    textures_specifics = [
        ["battleField.png", [0, 0, "nw"]],
        ["princessTower.png", [60, 150, "center"]],  # leftPrincessTower
        ["princessTower.png", [240, 150, "center"]],  # rightPrincessTower
        ["kingTower.png", [150, 75, "center"]],  # kingTower
        ["princessTowerBlue.png", [60, 510, "center"]],  # leftPrincessTowerBlue
        ["princessTowerBlue.png", [240, 510, "center"]],  # rightPrincessTowerBlue
        ["kingTowerBlue.png", [150, 570, "center"]]  # kingTowerBlue
    ]
    textures_nedded = [texture[0] for texture in textures_specifics]
    paths = find_paths(textures_nedded)
    if paths is None:
        return
    root = tk.Tk()
    canvasWidth = 300
    canvasHeight = 660
    canvas = tk.Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.title("Clash_Royale 1.2")
    canvas.images = []  # Initialize the list to store image references
    textures = []  # Create an array to store textures for future manipulation
    for path, specifics in zip(paths, textures_specifics):  # Resize and create textures
        resize_dims = (canvasWidth, canvasHeight) if specifics[0] == "battleField.png" else (90, 90)
        textures.append(load_and_place_image(canvas, path, resize_dims, specifics[1][:2], specifics[1][2]))
    root.mainloop()


def find_paths(textures_nedded):
    paths_found = []
    for drive in ["J://", "I://", "H://", "G://", "F://", "E://", "D://"]:  # Drives to search
        if os.path.exists(drive):  # Check if the drive exists
            print(f"Searching in {drive}...")
            temporary_counter = len(paths_found)
            for texture in textures_nedded:  # Search for each required texture
                path = texture_finder(texture, drive)
                if path:
                    paths_found.append(path)  # Add the found texture path to the list
                    print(f"textures found:({len(paths_found)}/{len(textures_nedded)}){texture, path}")
                    time.sleep(0.8)
                if len(paths_found) == len(textures_nedded):  # If all textures are found
                    print("All textures found.")
                    time.sleep(1)
                    return paths_found
            if len(paths_found) == temporary_counter:  # If no textures were found in the drive
                print("no textures in ", drive)
        else:
            time.sleep(0.8)
            print(f"directory '{drive}' does not exist")  # Feedback if the directory doesn't exist
    risposta = messagebox.askyesno("Conferma", "Non tutte le texture sono state trovate vuoi continuare lo stesso?")
    if risposta:
        return paths_found  # Start the game with the found textures
    return None


def texture_finder(texture_to_find, drive):  # Search the drive for the texture
    for root, _, files in os.walk(drive):
        for file in files:
            if texture_to_find in file:
                return os.path.join(root, file)


def load_and_place_image(canvas, path, resize_dims, position, anchor):  # Format and place images
    image = Image.open(path)
    resized_image = image.resize(resize_dims)
    tk_image = ImageTk.PhotoImage(resized_image)
    canvas.create_image(*position, image=tk_image, anchor=anchor)  # Create the image on the canvas
    canvas.images.append(tk_image)  # Save the image to prevent garbage collection
    return tk_image  # Return the image for future use


textures_manager()