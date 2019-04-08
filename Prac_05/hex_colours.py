"""
CP1404/CP5632 Prac
Hexadecimal colour dictionary
"""
COLOURS = {"Blue1": "#0000ff", "Black": "#000000", "BlueViolet": "#8a2be2", "DarkGreen": "#006400",
           "FloralWhite": "#fffaf0", "Gold1": "#ffd700"}

colour = input("Enter colour: ").upper()
while colour != "":
    if colour in COLOURS:
        print(colour, "is", COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").upper()
