"""
CP1404/CP5632 Practical
Hex colours look up
"""

COLOUR_TO_HEX = {"Black": "#000000", "Blue": "#0000ff", "Violet": "#8a2be2", "Brown": "#a52a2a", "Cyan": "#00ffff",
                 "Green": "#00ff00", "Gold": "#ffd700", "Gray": "#bebebe", "Pink": "#ff69b4", "Red": "#ff0000"}
print(COLOUR_TO_HEX)

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    if colour_name in COLOUR_TO_HEX:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()
