#20190509_MulitdimensionalDataBattleGround_V1.5
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
import time

#user stats
name = ""
weapon = ""
attackMod = 1
hp = 100

#Blank list to store monsters in
monsters = [] #[0] name, [1]attack_str, [2]attackMod, [3]HP

#create some monsters to fight
monsters.append(["Soda Can","Sugar Rush",5,25]) 
monsters.append(["Paper","Axe Throw",5,25]) 
monsters.append(["Bag","Suffocate",25,50])
monsters.append(["Cigarette","Smoke",25,50])
monsters.append(["Gum","Stick",25,35])
monsters.append(["Energy Drink","Strong Sugar Rush",25,150])

#define functions
"""
batte() will take parameters (monster) and return the 
outcome of each round of battle
"""
def battle(monster):
    global hp
    #global attackMod
    print("*********************")
    print("Your HP: ",hp)
    print(monster[0],"HP: ",monster[3])
    print("*********************")     
    print("(S)tab/(P)oke/(W)hip/(B)lock")
    userInput = input()
    #error control required
    if userInput.upper() == "S": #(S)tab
        dieRoll = random.randint(1,20)
        if dieRoll < 5:
            print("Critical fail")
            print("You Stab at the",monster[0],"but miss and Stab yourself in the foot")
            hp -= damage(dieRoll,attackMod,monster[2]) #monster[2] = attackModifier
        elif dieRoll < 15:
            print("You do ok")
            hp -= damage(dieRoll,attackMod,monster[2])
            monster[3] -= damage(dieRoll,attackMod,monster[2])
        else:
            print("Critical hit")
            print("You Stab at the",monster[0],"doing critical hit damage")
            monster[3] -= damage(dieRoll,attackMod,monster[2]*2)
        
    if userInput.upper() == "P":
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
                                
    if userInput.upper() == "W":
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
            
    if userInput.upper() == "B":
        dieRoll = random.randint(1,20)
        if dieRoll < 5:
            print("You Block! ",monster[0],"tries to attack but does no damage")
        elif dieRoll < 15:
            print("You Block! ")
        else:
            print("You Block! ",monster[0]," But gets past and hits you")
            hp -= damage(dieRoll,attackMod,monster[2]) #monster[2] = attackModifier
    #else:
        #print("that was not one of the options")

"""
damage() calculates how much damage each attack did
returns an integer based on calculations
"""
def damage(dieRoll,attackModUser,attackModMonster):
    return dieRoll*(attackModUser*attackModMonster)/20

while len(monsters) >0:    
    #user interface
    print("You have ",len(monsters)," monsters to beat today")
    
    #!!!! later on come back and write error checking !!!!
    i = 1
    for monster in monsters:
        
        print(i, " - ",monster[0])
        i +=1
    
    userChoice = int(input("Monster #: "))
    print("You have chosen ",monsters[userChoice-1][0]," prepare to do battle")
    
    #LOOP until someone dies



    while hp > 0 and monsters[userChoice-1][3]>0: 
        #debug
        #print(monsters)
        #main battle loop
        battle(monsters[userChoice-1])
    
    #debug
    print("Final HP: ",hp)
    print(monsters[userChoice-1][0]," HP: ",monsters[userChoice-1][3])
        
    if hp <= 0:
        print("You are dead")
        time.sleep(5)
    if monsters[userChoice-1][3]<=0:
        print(monsters[userChoice-1][0],"is dead")
        monsters.remove(monsters[userChoice-1])
        time.sleep(5)
