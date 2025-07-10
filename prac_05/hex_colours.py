"""
CP1404 Practical
Hex colours dictionary
"""

COLOUR_TO_CODE = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff",
                  "alizarincrimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                  "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                  "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378", "apricot": "#fbceb1", "aqua": "#00ffff",
                  "aquamarine1": "#7fffd4"}
print(COLOUR_TO_CODE)
colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"The code for {colour_name} is {COLOUR_TO_CODE[colour_name]}.")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
