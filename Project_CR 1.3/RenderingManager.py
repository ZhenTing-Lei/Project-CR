import PathFinder
import os

class Renderers:
    def __init__(self):
        results = PathFinder.findFolder("Renderers")

        if not results:
            raise FileNotFoundError("Renderers folder not found anywhere on disk")

        self.renderers_path = results[0]

        # load the 3 subfolders and their pngs
        self.images = {}
        for subfolder in os.listdir(self.renderers_path):
            subfolder_path = os.path.join(self.renderers_path, subfolder)
            if os.path.isdir(subfolder_path):
                pngs = [
                    os.path.join(subfolder_path, f)
                    for f in os.listdir(subfolder_path)
                    if f.endswith(".png")
                ]
                self.images[subfolder] = pngs


if __name__ == "__main__":
    app = Renderers()