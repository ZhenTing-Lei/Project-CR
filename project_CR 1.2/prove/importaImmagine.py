#prima prova di importare immagini, assicurarsi di aver installato Pillow, in caso contrario, usa il comando "pip install pillow"
from tkinter import Tk, Canvas
from PIL import Image, ImageTk  # Importa Pillow

# Crea la finestra principale
root = Tk()
canvas = Canvas(root, width=300, height=660)
canvas.pack()

# Carica e aggiungi l'immagine al canvas
image_path = r"D:\project CR 1.2\battleField.png"  # Usa una stringa raw per evitare problemi con i backslash
try:
    image = Image.open(image_path)  # Apri l'immagine
    resized_image = image.resize((300, 660))  # Ridimensiona l'immagine per adattarla al canvas
    princess_tower_image = ImageTk.PhotoImage(resized_image)  # Converti l'immagine per Tkinter
    canvas.create_image(150, 330, image=princess_tower_image, anchor="center")  # Centra l'immagine nel canvas

    # Mantieni un riferimento all'immagine per evitare che venga garbage collected
    canvas.princess_tower_image = princess_tower_image
except FileNotFoundError:
    print(f"Errore: Impossibile trovare il file immagine in {image_path}")
except Exception as e:
    print(f"Errore durante il caricamento dell'immagine: {e}")

# Avvia il loop principale
root.mainloop()