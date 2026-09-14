import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import time

root = tk.Tk()
canvasWidth = 300
canvasHeight = 660
canvas = tk.Canvas(root, width=canvasWidth, height=canvasHeight)
canvas.pack()
root.title("Clash_Royale 1.2")

def texturesManager():
    texturesSpecifics = [
        # robe generali
        ["battleField.png", [0, 0, "nw"]],
        ["princessTower.png", [60, 150, "center"]],  # leftPrincessTower
        ["princessTower.png", [240, 150, "center"]],  # rightPrincessTower
        ["kingTower.png", [150, 75, "center"]],  # kingTower
        ["princessTowerBlue.png", [60, 510, "center"]],  # leftPrincessTowerBlue
        ["princessTowerBlue.png", [240, 510, "center"]],  # rightPrincessTowerBlue
        ["kingTowerBlue.png", [150, 570, "center"]],  # kingTowerBlue
        # truppe blu
        ["knight.png", [150, 300, "center"]],  # knight blue
        ["zap.png", [150, 300, "center"]],  # zap blue
        ["fireball.png", [150, 300, "center"]],  # fireball blue
        ["hogRider.png", [150, 300, "center"]],  # hogRider blue
        ["miniPekka.png", [150, 300, "center"]],  # miniPekka blue
        ["pekka.png", [150, 300, "center"]],  # pekka blue
        ["valkyrie.png", [150, 300, "center"]],  # valkyrie blue
        ["wallBreaker.png", [150, 300, "center"]],  # wallBreaker blue
        # truppe rosse
        ["knightRed.png", [150, 300, "center"]],  # knight red
        ["zapRed.png", [150, 300, "center"]],  # zap red
        ["fireballRed.png", [150, 300, "center"]],  # fireball red
        ["hogRiderRed.png", [150, 300, "center"]],  # hogRider red
        ["miniPekkaRed.png", [150, 300, "center"]],  # miniPekka red
        ["pekkaRed.png", [150, 300, "center"]],  # pekka red
        ["valkyrieRed.png", [150, 300, "center"]],  # valkyrie red
        ["wallBreakerRed.png", [150, 300, "center"]]   # wallBreaker red
    ]
    texturesNeeded = [texture[0] for texture in texturesSpecifics]
    paths = findPaths(texturesNeeded)
    if paths is None:
        return

    canvas.images = []  # salva le immagini in un array per evitare che vengano cancellate
    textures = []  # crea un array per conservare le texture e manipolarle in futuro
    for path, specifics in zip(paths, texturesSpecifics):  # ridimensiona e crea le textures
        if specifics[0] == "knight.png":
            break
        resizeDims = (canvasWidth, canvasHeight) if specifics[0] == "battleField.png" else (90, 90)
        textures.append(loadAndPlaceImage(canvas, path, resizeDims, specifics[1][:2], specifics[1][2]))
    blueTroops = []
    redTroops = []
    for path, specifics in zip(paths, texturesSpecifics):
        if specifics[0] in ["knight.png", "zap.png", "fireball.png", "hogRider.png", "miniPekka.png", "pekka.png", "valkyrie.png", "wallBreaker.png"]:
            blueTroops.append(path)  # Save the path to the blueTroops list
        if specifics[0] in ["knightRed.png", "zapRed.png", "fireballRed.png", "hogRiderRed.png", "miniPekkaRed.png", "pekkaRed.png", "valkyrieRed.png", "wallBreakerRed.png"]:
            redTroops.append(path)


# tre funzioni per trovare le foto nel pc, è un po' arcana e non serve sapere come funziona in modo completo...
def findPaths(texturesNeeded):
    pathsFound = []
    for drive in ["J://", "I://", "H://", "G://", "F://", "E://", "D://", "C://"]:  # array con tutti i drive in cui vogliamo cercare
        if os.path.exists(drive):  # controlla se il drive esiste
            print(f"Searching in {drive}...")
            if drive == "C://":
                specificPath = "C://Users//leizh//OneDrive//Desktop//project CR//project_CR 1.2//renderers"  # percorso specifico per le texture
                if os.path.exists(specificPath):  # controlla se il percorso specifico esiste
                    print(f"Searching in specific path: {specificPath}...")
                    for texture in texturesNeeded:  # ripete il procedimento per tutte le texture che ci servono
                        path = textureFinder(texture, specificPath)
                        if path:
                            pathsFound.append(path)  # aggiunge la directory alla lista di directory trovate
                            print(f"textures found:({len(pathsFound)}/{len(texturesNeeded)}){texture, path}")
                        if len(pathsFound) == len(texturesNeeded):  # se ha trovato tutte le texture
                            print("All textures found.")
                            return pathsFound
                    print(f"No textures found in {specificPath}")
            temporaryCounter = len(pathsFound)
            for texture in texturesNeeded:  # ripete il procedimento per tutte le texture che ci servono
                path = textureFinder(texture, drive)
                if path:
                    pathsFound.append(path)  # se trova una texture che ci serve aggiunge la directory alla lista di directory trovate
                    print(f"textures found:({len(pathsFound)}/{len(texturesNeeded)}){texture, path}")
                    time.sleep(0.3)
                if len(pathsFound) == len(texturesNeeded):  # se ha trovato tutte le texture
                    print("All textures found.")
                    time.sleep(1)
                    return pathsFound
            if len(pathsFound) == temporaryCounter:  # se non trova texture nel drive da un feedback
                print("no textures in ", drive)
        else:
            time.sleep(0.3)
            print(f"directory '{drive}' does not exist")  # se la directory non esiste manda un feedback


def textureFinder(textureToFind, drive):  # analizza completamente il drive in cerca delle texture
    for root, _, files in os.walk(drive):
        for file in files:
            if textureToFind in file:
                return os.path.join(root, file)


def loadAndPlaceImage(canvas, path, resizeDims, position, anchor):  # formatta le immagini e le piazza
    image = Image.open(path)
    resizedImage = image.resize(resizeDims)
    tkImage = ImageTk.PhotoImage(resizedImage)
    canvas.create_image(*position, image=tkImage, anchor=anchor)  # crea l'immagine sul canvas
    canvas.images.append(tkImage)  # salva l'immagine per evitare che l'oggetto si corrompa
    return tkImage  # restituisce l'immagine pronta per essere usata


texturesManager()
root.mainloop()