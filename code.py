#code python de l'attaque des des titans ! Enjoy :D
import random
import time
import os
random_attack = True
random_damage = 0
pausedelay = 5
attacknb = 0
turn = 0
player1 = str(input("Joueur 1 Entre ton pseudo : "))
player1_hp = 250
print("Bonjour {} !".format(player1))
player2 = str(input("Joueur 2 Entre ton pseudo : "))
player2_hp = 250
print("Salut {} !".format(player2))
print("LE COMBAT COMMENCE !\n")
os.system('cls')
def attack():
    global random_attack,random_damage,player1,player1_hp,player2,player2_hp,turn,attacknb
    attacknb += 1
    print("------------------ATTAQUE N°{}-------------------".format(attacknb))
    random_attack = random.randint(0,1)
    random_attack = bool(random_attack)
    if random_attack == True:
        random_damage = random.randint(0,100)
        if turn == 0:
            player2_hp -= random_damage
            print("L'attaque de {} à infligée {}hp !\n{} se trouve maintenant avec {}hp".format(player1,random_damage,player2,player2_hp))
            turn = 1
        elif turn == 1:
            player1_hp -= random_damage
            print("L'attaque de {} à infligée {}hp !\n{} se trouve maintenant avec {}hp".format(player2,random_damage,player1,player1_hp))
            turn = 0
    else:
        if turn == 0:
            print("l'attaque de {} à échouée !".format(player1))
            turn = 1
        elif turn == 1:
            print("l'attaque de {} à échouée !".format(player2))
            turn = 0
    print("--------------Fin de l'attaque N°{}!----------------\nProchaine attaque dans {}sec\n\n".format(attacknb,pausedelay))
    if attacknb != 4:
        time.sleep(pausedelay)
for i in range(4):
    attack()
print("LE COMBAT EST TERMINEE !\nBilan de la partie :\n")
if player1_hp > player2_hp:
    print("{} ce trouve avec {}hp et {} avec {}hp\n{} à gagné !".format(player1,player1_hp,player2,player2_hp,player1))
elif player1_hp == player2_hp:
    print("{} et {} ont eux deux {}hp , il y a Match Nul !".format(player1,player2,player1_hp))
elif player1_hp < player2_hp:
    print("{} ce trouve avec {}hp et {} avec {}hp\n{} à gagné !".format(player1,player1_hp,player2,player2_hp,player2))
