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
        self.health = stats["health"]
        self.damage = stats["damage"]
        self.ability = stats["ability"]
        self.level = 0
        self.experience = 0
        self.balance = 0
    
    
    # method to handle adding experience to the player and levelling
    # up, which involves improving some stats and abilities
    # returns True if xp gain causes a level up
    def gainExperience(self, xp: float) -> bool:
        initialLevel = self.level
        self.experience += xp
        # calculate max experience for current level
        if (self.level == 0):
            maxXP = 5
        else:
            maxXP = (self.level * 5)
        # level up and preseve xp that goes over the level max
        while self.experience - maxXP >= 0:
            self.level += 1
            self.experience -= maxXP
            # apply stat changes for level change
            statGain = math.ceil(self.level / 2)
            self.health += statGain
            self.damage += statGain
            self.balance += statGain
            maxXP = self.level * 5

        return self.level - initialLevel