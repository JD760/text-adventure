import time, random
from player import *
#from items import *
#from enemies import *
from commands import *
from shop import openShop
from fight import fightEnemy

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
    playerClass: str = choice

    # choose a game difficulty
    difficulty: int = 0
    print("Select a game difficulty")
    selectOption("Easy - reduced enemy health and increased player damage")
    selectOption("Normal - standard game difficulty")
    selectOption("Hard - increased enemy health and player damage")
    choice = ""
    choices = ["e", "n", "h", "easy", "normal", "hard"]
    while choice not in choices:
        choice = input("-->: ").lower()
    conversion = {"e" : "easy", "n": "normal", "h": "hard"}
    if choice in ["e", "n", "h"]:
        choice = conversion[choice]
    
    if choice == "easy":
        difficulty = 0.75
    elif choice == "normal":
        difficulty = 1
    elif choice == "hard":
        difficulty = 1.5
    
    printBar()
    # create a player instance
    player = Player(playerClass, difficulty)

    # begin the first enemy fight
    enemy = Enemy(player.gameDifficulty, player.level)
    fightEnemy(player, enemy)

gameStart()
