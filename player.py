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
        self.fireballTurns = 0 # num turns since fireball used
    
    
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


    # method to handle an enemy attack 
    # damage -> the damage of the attacking enemy
    # enemyAbility -> the type of incoming attack
    # return: amount of health lost
    def takeDamage(self, damage: int, attackType: str = "") -> int:
        damageModifier: int = 1 # this is changed by abilities 
        if player.ability == "dodge":
            if random.randint(1,10) <= 3:
                print("You dodged the enemy attack")
                return 0
        elif player.ability == "ranged":
            if attackType != "ranged" and attackType != "":
                # 1/4 less damage taken if not ranged attack
                damageModifier = 0.75
        elif player.ability == "knight":
            if attackType == "melee":
                damageModifier = 0.6
        else:
            # something has gone wrong 
            return -1
        player.health -= math.floor(damage * damageModifier)
        return math.floor(damage * damageModifier)
