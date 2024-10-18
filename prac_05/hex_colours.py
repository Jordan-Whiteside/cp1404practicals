"""Prac_05 - Hex colours."""

NAME_TO_CODE = {"floralwhite": "#fffaf0", "green lizard": "#a7f432, ",
                "black": "#000000", "white": "#ffffff",
                "violetred1": "#ff3e96", "absolute zero": "#0048ba",
                "amber": "#ffbf00", "amethyst": "#9966cc",
                "red1": "#ff0000", "blue1": "#0000ff"}

colour_name = input("Colour name? ").lower()
while colour_name != "":
    if colour_name in NAME_TO_CODE:
        print(f"{colour_name} in hexadecimal is {NAME_TO_CODE[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Colour name? ").lower()
