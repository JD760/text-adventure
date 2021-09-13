## IO.py - SIL text adventure
# this file handles user text input for game choices etc
# and text output such as the help or stats pages

from os import system, name 
from player import *
from enemy import *


class Colours():
    Green: str = "\033[1;32;40m"
    Red: str = "\033[1;31;40m"
    White: str = "\033[1;37;40m"



# clear the console 
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


# menu that gives player the option to select a character class
def classSelectMenu() -> Player:
    print("Player classes: \n\
            \033[1;31;40mk\033[1;37;40mnight - bonus melee damage\n\
            \033[1;31;30ma\033[1;37;40mssassin - chance of dodging attacks\n")
    selection: str = ""
    while selection not in ["k", "a", "w"]:
        selection = input("select a class: \033[1;31;40mk, a, w")

# health/xp meter creation
def progressBar(quantity: int, maxQuantity: int, barUnits: int, quantityName: str = ""):
    filledUnits: int = math.floor(quantity / round(maxQuantity / barUnits, 1))
    bar: str = quantityName + ":["
    for i in range(barUnits):
        if i < filledUnits:
            bar += "\033[1;32;40m -" # add a green unit
        else:
            bar += "\033[1;31;40m -" # add a red unit
    bar += "\033[1;37;40m" # reset text colour to white
    outputStr: str = bar + "]" + str(quantity) + "/" + str(maxQuantity)
    print(outputStr)


def openHelp() -> None:
    clear()
    print("Help menu:\n\
    help - print this menu\n\
    stats - show player statistics menu\n\
    shop - open the item shop\n\
    exit - exit the game\n\
    restart - start a new game\n\
    attack - attack an enemy\n\
    defend - defend against an enemy attack")
    return


def openStats(player):
    progressBar(player.health, player.maxHealth, 10, "Health")
    progressBar(player.experience, player.maxXP, 10, "Experience")
    print("Player Damage: ", player.damage)
    print("Player Ability: ", player.ability)


def openShop(player):
    pass


# creates a list of sensible commands given a specific context
# eg attack/defend only work when context is enemy fight
# return - if successful, failure indicates invalid input
def processInput(context: str, inputStr: str, player: Player, enemy: Enemy) -> bool:
    if context not in ["enemyfight", "death", "fightVictory"]:
        return False
    contextCommands = {
            "enemyfight": ["attack", "defend"],
            "death": ["restart", "exit"],
            "fightVictory": ["shop", "stats"]
        }
    anyContext = ["exit", "help"]
    inputStr = inputStr.lower() # remove capitals
    if inputStr not in contextCommands[context] and inputStr not in anyContext:
        print("This command is not recognised during: ", context)
        return False

    # dicts don't work for this because functions need different parameters
    if inputStr == "attack":
        attack(player, enemy)
    elif inputStr == "defend":
        defend(player, enemy)
    elif inputStr == "restart":
        restartGame()
    elif inputStr == "exit":
        exitGame()
    elif inputStr == "shop":
        openShop()
    elif inputStr == "stats":
        openStats(player)
    elif inputStr == "help":
        openHelp()
    else:
        print("Something went wrong")
        exitGame()
    return True
