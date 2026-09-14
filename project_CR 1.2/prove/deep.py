def find_paths(textures_needed):
    paths_found = []
    drives = ["J://", "I://", "H://", "G://", "F://", "E://", "D://"]
    for texture in textures_needed:  # Loop through textures in order
        for drive in drives:
            if os.path.exists(drive):
                path = texture_finder(texture, drive)
                if path:
                    paths_found.append(path)
                    print(f"Found {texture} in {drive}")
                    break  # Move to next texture after finding
        else:
            print(f"Warning: {texture} not found in any drive!")
            paths_found.append(None)  # Keep alignment with textures_needed
    # Check if all textures are found
    if None in paths_found:
        # Handle missing textures
    return paths_found