"""Prac_05 - Hex colours."""

COLOUR_TO_HEXADECIMAL = {"floralwhite": "#fffaf0", "green lizard": "#a7f432, ",
                "black": "#000000", "white": "#ffffff",
                "violetred1": "#ff3e96", "absolute zero": "#0048ba",
                "amber": "#ffbf00", "amethyst": "#9966cc",
                "red1": "#ff0000", "blue1": "#0000ff"}

colour_name = input("Colour name? ").lower()
while colour_name != "":
    if colour_name in COLOUR_TO_HEXADECIMAL:
        print(f"{colour_name} in hexadecimal is {COLOUR_TO_HEXADECIMAL[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Colour name? ").lower()
