def sort(width, height, length, mass):
    """
    Sort packages into stacks based on their dimensions and mass.
    
    Returns: "STANDARD", "SPECIAL", or "REJECTED"
    """
    # Figure out if package is bulky
    volume = width * height * length
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Check for heavy packages
    is_heavy = mass >= 20
    
    # I'm using a ternary here for compact logic
    return "REJECTED" if (is_bulky and is_heavy) else ("SPECIAL" if (is_bulky or is_heavy) else "STANDARD")