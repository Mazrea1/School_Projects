import pythonProjectVaribles
import random


##Variables Imported from pythonProjectVaribles.py
roundCounter = pythonProjectVaribles.roundCounter
currentTurn = pythonProjectVaribles.currentTurn
waveCount = pythonProjectVaribles.waveCount
matt = pythonProjectVaribles.matt
natalie = pythonProjectVaribles.natalie
enemies = pythonProjectVaribles.enemies
inventory = pythonProjectVaribles.inventory
mattSkillList = pythonProjectVaribles.mattSkillList
natSkillList = pythonProjectVaribles.natSkillList


###Functions###
def attack(Attack, Buff):
    damage = Attack * Buff
    return damage

def attackSelect(mobSelect, damage):
    if enemies[mobSelect][1] == 0:
        print(f"{enemies[mobSelect][0]} is already defeated, you attacked the air 🤦\n\n")
    else:
        enemies[mobSelect][1] -= damage
        if enemies[mobSelect][1] <= 0:
            print(f"{enemies[mobSelect][0]} has been defeated!")
            enemies[mobSelect] = ["defeated enemy", 0, 0]
        else:
            print(f"You did {damage} damage to {enemies[mobSelect][0]}\n\n")

def aoeAttack(damage):
    enemies[0][1] -= damage
    enemies[1][1] -= damage
    enemies[2][1] -= damage
    if enemies[0][1] <= 0:
        print(f"{enemies[0][0]} has been defeated!")
        enemies[0] = ["defeated enemy", 0, 0]
    if enemies[1][1] <= 0:
        print(f"{enemies[1][0]} has been defeated!")
        enemies[1] = ["defeated enemy", 0, 0]
    if enemies[2][1] <= 0:
        print(f"{enemies[2][0]} has been defeated!")
        enemies[2] = ["defeated enemy", 0, 0]
    natalie[3] -= 150


def showInv():
    output = ""
    for i in range(len(inventory)):
        output += f" {i + 1}. {inventory[i]}\n"
    return output


def enemyPlayerSelect():
    x = random.randint(1, 2)
    if matt[4] == True:
        target = natalie[0]
    elif natalie[4] == True:
        target = matt[0]
    else:
        if x == 1:
            target = matt[0]
        else:
            target = natalie[0]
    return target

def enemyAttack():
    if enemies[0][1] <= 0:
        pass
    elif enemies[0][1] >= 0:
        if enemyPlayerSelect() == matt[0]:
            matt[1] -= enemies[0][2]
            print(f"{enemies[0][0]} did {enemies[0][2]} damage to {matt[0]}.")
        else:
            natalie[1] -= enemies[0][2]
            print(f"{enemies[0][0]} did {enemies[0][2]} damage to {natalie[0]}.")
    if enemies[1][1] <= 0:
        pass
    elif enemies[1][1] >= 0:
        if enemyPlayerSelect() == matt[0]:
            matt[1] -= enemies[1][2]
            print(f"{enemies[1][0]} did {enemies[1][2]} damage to {matt[0]}.")
        else:
            natalie[1] -= enemies[1][2]
            print(f"{enemies[1][0]} did {enemies[1][2]} damage to {natalie[0]}.")
    if enemies[2][1] <= 0:
        pass
    elif enemies[2][1] >= 0:
        if enemyPlayerSelect() == matt[0]:
            matt[1] -= enemies[2][2]
            print(f"{enemies[2][0]} did {enemies[2][2]} damage to {matt[0]}.\n\n")
        else:
            natalie[1] -= enemies[2][2]
            print(f"{enemies[2][0]} did {enemies[2][2]} damage to {natalie[0]}.\n\n")
    if matt[1] <= 0:
        matt[4] = True
        matt[1] = 0
        print("Matt has been defeated!\n\n")
    if natalie[1] <= 0:
        natalie[4] = True
        natalie[1] = 0
        print("Natalie has been defeated!\n\n")






###Items###
def healthPotion(health, iden):
    health += 300
    if health >= 1000 and iden == 1:
        health = 1000
        return health
    elif health >= 750 and iden == 2:
        return health
    else:
        return health

def manaPotion(mana, iden):
    mana += 200
    if mana >= 250 and iden == 1:
        mana = 250
        return mana
    elif mana >= 1500 and iden == 2:
        mana = 1500
        return mana
    else:
        return mana

def shuriken():
    damage = 250
    return damage

def revive(name, death):
    if name == 1:
        if death == True:
            matt[4] = False
            matt[1] += 600
    if name == 2:
        if death == True:
            natalie[4] = False
            natalie[1] += 600
    else:
        print(f"{name} is not dead and cannot be revived.")





###Skills###

def revengenceCalculation(health, attack, buff):
    if health <= matt[7] * 0.3:
        damage = attack * buff * 4
    elif health <= matt[7] * 0.5:
        damage = attack * buff * 2
    elif health <= matt[7] * 0.75:
        damage = attack * buff * 1.5
    else:
        damage = attack * buff
    return damage

def revengence():
    if matt[3] < 100:
        print("Not enough mana")
    else:
        damage = revengenceCalculation(matt[1], matt[2], matt[6])
        mobSelect = int(input(f"Choose your target: \n1. {enemies[0][0]} \n2. {enemies[1][0]} \n3. {enemies[2][0]} \n\n")) - 1
        matt[3] -= 100
        attackSelect(mobSelect, damage)

def criticalStrike():
    if matt[3] < 30:
        print("Not enough mana")
    else:
        damage = attack((matt[2] * 2), matt[6])
        mobSelect = int(input(f"Choose your target: \n1. {enemies[0][0]} \n2. {enemies[1][0]} \n3. {enemies[2][0]} \n\n")) - 1
        matt[3] -= 30
        attackSelect(mobSelect, damage)

def temper():
    if matt[3] < 40:
        print("Not enough mana")
    else:
        if matt[6] == 1:
            matt[6] += 2
            matt[3] -= 40
            print("Matt's attack has been tripled for 3 turns\n\n")
        else:
            print("Can't not be used. Effect is still in place")

def heal():
    if natalie[3] < 80:
        print("Not enough mana")
    else:
        natalie[1] += 700
        matt[1] += 700
        natalie[3] -= 40
        if natalie[1] > 750:
            natalie[1] = 750
            print("Natalie's health is full!\n\n")
        if matt[1] > 1000:
            matt[1] = 1000
            print("Matt,'s health is full!\n\n")
        natalie[3] -= 80

        print(f"Natalie's health is now {natalie[1]}\n")
        print(f"Matt's health is now {matt[1]}\n\n")

def lifeDrain(damage, mobSelect):
    if natalie[3] < 80:
        print("Not enough mana")
    else:
        if enemies[mobSelect][2] == 0:
            print(f"{enemies[mobSelect][0]} is already defeated, you healed nothing 🤦\n\n")
        elif enemies[mobSelect][1] < damage:
            natalie[1] += enemies[mobSelect][1]
            print(f"You drained {enemies[mobSelect][1]} health from {enemies[mobSelect][0]}\n\n")
            enemies[mobSelect][1] -= damage
            if enemies[mobSelect][1] <= 0:
                print(f"{enemies[mobSelect][0]} has been defeated!")
                enemies[mobSelect] = ["defeated enemy", 0, 0]
        else:
            enemies[mobSelect][1] -= damage
            natalie[1] += damage
            print(f"You drained {damage} health from {enemies[mobSelect][0]}\n\n")

        if natalie[1] > 750:
            natalie[1] = 750
            print("Natalie's health is full!\n\n")
        natalie[3] -= 80





###Champion's attack###

def bossHeal():
    enemies[0][1] += 200

def rageOfThePantheon():
    if enemies[0][1] <= 0:
        pass
    elif enemies[0][1] >= 0:
        if enemyPlayerSelect() == matt[0]:
            matt[1] -= enemies[0][2] * 2
            print(f"{enemies[0][0]} did {enemies[0][2] * 2} damage to {matt[0]}.")
        else:
            natalie[1] -= enemies[0][2] * 2
            print(f"{enemies[0][0]} did {enemies[0][2] * 2} damage to {natalie[0]}.")
    if matt[1] <= 0:
        matt[4] = True
        matt[1] = 0
        print("Matt has been defeated!\n\n")
    if natalie[1] <= 0:
        natalie[4] = True
        natalie[1] = 0
        print("Natalie has been defeated!\n\n")

def tidesOfPosiden():
    if enemies[0][1] <= 0:
        pass
    elif enemies[0][1] >= 0:
        matt[1] -= enemies[0][2]
        natalie[1] -= enemies[0][2]
        print(f"{enemies[0][0]} did {enemies[0][2]} damage to {matt[0]}.")
        print(f"{enemies[0][0]} did {enemies[0][2]} damage to {natalie[0]}.")
    if matt[1] <= 0:
        matt[4] = True
        matt[1] = 0
        print("Matt has been defeated!\n\n")
    if natalie[1] <= 0:
        natalie[4] = True
        natalie[1] = 0
        print("Natalie has been defeated!\n\n")

def bossAttack():
    x = random.randint(1, 2)
    if x == 1:
        rageOfThePantheon()
    elif x == 2:
        tidesOfPosiden()




def bossStrike():
    if matt[3] < 30:
        print("Not enough Mana")
    else:
        damage = attack((matt[2] * 2), matt[6])
        matt[3] -= 30
        attackSelect(0, damage)

def bossRevengence():
    if matt[3] < 100:
        print("Not enough Mana")
    else:
        damage = revengenceCalculation(matt[1], matt[2], matt[6])
        matt[3] -= 100
        attackSelect(0, damage)

def bossDrain(damage):
    if natalie[3] < 80:
        print("Not enough Mana")
    else:
        if enemies[0][2] == 0:
            print(f"{enemies[0][0]} is already defeated, you healed nothing 🤦\n\n")
        elif enemies[0][1] < damage:
            natalie[1] += enemies[0][1]
            print(f"You drained {enemies[0][1]} health from {enemies[0][0]}\n\n")
            enemies[0][1] -= damage
            if enemies[0][1] <= 0:
                print(f"{enemies[0][0]} has been defeated!")
                enemies[0] = ["defeated enemy", 0, 0]
        else:
            enemies[0][1] -= damage
            natalie[1] += damage
            print(f"You drained {damage} health from {enemies[0][0]}\n\n")
        if natalie[1] > 750:
            natalie[1] = 750
            print("Natalie's health is full!\n\n")
        natalie[3] -= 80

def aoeBossAttack(damage):
    if natalie[3] < 80:
        print("Not enough Mana")
    else:
        enemies[0][1] -= damage
        if enemies[0][1] <= 0:
            print(f"{enemies[0][0]} has been defeated!")
            enemies[0] = ["defeated enemy", 0, 0]
        natalie[3] -= 150