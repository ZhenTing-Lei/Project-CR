#La quarta versione del gioco. 
#pulito il culo alla terza versione, con le sprites correttamente caricate, divisione dei script, fix di bug minori e l'aggiunta del cooldown e fatto le basi per l'enemyIA
#problema: CanvasManager ha ancora troppo potere in mano, Troop crea troppi canvas.after e fa letteralmente laggare il gioco e blocca il progress
# -06/06/2026, sono troppo stanco per continuare
#si aspetta una quinta versione
import TaskManager as TaskManager
import CanvasManager as CanvasManager
import TroopManager as TroopManager
import RenderingManager as RenderingManager

class ClashRoyaleSimulator:
    def __init__(self):
        TaskManager.CheckWorks() # Placeholder
        
        troop = TroopManager.Troop()
        sprites = RenderingManager.Renderers()
        canvas = CanvasManager.Canvas(troop, sprites)

        canvas.stateItself(canvas) #consegna la reference del canvas al canvas stesso(tipo SerializeField self)
        canvas.run() # !!! Importante, mettere per ultimo

    def boh(self): #Boh
        print("Im gay")


if __name__ == "__main__":#questo fa partire il gioco
    app = ClashRoyaleSimulator()