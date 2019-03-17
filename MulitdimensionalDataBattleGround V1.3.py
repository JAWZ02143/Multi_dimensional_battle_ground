#20190318_MulitdimensionalDataBattleGround_V1.3
#Jacob McClure
"""
v1.1 changelog
- Added user stats
- Added battle function

v1.2 Changelog
-changed names to monsters
-added more monsters

V1.3 Changelog
-Added other attacks
-Added Block

"""

#import needed libraries
import random

#user stats
name = ""
weapon = ""
attackMod = 1
hp = 100

#Blank list to store monsters in
monsters = [] #[0] name, [1]attack_str, [2]attackMod, [3]HP

#create some monsters to fight
monsters.append(["Soda Can","Sugar Rush",5,150]) 
monsters.append(["Paper","Axe Throw",5,25]) 
monsters.append(["Bag","Suffocate",25,15])
monsters.append(["Cigarette","Smoke",25,15])
monsters.append(["Gum","",25,15])
monsters.append(["Energy Drink","",25,15])

#define functions
"""
batte() will take parameters (monster) and return the 
outcome of each round of battle
"""
def battle(monster):
    global hp
    global attackMod
    print("*********************")
    print("Your HP: ",hp)
    print(monster[0],"HP: ",monster[3])
    print("*********************")     
    print("(S)tab/(P)oke/(W)hip/(B)lock")
    userInput = input()
    #error control required
    if userInput == "S": #(S)lash
        dieRoll = random.randint(1,20)
        if dieRoll < 5:
            print("Critical fail")
            print("You slash at the ",monster[0],"but miss and slash yourself in the foot")
            hp -= damage(dieRoll,attackMod,monster[2]) #monster[2] = attackModifier
        elif dieRoll < 15:
            print("You do ok")
            hp -= damage(dieRoll,attackMod,monster[2])
            monster[3] -= damage(dieRoll,attackMod,monster[2])
        else:
            print("Critical hit")
            print("You slash at the ",monster[0],"doing critical hit damage")
            monster[3] -= damage(dieRoll,attackMod,monster[2])
        
        if userAttack == "P":
            dieRoll = random.randint(1,20)
            if dieRoll < 5:
                print("Critical Fail")
                print("You Poke at the ",monster[0],"but miss and slash yourself in the foot")
                hp -= damage(dieRoll,attackMod,monster[2]) #monster[2] = attackModifier
            elif dieRoll < 15:
                print("You do ok")
                print("You Poke at the ",monster[0],"and slightly hit the monster")
                monster[3] -= damage(dieRoll,attackMod,monster[2])
            else:
                print("Critical Hit")
                print("You Hit",monster[0]," and get a critical organ")
                monster[3] -= damage(dieRoll,attackMod,monster[2])
                                
        if userAttack == "W":
            dieRoll = random.randint(1,20)
            if dieRoll < 5:
                print("Critical Fail")
                print("You Whip at the ",monster[0],"but miss and slash yourself in the foot")
                hp -= damage(dieRoll,attackMod,monster[2]) #monster[2] = attackModifier
            
            elif dieRoll < 15:
                print("You do ok")
                print("You Whip at the ",monster[0],"and slightly hit the monster")
                monster[3] -= damage(dieRoll,attackMod,monster[2])
            else:
                print("Critical Hit")
                print("You Hit",monster[0]," and get a critical organ")  
                monster[3] -= damage(dieRoll,attackMod,monster[2])
                
        if userAttack == "B":
            dieRoll = random.randint(1,20)
            if dieRoll < 5:
                print("Critical Fail")
                print("You Block! ",monster[0],"tries to attack but does no damage")
            elif dieRoll < 15:
                print("You do ok")
                print("You Block! ",monster[0],"and slightly hit the monster")
                hp -= damage(dieRoll,attackMod,monster[2]) #monster[2] = attackModifier
            else:
                print("Critical Hit")
                print("You Block! ",monster[0]," But gets past and hits you")
                hp -= damage(dieRoll,attackMod,monster[2]) #monster[2] = attackModifier                

"""
damage() calculates how much damage each attack did
returns an integer based on calculations
"""
def damage(dieRoll,attackModUser,attackModMonster):
    return dieRoll*(attackModUser*attackModMonster)/20
    
#user interface
print("You have ",len(monsters)," monsters to beat today")

#!!!! later on come back and write error checking !!!!
userChoice = int(input("Monster 1,2 or 3?"))
print("You have chosen ",monsters[userChoice-1][0]," prepare to do battle")

#LOOP until someone dies

while hp > 0 and monsters[userChoice-1][3]>0: 
    #debug
    print(monsters)
    #main battle loop
    print(battle(monsters[userChoice-1]))

#debug
print("Final HP: ",hp)
print(monsters[userChoice-1][0]," HP: ",monsters[userChoice-1][3])
    
if hp <= 0:
    print("You are dead")
if monsters[userChoice-1][3]<=0:
    print(monsters[userChoice-1][0],"is dead")
