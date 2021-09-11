## IO.py - SIL text adventure
# this file handles user text input for game choices etc
# and text output such as the help or stats pages


import system, name 
# clear the console 
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def showHelpPage() -> None:
    clearclear()

def showStatsPage() -> None:
    clear()


def showShopPage() -> None:
    clear()


def processCommand(command: str):
    commands = {
            "help": showHelpPage,
            "stats": showStatsPage,
            "shop": showShopPage
            }
    commands[command]()
