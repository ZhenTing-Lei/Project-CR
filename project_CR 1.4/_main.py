#Quinta versione del gioco
# 10/08/2026-

import CanvasManager as CanvasManager
import TroopManager as TroopManager
import RenderingManager as RenderingManager

class ClashRoyaleSimulator:
    def __init__(self):
        
        troop = TroopManager.Troop()
        sprites = RenderingManager.Renderers()
        canvas = CanvasManager.Canvas(troop, sprites)

        canvas.stateItself(canvas) #consegna la reference del canvas al canvas stesso(tipo SerializeField self)

        canvas.run() # !!! Importante, mettere per ultimo


if __name__ == "__main__":#questo fa partire il gioco
    app = ClashRoyaleSimulator()