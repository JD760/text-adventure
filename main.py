import time, random
from player import *
#from items import *
#from enemies import *
from commands import *
from shop import openShop

# highlights the first letter of a choice green
def selectOption(inputStr: str, prefixChar: str = ""):
    print(prefixChar + Colours.Green + inputStr[0] + Colours.White + inputStr[1::]) 


def gameStart():
    choice:str = ""
    clear()
    printBar()
    print("Select an option: ")
    selectOption("Start", ">")
    selectOption("Quit", ">")
    while choice != "s" and choice != "q":
        choice = input("-->: ").lower()
    if choice == "quit":
        clear()
        return
    printBar()
    ## start the game ##

    # choose a player class
    print("Select a class: ")
    selectOption("Assassin - chance of dodging attacks", ">")
    selectOption("Wizard - fireball has limited use + high damage", ">")
    selectOption("Knight - Melee damage boost + melee resistance", ">")

    # get the player choice and check it is valid, loop while invalid
    choice = ""
    choices = ["a", "w", "k", "assassin", "wizard", "knight"]
    while choice not in choices:
        choice = input("-->: ").lower() # lowercase -> less required checks
    printBar()

    # convert shorthand input (first letter) into recognised class
    conversion = {"a": "assassin", "w": "wizard", "k": "knight"}
    if choice in ["a", "w", "k"]:
        choice = conversion[choice]

    # create a player instance
    player = Player(choice)
    openStats(player)

    openShop()


def enemyFight(player: Player, enemy: Enemy):
    choice: str = ""
    while player.health > 0:
        printBar()
        progressBar(player.health, player.maxHealth, "Player")
        progressBar(enemy.health, enemy.maxHealth, "Enemy")
        selectOption("Attack")
        selectOption("Defend")
        printBar()
        choice = input("-->: ")
        


gameStart()
