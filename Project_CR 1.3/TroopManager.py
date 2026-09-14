import PathFinder
import json

class Troop:
    def __init__(self):
        #trova il path del jason
        results = PathFinder.findFile("troopDictionary.json")
        
        # error handler
        if not results:
            raise FileNotFoundError("troopDictionary.json not found anywhere on disk")
        
        #ottieni i dati dal jason
        with open(results[0], "r") as f:
            self.troopStats = json.load(f)
        
        self.sizes={"small":10,"medium":15,"big":20,"superbig":40} #questo implementa le dimensioni delle trupp
        


if __name__ == "__main__":
    app = Troop()
