"""
CP1404/CP5632 Prac
Hexadecimal colour dictionary
"""
COLOURS = {"BLUE1": "#0000ff", "BLACK": "#000000", "BLUEVIOLET": "#8a2be2", "DARKGREEN": "#006400",
           "FLORALWHITE": "#fffaf0", "GOLD1": "#ffd700"}

colour = input("Enter colour: ").upper()
while colour != "":
    if colour in COLOURS:
        print(colour, "is", COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").upper()
