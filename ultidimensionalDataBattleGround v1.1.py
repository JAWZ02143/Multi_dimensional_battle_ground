#20190228_MultidimensionalDataBattleGround_v1.1
#by Jacob McClure

"""
v1.0
-Added Lists
V1.1
-added user stats
-added battle function
"""
import random



name = ""
weapon = ""
hp = 100
defence = 50
attackMod = 0


monsters = [] #name, attack, attackMod, HP

monsters.append(["Dragon","FireBall",10,100])
monsters.append(["Dwarf","Axe Throw",5,25])
monsters.append(["Orge","Club Smash",7,50])

def battle(monster):
    global hp
    while hp > 0:
        #battle display
        print("***********************")
        print("Your Hp: ", hp)
        print(monster[0],"HP: ", monster[3])
        print("***********************")
        print("(S)lash/(P)oke/(W)hip/(B)lock")
        userAttack = input()
        if userAttack == "S":
            dieRoll = random.randint(1,20)
            if dieRoll < 5:
                print("Critical Fail")
                print("You slash at the ",monster[0],"but miss and slash yourself in the foot")
                hp -= 25
            elif dieRoll < 15:
                print("You do ok")
                print("You slash at the ",monster[0],"and slightly hit the monster")
            else:
                print("Critical Hit")
                print("You Hit",monster[0]," and get a critical organ")
        if userAttack == "P":
            dieRoll = random.randint(1,20)
            if dieRoll < 5:
                print("Critical Fail")
                print("You Poke at the ",monster[0],"but miss and slash yourself in the foot")
                hp -= 25
            elif dieRoll < 15:
                print("You do ok")
                print("You Poke at the ",monster[0],"and slightly hit the monster")
            else:
                print("Critical Hit")
                print("You Hit",monster[0]," and get a critical organ")                
                
        if userAttack == "W":
            dieRoll = random.randint(1,20)
            if dieRoll < 5:
                print("Critical Fail")
                print("You Whip at the ",monster[0],"but miss and slash yourself in the foot")
                hp -= 25
            elif dieRoll < 15:
                print("You do ok")
                print("You Whip at the ",monster[0],"and slightly hit the monster")
            else:
                print("Critical Hit")
                print("You Hit",monster[0]," and get a critical organ")

print("You have",len(monsters),"monsters to beat today")

userChoice = int(input("Monster 1, 2 or 3? "))
print("You have Chosen",monsters[userChoice-1][0], "Prepare to battle")

while True:
    battle(monsters[userChoice-1])
