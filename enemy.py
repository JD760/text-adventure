import math
# class to describe an instance of an enemy
class Enemy():
    def __init__(self, difficulty: int, level: int):
        if difficulty < 1:
            print("Enemy assigned incorrect difficulty, defaulting to 1")
            difficulty = 1
        health: int = 100
        damage: int = 5
        ability: str = ""
        multiplier = (difficulty * level ) / (difficulty / level)
        self.health = math.floor(health)
        self.damage = math.floor(damage)
        self.ability = ability
    
