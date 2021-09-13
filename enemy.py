import math
# class to describe an instance of an enemy
class Enemy():
    def __init__(self,
            difficulty: int,
            level: int,
            health: int,
            damage: int,
            ability: str = ""
            ) -> int:
        if difficulty < 1:
            print("Enemy assigned incorrect difficulty, defaulting to 1")
            difficulty = 1
        # difficulty of the enemy will scale with player level and game difficulty (chosen at start)
        multiplier = (difficulty * level ) / (difficulty / level)
        self.maxHealth = math.floor(health)
        self.health = self.maxHealth
        self.damage = math.floor(damage)
        self.ability = ability


    def takeDamage(self, damage: int, attackType: str, difficulty: int) -> int:
        if self.ability == "dodge":
            if random.randint(1, 10) <= 3:
                print(self.name, " dodged the attack")
                return 0
        result = math.floor(damage * (difficulty / 2))
        self.health -= result
        return result 
   
