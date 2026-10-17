# ...existing code...
import PathFinder
import json
import os

path = PathFinder.findFile("troopDictionary.json")

print(path)

# Normalize path (handle string or list/tuple)
if isinstance(path, (list, tuple)):
    file_path = path[0]
else:
    file_path = path

if not os.path.isfile(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Try to extract a 'knight' value robustly
knight = None

# If JSON is a list of lists (original index attempt), try that first
if isinstance(data, list):
    try:
        knight = data[1][3]
    except Exception:
        pass

# If JSON is a dict, look for common keys
if knight is None and isinstance(data, dict):
    for key in ("knight", "Knight", "troops", "troopDictionary"):
        if key in data:
            knight = data[key]
            break

if knight is None:
    # Fallback: show structure to help debugging
    import pprint
    print("Loaded JSON but couldn't find 'knight' using expected indexes/keys. Data preview:")
    pprint.pprint(data)
else:
    print(knight)
# ...existing code...