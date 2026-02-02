##NOTES




import Functions
import pythonProjectVaribles

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


##Functions Imported from Functions.py
attack = Functions.attack
attackSelect = Functions.attackSelect
criticalStrike = Functions.criticalStrike
temper = Functions.temper
revengence = Functions.revengence
heal = Functions.heal
aoeAttack = Functions.aoeAttack
lifeDrain = Functions.lifeDrain
healthPotion = Functions.healthPotion
manaPotion = Functions.manaPotion
shuriken = Functions.shuriken
revive = Functions.revive
enemyAttack = Functions.enemyAttack
showInv = Functions.showInv
bossHeal = Functions.bossHeal
bossAttack = Functions.bossAttack
bossStrike = Functions.bossStrike
bossRevengence = Functions.bossRevengence
bossDrain = Functions.bossDrain
aoeBossAttack = Functions.aoeBossAttack






##Start Game
print("Welcome to the colosseum!")
while True:
    waveCount += 1
    ##Wave 1
    if waveCount == 1:
        print(f"Wave 1: a slime, a skeleton, and a goblin")
    elif waveCount == 2:
        enemies.pop(0)
        enemies.pop(0)
        enemies.pop(0)
        print("You take a short rest between waves...\n\n")
        matt[1] += 400
        if matt[1] > 1000:
            matt[1] = 1000
        natalie[1] += 300
        if natalie[1] > 750:
            natalie[1] = 750
        matt[3] += 100
        if matt[3] > 250:
            matt[3] = 250
        natalie[3] += 500
        if natalie[3] > 1500:
            natalie[3] = 1500
        print("Wave 2: A skeleton elite, a goblin chief, and a troll")
    elif waveCount == 3:
        enemies.pop(0)
        enemies.pop(0)
        enemies.pop(0)
        print("You take a short rest between waves...\n\n")
        matt[1] += 400
        if matt[1] > 1000:
            matt[1] = 1000
        natalie[1] += 300
        if natalie[1] > 750:
            natalie[1] = 750
        matt[3] += 100
        if matt[3] > 250:
            matt[3] = 250
        natalie[3] += 500
        if natalie[3] > 1500:
            natalie[3] = 1500
        print("Wave 3: A flame dragon, an ice golem, and a dark sorcerer")
    elif waveCount == 4:
        enemies.pop(0)
        enemies.pop(0)
        enemies.pop(0)
        print("You take a short rest between waves...\n\n")
        print("The colosseum has champion stand before you! ")
        matt[1] += 400
        if matt[1] > 1000:
            matt[1] = 1000
        natalie[1] += 300
        if natalie[1] > 750:
            natalie[1] = 750
        matt[3] += 100
        if matt[3] > 250:
            matt[3] = 250
        natalie[3] += 500
        if natalie[3] > 1500:
            natalie[3] = 1500
        waveCount += 1
        break


    ##MAIN GAME LOOP
    while True:
        roundCounter += 1
        if roundCounter > currentTurn + 4:
            matt[6] = 1
        print(f"{enemies[0][0]} has {enemies[0][1]} health \n{enemies[1][0]} has {enemies[1][1]} health \n{enemies[2][0]} has {enemies[2][1]} health")
        print(f"\nMatt has {matt[1]} health and {matt[3]} mana, Natalie has {natalie[1]} health and {natalie[3]} mana\n")

        ###Matt's Turn###
        if matt[4] == False:
            turnChoice = int(input("\nChoose you move for Matt: \n1. Attack \n2. Skills \n3. Items \n\n"))
            if turnChoice == 1:
                damage = attack(matt[2], matt[6])
                mobSelect = int(input(f"Choose your target: \n1. {enemies[0][0]} \n2. {enemies[1][0]} \n3. {enemies[2][0]} \n\n")) - 1
                attackSelect(mobSelect, damage)
            elif turnChoice == 2:
                for i in range(1, len(mattSkillList), 2):
                    print(f"{int((i + 1)/2)}. {mattSkillList[i]}\n")
                skillChoice = int(input("\nChoose your skill: 1-3\n\n"))
                if skillChoice == 1:
                    criticalStrike()
                elif skillChoice == 2:
                    temper()
                    currentTurn = roundCounter
                elif skillChoice == 3:
                    revengence()
            elif turnChoice == 3:
                itemNum = int(input(f"Pick an item: \n\n{showInv()}")) - 1
                itemChoice = inventory[itemNum]
                if itemChoice == "Health Potion":
                    matt[1] = healthPotion(matt[1], matt[5])
                    inventory.pop(itemNum)
                    print(f"Matt's health is now {matt[1]}\n\n")
                elif itemChoice == "Mana Potion":
                    matt[3] = manaPotion(matt[3], matt[5])
                    inventory.pop(itemNum)
                    print(f"Matt's mana is now {matt[3]}\n\n")
                elif itemChoice == "Shuriken":
                    damage = shuriken()
                    mobSelect = int(input(f"Choose your target: \n1. {enemies[0][0]} \n2. {enemies[1][0]} \n3. {enemies[2][0]} \n\n")) - 1
                    attackSelect(mobSelect, damage)
                    inventory.pop(itemNum)
                elif itemChoice == "revive":
                    revive(natalie[5], natalie[4])
                    print(f"Natalie's health is now {natalie[1]}\n\n")
                    inventory.pop(itemNum)

        ###Win Check###
        if enemies[0][1] == 0 and enemies[1][1] == 0 and enemies[2][1] == 0:
            print("You beat the Wave!\n\n")
            break


        ###Natalie's Turn###
        if natalie[4] == False:
            turnChoice = int(input("\nChoose you move for Natalie: \n1. Attack \n2. Skills \n3. Items \n\n"))
            if turnChoice == 1:
                damage = attack(natalie[2], 1)
                mobSelect = int(input(f"Choose your target: \n1. {enemies[0][0]} \n2. {enemies[1][0]} \n3. {enemies[2][0]} \n\n")) - 1
                attackSelect(mobSelect, damage)
            elif turnChoice == 2:
                for i in range(1, len(natSkillList), 2):
                    print(f"{int((i + 1) / 2)}. {natSkillList[i]}\n")
                skillChoice = int(input("\nChoose your skill: 1-3\n\n"))
                if skillChoice == 1:
                    heal()
                elif skillChoice == 2:
                    aoeAttack(300)
                elif skillChoice == 3:
                    damage = 600
                    mobSelect = int(input(f"Choose your target: \n1. {enemies[0][0]} \n2. {enemies[1][0]} \n3. {enemies[2][0]} \n\n")) - 1
                    lifeDrain(damage, mobSelect)
            elif turnChoice == 3:
                itemNum = int(input(f"Pick an item: \n\n{showInv()}")) - 1
                itemChoice = inventory[itemNum]
                if itemChoice == "Health Potion":
                    natalie[1] = healthPotion(natalie[1], natalie[5])
                    inventory.pop(itemNum)
                    print(f"Natalie's health is now {natalie[1]}\n\n")
                elif itemChoice == "Mana Potion":
                    natalie[3] = manaPotion(natalie[3], natalie[5])
                    inventory.pop(itemNum)
                    print(f"Natalie's mana is now {natalie[3]}\n\n")
                elif itemChoice == "Shuriken":
                    damage = shuriken()
                    mobSelect = int(input(f"Choose your target: \n1. {enemies[0][0]} \n2. {enemies[1][0]} \n3. {enemies[2][0]} \n\n")) - 1
                    attackSelect(mobSelect, damage)
                    inventory.pop(itemNum)
                elif itemChoice == "revive":
                    revive(matt[5], matt[4])
                    print(f"Matt's health is now {matt[1]}\n\n")
                    inventory.pop(itemNum)

        ###Enemy's Turn###
        enemyAttack()
        ###Loss Check###
        if matt[4] == True and natalie[4] == True:
            print("You Lost")
            break

        ###Win Check###
        if enemies[0][1] == 0 and enemies[1][1] == 0 and enemies[2][1] == 0:
            print("You beat the Wave!\n\n")
            break

        print(f"\n\n\n-----------------------------Turn {roundCounter} over-----------------------------\n\n\n")



############################BOSS WAVE########################################

if waveCount > 4:
    while True:
        roundCounter += 1
        if roundCounter > currentTurn + 4:
            matt[6] = 1
        print(f"{enemies[0][0]} has {enemies[0][1]} health")
        print(f"\nMatt has {matt[1]} health and {matt[3]} mana, Natalie has {natalie[1]} health and {natalie[3]} mana\n")

        ###Matt's Turn###
        if matt[4] == False:
            turnChoice = int(input("\nChoose you move for Matt: \n1. Attack \n2. Skills \n3. Items \n\n"))
            if turnChoice == 1:
                damage = attack(matt[2], matt[6])
                attackSelect(0, damage)
            elif turnChoice == 2:
                for i in range(1, len(mattSkillList), 2):
                    print(f"{int((i + 1)/2)}. {mattSkillList[i]}\n")
                skillChoice = int(input("\nChoose your skill: 1-3\n\n"))
                if skillChoice == 1:
                    bossStrike()
                elif skillChoice == 2:
                    temper()
                    currentTurn = roundCounter
                elif skillChoice == 3:
                    bossRevengence()
            elif turnChoice == 3:
                itemNum = int(input(f"Pick an item: \n\n{showInv()}")) - 1
                itemChoice = inventory[itemNum]
                if itemChoice == "Health Potion":
                    matt[1] = healthPotion(matt[1], matt[5])
                    inventory.pop(itemNum)
                    print(f"Matt's health is now {matt[1]}\n\n")
                elif itemChoice == "Mana Potion":
                    matt[3] = manaPotion(matt[3], matt[5])
                    inventory.pop(itemNum)
                    print(f"Matt's mana is now {matt[3]}\n\n")
                elif itemChoice == "Shuriken":
                    damage = shuriken()
                    attackSelect(0, damage)
                    inventory.pop(itemNum)
                elif itemChoice == "revive":
                    revive(natalie[5], natalie[4])
                    print(f"Natalie's health is now {natalie[1]}\n\n")
                    inventory.pop(itemNum)

        ###Win Check###
        if enemies[0][1] == 0:
            print("You beat the Champion!!!\n\n")
            break


        ###Natalie's Turn###
        if natalie[4] == False:
            turnChoice = int(input("\nChoose you move for Natalie: \n1. Attack \n2. Skills \n3. Items \n\n"))
            if turnChoice == 1:
                damage = attack(natalie[2], 1)
                attackSelect(0, damage)
            elif turnChoice == 2:
                for i in range(1, len(natSkillList), 2):
                    print(f"{int((i + 1) / 2)}. {natSkillList[i]}\n")
                skillChoice = int(input("\nChoose your skill: 1-3\n\n"))
                if skillChoice == 1:
                    heal()
                elif skillChoice == 2:
                    aoeBossAttack(300)
                elif skillChoice == 3:
                    damage = 600
                    bossDrain(damage)
            elif turnChoice == 3:
                itemNum = int(input(f"Pick an item: \n\n{showInv()}")) - 1
                itemChoice = inventory[itemNum]
                if itemChoice == "Health Potion":
                    natalie[1] = healthPotion(natalie[1], natalie[5])
                    inventory.pop(itemNum)
                    print(f"Natalie's health is now {natalie[1]}\n\n")
                elif itemChoice == "Mana Potion":
                    natalie[3] = manaPotion(natalie[3], natalie[5])
                    inventory.pop(itemNum)
                    print(f"Natalie's mana is now {natalie[3]}\n\n")
                elif itemChoice == "Shuriken":
                    damage = shuriken()
                    attackSelect(0, damage)
                    inventory.pop(itemNum)
                elif itemChoice == "revive":
                    revive(matt[5], matt[4])
                    print(f"Matt's health is now {matt[1]}\n\n")
                    inventory.pop(itemNum)
        ###Enemy's Turn###
        bossHeal()
        bossAttack()

        ###Loss Check###
        if matt[4] == True and natalie[4] == True:
            print("You Lost")
            break

        ###Win Check###
        if enemies[0][1] == 0:
            print("You beat the Champion!!!\n\n")
            print("Congratulations!!!\n\n")
            print("You have beaten the colosseum!!!\n\n")
            break




