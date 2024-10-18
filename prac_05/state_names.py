"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
for code, name in CODE_TO_NAME.items():
    print(f"{code:<3} is {name}")

is_valid_input = False
while not is_valid_input:
    try:
        state_code = input("Enter short state: ").upper()
        print(state_code, "is", CODE_TO_NAME[state_code])
        is_valid_input = True
    except KeyError:
        print("Invalid short state")
