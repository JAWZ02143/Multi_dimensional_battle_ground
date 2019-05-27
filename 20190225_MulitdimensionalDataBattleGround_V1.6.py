#20190509_MulitdimensionalDataBattleGround_V1.6
#Jacob McClure
"""
v1.1 changelog
- Added user stats
- Added battle function

v1.2 Changelog
-changed names to trash
-added more trash

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

#Blank list to store trash in
trash = [] #[0] name, [1]attack_str, [2]attackMod, [3]HP

#create some trash to fight
trash.append(["Soda Can","Sugar Rush",5,25]) 
trash.append(["Paper","Axe Throw",5,25])
trash.append(["Bag","Suffocate",25,50])
trash.append(["Cigarette","Smoke",25,50])
trash.append(["Gum","Stick",25,35])
trash.append(["Energy Drink","Strong Sugar Rush",25,150])

#define functions
"""
batte() will take parameters (rubbish) and return the 
outcome of each round of battle
"""
def battle(rubbish):
    global hp
    #global attackMod
    print("*********************")
    print("Your HP: ",hp)
    print(rubbish[0],"HP: ",rubbish[3])
    print("*********************")     
    print("(S)tab/(P)oke/(W)hip/(B)lock")
    userInput = input()
    #error control required
    if userInput.upper() == "S": #(S)tab
        dieRoll = random.randint(1,20)
        if dieRoll < 5:
            print("Critical fail")
            print("You Stab at the",rubbish[0],"but miss and Stab yourself in the foot")
            hp -= damage(dieRoll,attackMod,rubbish[2]) #rubbish[2] = attackModifier
        elif dieRoll < 15:
            print("You do ok")
            hp -= damage(dieRoll,attackMod,rubbish[2])
            rubbish[3] -= damage(dieRoll,attackMod,rubbish[2])
        else:
            print("Critical hit")
            print("You Stab at the",rubbish[0],"doing critical hit damage")
            rubbish[3] -= damage(dieRoll,attackMod,rubbish[2]*2)
        
    if userInput.upper() == "P":
        dieRoll = random.randint(1,20)
        if dieRoll < 5:
            print("Critical Fail")
            print("You Poke at the ",rubbish[0],"but miss and slash yourself in the foot")
            hp -= damage(dieRoll,attackMod,rubbish[2]) #rubbish[2] = attackModifier
        elif dieRoll < 15:
            print("You do ok")
            print("You Poke at the ",rubbish[0],"and slightly hit the rubbish")
            rubbish[3] -= damage(dieRoll,attackMod,rubbish[2])
        else:
            print("Critical Hit")
            print("You Hit",rubbish[0]," and get a critical organ")
            rubbish[3] -= damage(dieRoll,attackMod,rubbish[2])
                                
    if userInput.upper() == "W":
        dieRoll = random.randint(1,20)
        if dieRoll < 5:
            print("Critical Fail")
            print("You Whip at the ",rubbish[0],"but miss and slash yourself in the foot")
            hp -= damage(dieRoll,attackMod,rubbish[2]) #rubbish[2] = attackModifier
        
        elif dieRoll < 15:
            print("You do ok")
            print("You Whip at the ",rubbish[0],"and slightly hit the rubbish")
            rubbish[3] -= damage(dieRoll,attackMod,rubbish[2])
        else:
            print("Critical Hit")
            print("You Hit",rubbish[0]," and get a critical organ")  
            rubbish[3] -= damage(dieRoll,attackMod,rubbish[2])
            
    if userInput.upper() == "B":
        dieRoll = random.randint(1,20)
        if dieRoll < 5:
            print("You Block! ",rubbish[0],"tries to attack but does no damage")
        elif dieRoll < 15:
            print("You Block! ")
        else:
            print("You Block! ",rubbish[0]," But gets past and hits you")
            hp -= damage(dieRoll,attackMod,rubbish[2]) #rubbish[2] = attackModifier
    #else:
        #print("that was not one of the options")

"""
damage() calculates how much damage each attack did
returns an integer based on calculations
"""
def damage(dieRoll,attackModUser,attackModMonster):
    return dieRoll*(attackModUser*attackModMonster)/20

while len(trash) >0:    
    #user interface
    print("You have ",len(trash)," pieces of rubbish to clean up today")
    
    #!!!! later on come back and write error checking !!!!
    i = 1
    for rubbish in trash:
        
        print(i, " - ",rubbish[0])
        i +=1
    validInput = False
    while validInput == False:
        try:
            userChoice = int(input("Trash Piece #: "))
            if userChoice >0 and userChoice < len(trash)+1:
                validInput = True
            else:
                print("No")
        except ValueError:
            print("Not a number")
    print("You have chosen ",trash[userChoice-1][0]," prepare to do battle")
    
    #LOOP until someone dies



    while hp > 0 and trash[userChoice-1][3]>0: 
        #debug
        #print(trash)
        #main battle loop
        battle(trash[userChoice-1])
    
    #debug
    print("Final HP: ",hp)
    print(trash[userChoice-1][0]," HP: ",trash[userChoice-1][3])
        
    if hp <= 0:
        print("You are dead")
        time.sleep(5)
        break
    if trash[userChoice-1][3]<=0:
        print(trash[userChoice-1][0],"is dead")
        trash.remove(trash[userChoice-1])
        time.sleep(5)
    if len(trash) <= 0:
        print("you won")
        time.sleep(5)
        break