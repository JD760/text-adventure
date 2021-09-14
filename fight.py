## Fight.py ##
# handles enemy fights and xp/balance rewards

from player import *
from enemy import *
from commands import progressBar, printBar, Colours
import time


def selectOption(inputStr: str, prefixChar: str = ""):
    print(prefixChar + Colours.Green + inputStr[0] + Colours.White + inputStr[1::])


def enemyTurn(player: Player, enemy: Enemy):
    # enemy attack, player defend
    result = player.takeDamage()
    if result == 0:
        print("Player dodged the attack")
    else:
        print("Player took: ", result, "damage")


def playerTurn(player: Player, enemy: Enemy):
    # player attack, enemy defend
    result = enemy.takeDamage()
    if result == 0:
        print("Enemy dodged the attack")
    else:
        print("Player took: ", result, "damage")


def fightEnemy(player: Player, enemy: Enemy):
    result: str = ""
    choice: str = ""
    while player.health > 0:
        # cycle between player and enemy turns
        # player turn
        print("Player Turn")
        # choose to attack or flee
        print("Make a selection: ")
        selectOption("Attack - damage the enemy")
        selectOption("Flee - lose the fight + rewards")
        printBar()
        choice = ""
        while choice not in ["a", "f", "attack", "flee"]:
            choice = input("-->: ").lower()
        conversion = {"a": "attack", "f": "flee"}
        if choice in ["a", "f"]:
            choice = conversion[choice]
        if choice == "flee":
            print("Player loses")
            printBar()
            return
        printBar()

        result = enemy.takeDamage(player.damage, player.gameDifficulty)
        if result == 0:
            print("Enemy dodged the attack")
        progressBar(enemy.health, enemy.maxHealth, 10, "Enemy")
        
        printBar()
        # check if enemy alive
        if enemy.health <= 0:
            print("Player wins")
        # enemy turn
        time.sleep(1.5)
        printBar()
        print("Enemy Turn")
        time.sleep(0.2)
        result = player.takeDamage(enemy.damage, player.gameDifficulty)
        if result == 0:
            print("Player dodged the attack")
        time.sleep(0.2)
        progressBar(player.health, player.maxHealth, 10, "Player")
    else:
        # player is dead
        print("Game over")
        pass
