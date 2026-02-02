roundCounter = 0
currentTurn = 0
waveCount = 0

###Player Stuff###

##Melee Fighter(Matt) [Name, Health, Attack, Mana, Death, iden, buff, maxHP]
matt = ["Matt", 1000, 150, 250, False, 1, 1, 1000]
#2nd is an attack that does 1.5x damage, 3rd is a buff that adds 100 attack for 3 turns, 4th is an attack that scales off of remaining health
mattSkillList = [20, "critical strike", 40, "Temper", 50, "Revengeance"]

##Magic Fighter(Natalie)[Name, Health, Attack, Mana, Death, Iden]
natalie = ["Natalie", 750, 100, 1500, False, 2]
natSkillList = [60, "heal", 70, "fireball", 80, "life drain"]


###Wave Mobs###
enemies = [["slime", 300, 30], ["skeleton", 250, 40], ["goblin", 400, 15], ["Skeleton Elite", 600, 80], ["goblin chief", 800, 50], ["troll", 1200, 65], ["Flame Dragon", 2000, 100], ["Ice Golem", 1800, 70], ["Dark Sorcerer", 1200, 90], ["Oddyseous", 5000, 250]]


inventory = ["Health Potion", "Health Potion", "Health Potion", "Mana Potion", "Mana Potion", "Mana Potion", "Shuriken", "Shuriken", "Shuriken", "revive", "revive"]
