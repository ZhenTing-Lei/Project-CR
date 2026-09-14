import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import time

def textures_manager():
    textures_specifics = [
        ["battleField.png", [0, 0, "nw"]],  # Sfondo
        ["princessTower.png", [60, 150, "center"]],  # Torre sinistra
        ["princessTower.png", [240, 150, "center"]],  # Torre destra
        ["kingTower.png", [150, 75, "center"]],  # Torre centrale
        ["princessTowerBlue.png", [60, 510, "center"]],  # Torre sinistra blu
        ["princessTowerBlue.png", [240, 510, "center"]],  # Torre destra blu
        ["kingTowerBlue.png", [150, 570, "center"]]  # Torre centrale blu
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
    canvas.images = []  # Salva le immagini in un array per evitare che vengano cancellate
    textures = []  # Crea un array per conservare le texture e manipolarle in futuro
    for path, specifics in zip(paths, textures_specifics):  # Ridimensiona e crea le textures
        resize_dims = (canvasWidth, canvasHeight) if specifics[0] == "battleField.png" else (90, 90)
        textures.append(load_and_place_image(canvas, path, resize_dims, specifics[1][:2], specifics[1][2]))
    root.mainloop()


def find_paths(textures_nedded):
    paths_found = []
    # Rimuoviamo "C://" dalla lista dei drive da cercare
    for drive in ["J://", "I://", "H://", "G://", "F://", "E://", "D://"]:  # Array con tutti i drive in cui vogliamo cercare
        if os.path.exists(drive):  # Controlla se il drive esiste
            print(f"Searching in {drive}...")
            temporary_counter = len(paths_found)
            for texture in textures_nedded:  # Ripete il procedimento per tutte le texture che ci servono
                path = texture_finder(texture, drive)
                if path:
                    paths_found.append(path)  # Se trova una texture che ci serve aggiunge la directory alla lista di directory trovate
                    print(f"textures found:({len(paths_found)}/{len(textures_nedded)}) {texture, path}")
                    time.sleep(0.8)
                if len(paths_found) == len(textures_nedded):  # Se ha trovato tutte le texture
                    print("All textures found.")
                    time.sleep(1)
                    return paths_found
            if len(paths_found) == temporary_counter:  # Se non trova texture nel drive da un feedback
                print("no textures in ", drive)
        else:
            time.sleep(0.8)
            print(f"directory '{drive}' does not exist")  # Se la directory non esiste manda un feedback
    risposta = messagebox.askyesno("Conferma", "Non tutte le texture sono state trovate vuoi continuare lo stesso?")
    if risposta:
        return paths_found  # Fa partire il gioco con le texture trovate
    return None


def texture_finder(texture_to_find, drive):  # Analizza completamente il drive in cerca delle texture
    for root, _, files in os.walk(drive):
        for file in files:
            if texture_to_find in file:
                return os.path.join(root, file)


def load_and_place_image(canvas, path, resize_dims, position, anchor):  # Format e piazza le immagini
    image = Image.open(path)
    resized_image = image.resize(resize_dims)
    tk_image = ImageTk.PhotoImage(resized_image)
    canvas.create_image(*position, image=tk_image, anchor=anchor)  # Crea l'immagine sul canvas
    canvas.images.append(tk_image)  # Salva l'immagine per evitare che l'oggetto si corrompa
    return tk_image  # Restituisce l'immagine pronta per essere usata


textures_manager()