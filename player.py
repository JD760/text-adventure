import math

class Player():

    # set player starting stats and ability according to class
    # chosen by the user
    def __init__(self, playerClass):
        # dodge - chance of an enemy attack dealing no damage
        # ranged - less damage taken by melee enemies
        # fireball - only usable 1/10 attacks, does a lot of damage
        # knight - melee weapons do more damage + resistance to melee attack
        statsByClass = {
                "assassin": {"health": 100, "damage": 5, "ability": "dodge"},
                "archer": {"health": 100, "damage": 7, "ability": "ranged"},
                "wizard": {"health": 100, "damage": 5, "ability": "fireball"},
                "knight": {"health": 100, "damage": 8, "ability": "knight"}
                    }
        stats = statsByClass[playerClass]
        self.maxHealth = stats["health"]
        self.damage = stats["damage"]
        self.ability = stats["ability"]
        self.health = self.maxHealth
        self.level = 0
        self.experience = 0
        self.maxXP = 5
        self.balance = 0
    
    
    # method to handle adding experience to the player and levelling
    # up, which involves improving some stats and abilities
    # returns the number of level-ups that have occurred
    def gainExperience(self, xp: float) -> int:
        initialLevel = self.level
        self.experience += xp
        # calculate max experience for current level
        if (self.level > 0):
            self.maxXP = (self.level * 5)
        # level up and preseve xp that goes over the level max
        while self.experience - self.maxXP >= 0:
            self.level += 1
            self.experience -= self.maxXP
            # apply stat changes for level change
            statGain = math.ceil(self.level / 2)
            self.maxHealth += statGain
            self.damage += statGain
            self.balance += statGain
            self.maxXP = self.level * 5

        return self.level - initialLevel
