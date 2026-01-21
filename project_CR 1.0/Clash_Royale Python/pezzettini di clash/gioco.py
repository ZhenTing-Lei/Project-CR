import pygame
import sys

# Inizializza Pygame
pygame.init()

# Imposta la finestra di gioco
larghezza_schermo, altezza_schermo = 800, 600
schermo = pygame.display.set_mode((larghezza_schermo, altezza_schermo))
pygame.display.set_caption("Pygame")

# Colori
bianco = (255, 255, 255)
blu = (0, 0, 255)   

# Proprietà del giocatore
larghezza_giocatore, altezza_giocatore = 50, 50
x_giocatore, y_giocatore = larghezza_schermo // 2, altezza_schermo - altezza_giocatore
velocità_giocatore = 5

# Ciclo principale del gioco
orologio = pygame.time.Clock()
in_esecuzione = True
while in_esecuzione:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            in_esecuzione = False

    # Movimento del giocatore
    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_LEFT]:
        x_giocatore -= velocità_giocatore
    if tasti[pygame.K_RIGHT]:
        x_giocatore += velocità_giocatore

    # Disegna il giocatore
    schermo.fill(bianco)
    pygame.draw.rect(schermo, blu, (x_giocatore, y_giocatore, larghezza_giocatore, altezza_giocatore))

    pygame.display.flip()
    orologio.tick(60)

pygame.quit()
sys.exit()