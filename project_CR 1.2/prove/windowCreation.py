import tkinter as tk
from tkinter import messagebox

# windowCreation.py
# This script creates a simple GUI window using tkinter.


def show_announcement():
    messagebox.showinfo("Annuncio", "Benvenuto nella nostra applicazione!")

# Create the main window
root = tk.Tk()
root.title("Finestra di Annuncio")
root.geometry("400x200")

# Add a button to show the announcement
announcement_button = tk.Button(root, text="Mostra Annuncio", command=show_announcement)
announcement_button.pack(pady=50)

# Run the application
root.mainloop()