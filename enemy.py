import math, random

# class to describe an instance of an enemy
class Enemy():
    def __init__(self,
            difficulty: int,
            level: int,
            ) -> int:
        if difficulty < 1:
            print("Enemy assigned incorrect difficulty, defaulting to 1")
            difficulty = 1
        # difficulty of the enemy will scale with player level and game difficulty (chosen at start)
        multiplier = (difficulty * level ) / (difficulty / level)
        self.maxHealth = math.floor(100 * multiplier)
        self.health = self.maxHealth
        self.damage = math.floor(5 * multiplier)
        self.dodgeChance: int = math.floor(20 + (self.maxHealth / 100))


    def takeDamage(self, damage: int, difficulty: int) -> int:
        if random.randint(1, 100) <= self.dodgeChance:
            # no damage taken as attack dodged
            return 0
        # return the amount of damage taken
        result = math.floor(damage * (difficulty / 2))
        self.health -= result
        return result
