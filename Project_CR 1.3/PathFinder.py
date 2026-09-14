import os

#Funzione che ti trova un file specifico
def findFile(target, full_scan_fallback=True):

    # 1. check the current working directory and nearby folders first
    quick_locations = [
        os.getcwd(),
        os.path.dirname(os.path.abspath(__file__)),  # same folder as the script
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "Documents"),
    ]

    for location in quick_locations:
        candidate = os.path.join(location, target)
        if os.path.isfile(candidate):
            print(f"Found quickly: {candidate}")
            return [candidate]

    # 2. fall back to full disk scan if nothing found
    if not full_scan_fallback:
        print("Not found in common locations.")
        return []

    drives = ["C:\\", "D:\\", "E:\\", "F:\\"]
    found_paths = []

    for drive in drives:
        if not os.path.exists(drive):
            continue
        print(f"Full scan on {drive}... (this may take a while)")

        for root, dirs, files in os.walk(drive):
            dirs[:] = [
                d for d in dirs
                if d not in {"Windows", "System32", "$Recycle.Bin", "Program Files", "Program Files (x86)"}
            ]
            if target in files:
                full_path = os.path.join(root, target)
                found_paths.append(full_path)
                print(f"Found: {full_path}")

    return found_paths

#Funzione che ti trova una cartella specifica
def findFolder(target, full_scan_fallback=True):
    quick_locations = [
        os.getcwd(),
        os.path.dirname(os.path.abspath(__file__)),
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "Documents"),
    ]

    for location in quick_locations:
        candidate = os.path.join(location, target)
        if os.path.isdir(candidate):  # isdir instead of isfile
            print(f"Found quickly: {candidate}")
            return [candidate]

    if not full_scan_fallback:
        print("Not found in common locations.")
        return []

    drives = ["C:\\", "D:\\", "E:\\", "F:\\"]
    found_paths = []

    for drive in drives:
        if not os.path.exists(drive):
            continue
        print(f"Full scan on {drive}...")

        for root, dirs, files in os.walk(drive):
            dirs[:] = [
                d for d in dirs
                if d not in {"Windows", "System32", "$Recycle.Bin", "Program Files", "Program Files (x86)"}
            ]
            if target in dirs:  # dirs instead of files
                full_path = os.path.join(root, target)
                found_paths.append(full_path)
                print(f"Found: {full_path}")

    return found_paths