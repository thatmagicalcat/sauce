import keyboard

def add_abbreviation(abbreviations):
    for key, value in abbreviations:
        keyboard.add_abbreviation(key, value)


def remove_abbrevation(abbreviation):
    keyboard.remove_abbreviation(abbreviation)
