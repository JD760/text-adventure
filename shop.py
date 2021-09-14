## shop.py - SIL text adventure
# this file handles items sold in the shop

import random
from player import *
from commands import printBar

class Item():
    def __init__(self,
            name: str,
            displayName: str,
            category: str,
            effect: int,
            cost: int):
        self.name = name
        self.displayName = displayName
        self.category = category
        self.effect = effect
        self.cost = cost



class Items():
    health1 = Item("health1", "Health I", "health", 15, 3)
    health2 = Item("health2", "Health II", "health", 25, 5)
    health3 = Item("health3", "Health III", "health", 40, 8)

    strength1 = Item("strength1", "Strength I", "strength", 3, 3)
    strength2 = Item("strength2", "Strength II", "strength", 5, 5)
    strength3 = Item("strength3", "Strength III", "strength", 8, 8)
    
    # dodge -> assassin class only
    # fireball -> wizard class only
    # melee -> knight class only
    dodge1 = Item("dodge1", "Dodge I", "dodge", 2, 5) 
    fireball1 = Item("fireball1", "Fireball I", "fireball", 1, 5)
    melee1 = Item("melee1", "Melee Boost I", "melee", 2, 5)


def displayItem(item: Item):
    print(item.displayName, " : ", item.category, "+", item.effect)
    print("Price: ", item.cost)
    printBar()


def openShop(player: Player):
    print("\" Welcome to my Shop \"")
    printBar()
    # all T1 items always stocked
    # 2/3 T2 items stocked at any time 
    # 1/3 T3 items stocked at any time
    # relevant class item also always stocked

    ## display item
    #health
    displayItem(Items.health1)
    displayItem(Items.health2)
    displayItem(Items.health3)
    # damage
    displayItem(Items.strength1)
    displayItem(Items.strength2)
    displayItem(Items.strength3)
    if player.ability == "dodge":
        displayItem(Items.dodge1)
    elif player.ability == "fireball":
        displayItem(Items.fireball1)
    else:
        displayItem(Items.melee1)


    
    
