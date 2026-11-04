'''
made with love
'''

from time import * ; from random import * ; from colorama import *

class chara:
    '''
    Classe pour la création du personnage contenant son nom, sa classe, sa vie, son type de magie, son mana et son * de dégat, le nom de l'arme, sa dura, le niveau, son xp et son argent
    '''
    def __init__(self, nom, classe, vie, vie_max, magika, mana, degat, arme, dura_arme, lvl, xp, argent):
        self.nom=nom
        self.classe=classe
        self.vie_base=vie
        self.lvl=lvl
        self.vie_max=self.get_maxvie()
        self.vie=self.vie_max
        self.magika=magika
        self.mana=mana
        self.degat=degat
        self.arme=arme
        self.xp=xp
        self.dura=dura_arme
        self.argent=argent

    def get_maxvie(self):
        return int(self.vie_base*(1+0.15*(self.lvl-1)))
    def set_maxvie(self):
        self.vie=self.get_maxvie()
        return self.vie
class mobs:
    '''
    Classe pour la création des mobs : nom, pv, race (abandonné tbh), son type de magie (aussi mdrr), * de degat, argent drop et xp drop
    '''
    def __init__(self, nom, pv, race, magika, mana, degat, argent, xp):
        self.nom=nom
        self.race=race
        self.magika=magika
        self.degat=degat
        self.argent=argent
        self.pv=pv
        self.pv_max=pv
        self.xp=xp
        self.mana=mana
class arme:
    '''
    Classe pour la création des armes : nom de l'arme, son * de degat, la dura et le prix a l'armurie
    '''
    def __init__(self, nom, degat, durabilite, prix):
        self.nom=nom
        self.degat=degat
        self.dura=durabilite
        self.prix=prix
class objet:
    '''
    Classe pour la création des objets : nom de l'objet, sa quantité dans le sac a dos, le prix au vendeur, sa rareté et son ID
    '''
    def __init__(self, nom, quantite, prix, rarete, ID):
        self.nom=nom
        self.quantite=quantite
        self.prix=prix
        self.rarete=rarete
        self.ID=ID

############## mon bullshit d'amour ##############

# FONCTION VÉRIFIANT SI LES PERSOS ONT DES ARMES POUR SE BATTRE
def lookup_arme(List_player):
    for i in List_player:
        if i.dura==0:
            print("Vous ne pouvez pas vous battre car " + i.nom + " n'a plus d'arme.")
            return 0
    return 1

# FONCTION POUR CHOISIR UN ENEMI EN FONCTION DE LA DIFFICULTÉ DU MONDE
def rdm_enemi():
    if diff==10:
        enemi=garde_1
    if diff==11:
        enemi=garde_2
    if diff==12:
        enemi=mini_boss1
    if diff==1:
        enemi=choice(diff1)
    if diff==2:
        enemi=choice(diff2)
    if diff==3:
        enemi=choice(diff3)
    enemi.pv=enemi.pv_max
    return enemi

# FONCTION CALCUL TOTAL DU HEAL DE L'ÉQUIPE
def totalpv(List_player):
    totalheal=0
    for i in List_player:
        totalheal+=i.vie
    return totalheal

# FONCTION POUR LES COMBATS "BASIQUES" (pas les minis boss + bossfinal)
def fight():
    arme_equipe=lookup_arme(List_player)
    if arme_equipe==1:
        enemi=rdm_enemi()
        print("\nUn " + str(enemi.nom) + " apparait et il a " + str(enemi.pv) + "pv.")
        while totalpv(List_player)>0 and enemi.pv>0:
            for k in List_player:
                affichage_combat(k, enemi, List_player)
                print(k.nom + " attaque  ->  il lui reste " + str(enemi.pv) + "pv.\n")
            if enemi.pv>0:
                cible=attack_enemi(enemi,List_player)
                print(enemi.nom + " attaque " + cible.nom + "  ->  " + str(cible.vie) + "pv.")
        for i in List_player:
            i.xp+=enemi.xp
        lvlup()
        for i in List_player:
            i.dura-=1
    else:
        print("Vous ne pouvez pas vous battre car vous n'avez pas d'arme.")
        armurerie()
        fight()

# FONCTION POUR L'AFFICHAGE DES COMBATS
def affichage_combat(k,enemi,List_player):
    if stade_equipe==0:
        print(character.nom + " : " + str(character.vie) + "pv / Andy : " + str(Andy.vie) + "pv")
    elif stade_equipe==1:
        print(character.nom + " : " + str(character.vie) + "pv / Nathaniel : " + str(Nath.vie) + "pv / Andy : " + str(Andy.vie) + "pv")
    elif stade_equipe==2:
        print(character.nom + " : " + str(character.vie) + "pv / Nathaniel : " + str(Nath.vie) + "pv / Andy : " + str(Andy.vie) + "pv / Éthan : " + str(Ethan.vie) + "pv")
    elif stade_equipe==3:
        print(character.nom + " : " + str(character.vie) + "pv")
    move=int(input("-------------------------------------\nTour de " + k.nom + " (" + str(k.mana) + " mana)" +"\n1 = attaque  /  2 = magie / 3 = Objet\n--------------------------------------\n"))
    if move==1:
        attack(k,enemi)
    elif move==2:
        if k.mana<=10:
            print("Vous n'avez pas assez de Mana pour attaquer")
        else:    
            magie(k,enemi,List_player)
    elif move==3:
        backpack(bp, k)

# FONCTION POUR ATTAQUE PHYSIQUE
def attack(k,enemi):
    enemi.pv-=5*k.degat*k.lvl
    return enemi

# FONCTION POUR LA MAGIE / LES SORTS
def magie(k,enemi,List_player):
    if k==character:           # sorts du mc
        if character.magika==1:         # sorts de feu
            sort=int(input("--------------------------\n1 = Boule de feu (-10 mana) /  2 = Agidyne (-20mana)\n--------------------------\n"))
            if sort==1:
                enemi.pv-=randint(5,10)*k.degat*k.lvl
                k.mana-=10
            if sort==2:
                if k.mana<20:
                    print("Vous n'avez pas assez de Mana pour attaquer")
                else:
                    enemi.pv-=randint(7,15)*k.degat*k.lvl
                    k.mana-=20
        elif character.magika==2:       # sort d'eau
            sort=int(input("--------------------------\n1 = Ébulition (-10 mana) /  2 = Hydrocanon (-20mana)\n--------------------------\n"))
            if sort==1:
                enemi.pv-=randint(5,10)*k.degat*k.lvl
                k.mana-=10
            if sort==2:
                if k.mana<20:
                    print("Vous n'avez pas assez de Mana pour attaquer")
                else:
                    enemi.pv=randint(7,15)*k.degat*k.lvl
                    k.mana-=20
        elif character.magika==3:       # sort de Terre
            sort=int(input("--------------------------\n1 = Tectoclaque (-10 mana) /  2 = Séisme (-20mana)\n--------------------------\n"))
            if sort==1:
                enemi.pv-=randint(5,10)*k.degat*k.lvl
                k.mana-=10
            if sort==2:
                if k.mana<20:
                    print("Vous n'avez pas assez de Mana pour attaquer")
                else:
                    enemi.pv-=randint(7,15)*k.degat*k.lvl
                    k.mana-=20
        elif character.magika==4:       # sort Divin (BLESS DAMAGE AHH)
            sort=int(input("--------------------------\n1 = Lumière Divine (-10 mana) /  2 = Lance Divine (-20mana)\n3 = Hamaon (-1 mana)\n--------------------------\n"))
            if sort==1:
                enemi.pv-=randint(5,10)*k.degat*k.lvl
                k.mana-=10
            if sort==2:
                if k.mana<20:
                    print("Vous n'avez pas assez de Mana pour attaquer")
                else:
                    enemi.pv-=randint(7,15)*k.degat*k.lvl
                    k.mana-=20
            if sort==3:
                if laclasse==4:
                    enemi.pv-=6969
                    k.mana-=1
                else:
                    if randint(0,100)==69:
                        enemi.pv-=6969
                        k.mana-=1
    elif k==Nath:         # sorts de Nath
        sort=int(input("--------------------------\n1 = Glaive de Lumière (-10 mana) /  2 = Flèche de Lumière (-20mana) \n3 = Rejuvenate (-5mana)\n--------------------------\n"))
        if sort==1:
            enemi.pv-=randint(5,10)*k.degat*k.lvl
            k.mana-=10
        if sort==2:
                if k.mana<20:
                    print("Vous n'avez pas assez de Mana pour attaquer")
                else:
                    enemi.pv-=randint(5,20)*k.degat*k.lvl
                    k.mana-=20
        if sort==3:     
            stolen=randint(7,25)
            enemi.mana-=stolen
            Nath.mana+=(stolen-5)
    elif k==Andy:          # sorts d'Andy
        sort=int(input("--------------------------\n1 = Ébulition (-10 mana) /  2 = Hydrocanon (-20mana)\n--------------------------\n"))
        if sort==1:
            enemi.pv-=randint(5,10)*k.degat*k.lvl
            k.mana-=10
        if sort==2:
            if k.mana<20:
                print("Vous n'avez pas assez de Mana pour attaquer")
            else:
                enemi.pv-=randint(7,15)*k.degat*k.lvl
                k.mana-=20
    elif k==Ethan:          # sorts d'Éthan
        sort=int(input("--------------------------\n1 = Boule de feu (-10 mana) /  2 = Tempête de Flamme (-20mana)\n--------------------------\n"))
        if sort==1:
            enemi.pv-=randint(5,10)*k.degat*k.lvl
            k.mana-=10
        if sort==2:
            if k.mana<20:
                print("Vous n'avez pas assez de Mana pour attaquer")
            else:
                enemi.pv-=randint(7,15)*k.degat*k.lvl
                k.mana-=20

# FONCTION POUR LE SAC A DOS / OBJET
def backpack(bp, k):
    for i in bp:
        if i.quantite>=1:
            print(str(i.ID) + " = " + i.nom +" (" + str(i.quantite) +")")
    choic=int(input("Choississez l'objet (son ID)"))
    for i in bp:
        if i.ID==choic and i.quantite>0:
            if i.ID==1:       # ID = 1 -> potion heal 1
                k.vie+=15
            elif i.ID==2:     # ID = 1 -> potion heal 2
                k.vie+=35
            elif i.ID==3:     # ID = 1 -> potion heal 3
                k.vie+=60
            elif i.ID==4:     # ID = 1 -> potion mana 1
                k.mana+=15
            elif i.ID==5:     # ID = 1 -> potion mana 2
                k.mana+=35
            elif i.ID==6:     # ID = 1 -> potion mana 3
                k.mana+=60
            i.quantite-=1
            return

# FONCTION POUR LES ATTAQUES ENEMIS
def attack_enemi(enemi, List_player):
    perso=choice(List_player)
    perso.vie-=5*enemi.degat
    if perso.vie<=0:
        List_player.remove(perso)
        print(perso.nom + " est mort")
    return perso

def lvlup():
    for i in List_player:
        while i.xp>=100:
            i.degat+=0.5
            i.lvl+=1
            i.vie=i.get_maxvie()
            i.xp-=100
            print("Félicitation ! " + i.nom + " a augmenté d'un niveau, il est maintenant niveau " + str(i.lvl)+ ".")
            return i

# FONCTION POUR L'AMURERIEcharacter.vie_max=character.vie
# ELLE EST HORRIBLE JE SAIS 
# LA PLIER/CACHER ELLE PREND TROP DE PLACE POUR RIEN
def armurerie():
    print()
    shop=0
    while shop!=5:
        shop=int(input("-----------------------------------\nKilliann le forgeron : Bonjour. Vous avez b'soin d'quoi ?\n" 
        + "1 = " + character.nom + " ("+ str(character.argent) + ')\n' 
        + "2 = Nath" + " ("+ str(Nath.argent) + ')\n' 
        + "3 = Andy " + "("+ str(Andy.argent) + ')\n' 
        + "4 = " + Ethan.nom + " ("+ str(Ethan.argent) + ')' 
        + "\n5 = Partir" + "\n-----------------------------------\n"))
        if shop==1:
            if laclasse==1:     # mêlée
                achat=int(input("1 = " + tier1_sword.nom + '  ->  ' + str(tier1_sword.prix) +
                "\n2 = " + tier2_sword.nom + "  ->  " + str(tier2_sword.prix) + 
                "\n3 = " + ultimate_sword.nom + "  ->  " + str(ultimate_sword.prix)+ "\n")) 
                if achat==1:
                    if character.argent>=tier1_sword.prix:
                        character.arme=tier1_sword.nom
                        character.dura=tier1_sword.dura
                        character.degat=tier1_sword.degat
                        character.argent-=tier1_sword.prix
                    else:
                        print("Vous n'avez pas assez d'argent pour acheter ceci")
                        shop=0
                if achat==2:
                    if character.argent>=tier2_sword.prix:
                        character.arme=tier2_sword.nom
                        character.dura=tier2_sword.dura
                        character.degat=tier2_sword.degat
                        character.argent-=tier2_sword.prix
                    else:
                        print("Vous n'avez pas assez d'argent pour acheter ceci")
                        shop=0
                if achat==3:
                    if character.argent>=ultimate_sword.prix:    
                        character.arme=ultimate_sword.nom
                        character.dura=ultimate_sword.dura
                        character.degat=ultimate_sword.degat
                        character.argent-=ultimate_sword_sword.prix
                    else:
                        print("Vous n'avez pas assez d'argent pour acheter ceci")
                        shop=0
            elif laclasse==2:   # ranger
                achat=int(input("1 = " + tier1_bow.nom + '  ->  ' + str(tier1_bow.prix) +
                "\n2 = " + tier2_bow.nom + "  ->  " + str(tier2_bow.prix) + 
                "\n3 = " + ultimate_bow.nom + "  ->  " + str(ultimate_bow.prix) + "\n"))
                if achat==1:
                    if character.argent>=tier1_bow.prix:
                        character.arme=tier1_bow.nom
                        character.dura=tier1_bow.dura
                        character.degat=tier1_bow.degat
                        character.argent-=tier1_bow.prix
                    else:
                        print("Vous n'avez pas assez d'argent pour acheter ceci")
                        shop=0
                if achat==2:
                    if character.argent>=tier2_bow.prix:
                        character.arme=tier2_bow.nom
                        character.dura=tier2_bow.dura
                        character.degat=tier2_bow.degat
                        character.argent-=tier2_bow.prix
                    else:
                        print("Vous n'avez pas assez d'argent pour acheter ceci")
                        shop=0
                if achat==3:
                    if character.argent>=ultimate_bow.prix:    
                        character.arme=ultimate_bow.nom
                        character.dura=ultimate_bow.dura
                        character.degat=ultimate_bow.degat
                        character.argent-=ultimate_bow.prix
                    else:
                        print("Vous n'avez pas assez d'argent pour acheter ceci")
                        shop=0
            elif laclasse==3:   # mage
                achat=int(input("1 = " + tier1_staff.nom + '  ->  ' + str(tier1_staff.prix) +
                "\n2 = " + tier2_staff.nom + "  ->  " + str(tier2_staff.prix) + 
                "\n3 = " + ultimate_staff.nom + "  ->  " + str(ultimate_staff.prix) + "\n"))
                if achat==1:
                    if character.argent>=tier1_staff.prix:
                        character.arme=tier1_staff.nom
                        character.dura=tier1_staff.dura
                        character.degat=tier1_staff.degat
                        character.argent-=tier1_staff.prix
                    else:
                        print("Vous n'avez pas assez d'argent pour acheter ceci")
                        shop=0
                elif achat==2:
                    if character.argent>=tier2_staff.prix:
                        character.arme=tier1_staff.nom
                        character.dura=tier1_staff.dura
                        character.degat=tier1_staff.degat
                        character.argent-=tier2_staff.prix
                    else:
                        print("Vous n'avez pas assez d'argent pour acheter ceci")
                        shop=0
                elif achat==3:
                    if character.argent>=ultimate_staff.prix:    
                        character.arme=ultimate_staff.nom
                        character.dura=ultimate_staff.dura
                        character.degat=ultimate_staff.degat
                        character.argent-=ultimate_staff.prix
                    else:
                        print("Vous n'avez pas assez d'argent pour acheter ceci")
                        shop=0
        elif shop==2:
            achat=int(input("1 = " + tier1_staff.nom + '  ->  ' + str(tier1_staff.prix) +
                "\n2 = " + tier2_staff.nom + "  ->  " + str(tier2_staff.prix) + 
                "\n3 = " + ultimate_staff.nom + "  ->  " + str(ultimate_staff.prix) + "\n"))
            if achat==1:
                if Nath.argent>=tier1_staff.prix:
                    Nath.arme=tier1_staff.nom
                    Nath.dura=tier1_staff.dura
                    Nath.degat=tier1_staff.degat
                    Nath.argent-=tier1_staff.prix
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
                    shop=0
            elif achat==2:
                if Nath.argent>=tier2_staff.prix:
                    Nath.arme=tier2_staff.nom
                    Nath.dura=tier2_staff.dura
                    Nath.degat=tier2_staff.degat
                    Nath.argent-=tier2_staff.prix
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
                    shop=0
            elif achat==3:
                if Nath.argent>=ultimate_staff.prix:    
                    Nath.arme=ultimate_staff.nom
                    Nath.dura=ultimate_staff.dura
                    Nath.degat=ultimate_staff.degat
                    Nath.argent-=ultimate_staff.prix
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
                    shop=0
        elif shop==3:
            achat=int(input("1 = " + tier1_music.nom + '  ->  ' + str(tier1_music.prix) +
                "\n2 = " + tier2_music.nom + "  ->  " + str(tier2_music.prix) + 
                "\n3 = " + ultimate_music.nom + "  ->  " + str(ultimate_music.prix) + "\n"))
            if achat==1:
                if Andy.argent>=tier1_music.prix:
                    Andy.arme=tier1_music.nom
                    Andy.dura=tier1_music.dura
                    Andy.degat=tier1_music.degat
                    Andy.argent-=tier1_music.prix
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
                    shop=0  
            elif achat==2:
                if Andy.argent>=tier2_music.prix:
                    Andy.arme=tier2_music.nom
                    Andy.dura=tier2_music.dura
                    Andy.degat=tier2_music.degat
                    Andy.argent-=tier2_music.prix
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
                    shop=0
            elif achat==3:
                if Andy.argent>=ultimate_music.prix:    
                    Andy.arme=ultimate_music.nom
                    Andy.dura=ultimate_music.dura
                    Andy.degat=ultimate_music.degat
                    Andy.argent-=ultimate_music.prix
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
                    shop=0
        elif shop==4:
            achat=int(input("1 = " + tier1_cook.nom + '  ->  ' + str(tier1_cook.prix) +
                "\n2 = " + tier2_cook.nom + "  ->  " + str(tier2_cook.prix) + 
                "\n3 = " + ultimate_cook.nom + "  ->  " + str(ultimate_cook.prix) + "\n"))
            if achat==1:
                if Ethan.argent>=tier1_cook.prix:
                    Ethan.arme=tier1_cook.nom
                    Ethan.dura=tier1_cook.dura
                    Ethan.degat=tier1_cook.degat
                    Ethan.argent-=tier1_cook.prix
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
                    shop=0
            elif achat==2:
                if Ethan.argent>=tier2_cook.prix:
                    Ethan.arme=tier2_cook.nom
                    Ethan.dura=tier2_cook.dura
                    Ethan.degat=tier2_cook.degat
                    Ethan.argent-=tier2_cook.prix
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
                    shop=0
            elif achat==3:
                if Ethan.argent>=ultimate_cook.prix:    
                    Ethan.arme=ultimate_cook.nom
                    Ethan.dura=ultimate_cook.dura
                    Ethan.degat=ultimate_cook.degat
                    Ethan.argent-=ultimate_cook.prix
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
                    shop=0

# FONCTION POUR LE SHOP
# ELLE EST MOCHE AUSSI JE SAIS :)
def shop_heal():
    print("-----------------------------------\nMathieu le vendeur : Bien le bonjour ! Qu'est ce qu'il vous faudrait ?")
    shop=0
    finished=0
    while finished!=1:
        for i in List_player:
            achat=int(input("-----------------------------------\n"
            + i.nom + " (" + str(i.argent) + ")\n"
            + potion_heal1.nom + " ("+ str(potion_heal1.prix) + ")\n"
            + potion_heal2.nom + " ("+ str(potion_heal2.prix) + ")\n"
            + potion_heal3.nom + " ("+ str(potion_heal3.prix) + ")\n"
            + potion_mana1.nom + " ("+ str(potion_mana1.prix) + ")\n"
            + potion_mana2.nom + " ("+ str(potion_mana2.prix) + ")\n"
            + potion_mana3.nom + " ("+ str(potion_mana3.prix) + ")\n"
            + "7 = Partir"))
            if achat==1:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_heal1.prix*quantity:
                    potion_heal1.quantite+=quantity
                    i.argent-=potion_heal1.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de fiole de soin ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            elif achat==2:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_heal2.prix*quantity:
                    potion_heal2.quantite+=quantity
                    i.argent-=potion_heal2.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de potion de soin ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            elif achat==3:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_heal3.prix*quantity:
                    potion_heal3.quantite+=quantity
                    i.argent-=potion_heal3.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de patch de soin ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            elif achat==4:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_mana1.prix*quantity:
                    potion_mana1.quantite+=quantity
                    i.argent-=potion_mana1.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de fiole de mana ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            elif achat==5:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_mana2.prix*quantity:
                    potion_mana2.quantite+=quantity
                    i.argent-=potion_mana2.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de potion de mana ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            elif achat==6:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_mana3.prix*quantity:
                    potion_mana3.quantite+=quantity
                    i.argent-=potion_mana3.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de fiole de soin ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            elif achat==7:
                pass
        finished=int(input("Mathieu le vendeur : Ce sera tout ?\n1 = OUI\n2 = NON\n"))

# FONCTION POUR LE GAMEOVER
def gameover():
    if character.vie<=0:
        print("Vous êtes mort ! Malheureusement, il n'y a pas de checkpoint hihi skill issue !")
        sleep(2)
        exit()

### boss fight ###

# FONCTION POUR CHOISIR LE BOSS
def bossfightrdm(IsArnaudDead):
    if IsArnaudDead==0:
        enemi=Arnaud
    else:
        enemi=Ethan_boss
    return enemi

# FONCTION DU SYSTEME DE FIGHT CONTRE LES BOSS FINAUX
def boss_fight(IsArnaudDead):
    arme_equipe=lookup_arme(List_player)
    if arme_equipe==1:
        enemi=bossfightrdm(IsArnaudDead)
        print("\nVous vous apprêtez à vous battre contre " + str(enemi.nom) + ", il a " + str(enemi.pv) + " PV")
        if enemi.nom==Arnaud.nom:
            objetprecedent=None
            while totalpv(List_player)>0 and Arnaud.pv>0:
                for k in List_player:
                    affichage_combat(k, enemi, List_player)
                    print(k.nom + " attaque  ->  " + str(enemi.pv) + "\n")
                if objet_vole_ce_tour!=0:
                    objetprecedent=objet_vole_ce_tour
                if objetprecedent!=None:
                    objetprecedent=temp_objet
                    print("Vous avez récuperer vos objets")
                    objetprecedent=0
                if enemi.pv<0:
                    cible,a,objet_vole_ce_tour,temp_objet=attack_arnaud(enemi,List_player,bp)
                    print(enemi.nom + " attaque " + cible.nom + " -> " + str(cible.vie) + "pv.")
                if a==4:
                    break
        elif enemi.nom==Ethan_boss:
            while totalpv(List_player)>0 and Ethan_boss.pv>0:
                for k in List_player:
                    affichage_combat(k, enemi, List_player)
                    print(k.nom + " attaque  ->  " + str(enemi.pv) + "\n")
                cible=attack_ethan(enemi,List_player,bp)
                print(enemi.nom + " attaque " + cible.nom + " -> " + str(cible.vie) + "pv.")
        if totalpv(List_player)>0:
            for i in List_player:
                i.xp+=enemi.xp
            lvlup()
        else:
            Nath.vie=80 ; Andy.vie=100 ; character.vie=max_vie
        for i in List_player:
            i.dura-=1
    else:
        print("Vous ne pouvez pas vous battre car vous n'avez pas d'arme.")
        armurerie()
        boos_fight(IsArnaudDead)

# FONCTION ATTAQUE DU BOSS ARNAUD
def attack_arnaud(enemi, List_player, bp):
    perso=choice(List_player)
    temp_objet=None
    objet_vole_ce_tour=None
    if 900<enemi.pv<=1500:        # phase 1
        a=randint(1,3)
        if a==1:
            perso=choice(List_player)
            perso.vie-=15*enemi.degat
        elif a==2:
            enemi.degat+=0.1
        elif a==3:
            for perso in List_player:
                perso.vie-=10*enemi.degat
    elif 300 <= enemi.pv <= 900:  # phase 2
            a = randint(1,3)
            if a==1:
                perso=choice(List_player)
                perso.vie-=25*enemi.degat
            elif a==2:
                objet_vole_ce_tour = choice(bp)
                objet_vole_ce_tour.quantite=temp_objet
                objet_vole_ce_tour.quantite=0
                print("M. Arnaud vous à enlever " + objet_vole_ce_tour.nom + " pour 1 tour")
            elif a==3:
                for perso in List_player:
                    perso.vie-=20*enemi.degat
    elif enemi.pv<300:            # phase 3
        a=randint(1,4)
        if a==1:
            perso=choice(List_player)
            perso.vie-=40*enemi.degat
        elif a==2:
            for i in bp:
                i.quantite=0
        elif a==3:
            for perso in List_player:
                perso.vie-=30*enemi.degat
        elif a==4:
            print("Monsieur Arnaud : Je me rend ! Ne m'attaquez plus !")
    return perso, a, objet_vole_ce_tour, temp_objet

# FONCTION ATTAQUE DU BOSS ETHAN
def attack_ethan(enemi, List_player):
    if 500<enemi.pv<=750:       # phase 1
        a=randint(1,2)
        if a==1:
            perso=choice(List_player)
            perso.vie-=20*enemi.degat
        elif a==2:
            enemi.degat+=0.2
    if 250<enemi.pv<=500:       # phase 2
        a=randint(1,2)
        if a==1:
            for i in List_player:
                i.vie-=20*enemi.degat
        elif a==2:
            enemi.degat+=0.3
    if enemi.pv<250:            # phase 3
        a=randint(0,5)
        if a==0:
            perso=choice(List_player)
            perso.vie-=50*enemi.degat
        elif a==1:
            print("Ethan : Aie !")
        elif a==2:
            print("Ethan : Je vais vous tuer !")
        elif a==3:
            print("Ethan : Vous allez me le payer !")
        elif a==4:
            print("Ethan : Vous ne pouvez pas gagner !")
        elif a==5 and Req_TrueEnding == 1:
            print("Ethan : Je me rend ! Ne m'attaquez plus pitié !")
    return perso, a

##########################################

# default weapon

null_sword=arme("null sword",6969,1000,6969)
starter_sword=arme("Épée basique", 1, 5,50)
starter_bow=arme("Arc basique", 1, 5, 50)
starter_staff=arme("Sceptre basique", 1, 5, 50)
starter_music=arme("Luthe basique", 1, 5, 50)
starter_cook=arme("Couteau à pain", 1, 5, 50)

# tier 1 weapon

tier1_sword=arme("Katana de Yone", 1, 25,350)
tier1_bow=arme("Arc à pouli", 1, 25, 350)
tier1_staff=arme("Sceptre de la trahison", 1, 25, 350)
tier1_music=arme("Le triangle", 1, 25, 350)
tier1_cook=arme("Couteau à beurre", 1, 25, 350)

# tier 2 weapon

tier2_sword=arme("Rapière d'Arès", 1, 25,750)
tier2_bow=arme("Arc de la déese d'Arthémis", 1, 25, 750)
tier2_staff=arme("Aghanim's scepter", 1, 25, 750)
tier2_music=arme("Harpe d'Apollon", 1, 25, 750)
tier2_cook=arme("Dague cuisinière", 1, 25, 750)

#ultimate weapon

ultimate_sword=arme("Baguette de Pain Traditionnelle Française", 5, 50,1250)
ultimate_bow=arme("M4A1", 5, 50, 1250)
ultimate_staff=arme("", 5, 50, 1250)
ultimate_music=arme("Méga Ukulele", 5, 50, 1250)
ultimate_cook=arme("Alan Food Challenge", 5, 50, 1250)
Ferdi_sword=arme("L'épée de Fertiplouf", 10, 6969, 50)
shadow_scythe=arme("Faux des ombres", 50, 100, 0)

# personnages

Nath=chara("Nathaniel", 3, 80, 80, 4, 150, starter_staff.degat, starter_staff.nom, starter_staff.dura, 1, 0, randint(25,150))
Andy=chara("Andy", 0, 100, 100, 2, 100, starter_music.degat, starter_music.nom, starter_music.dura, 1, 0, randint(25,150))
Ferdi=chara("Ferdinand", 1, 150, 150, 3, 75, Ferdi_sword.degat, Ferdi_sword.nom, Ferdi_sword.dura, 1, 0, 0)
Ethan=chara("Éthan", 0, 120, 120, 1, 80, starter_cook.degat+1, starter_cook.nom, starter_cook.dura, 1, 0, randint(25,150))

# mobs

garde_1=mobs("Garde d'Arnaud", 30, 'humain', 0, 100, 0.85, 10, 15)
garde_2=mobs("Garde d'Arnaud", 75, 'humain', 0, 100, 1.5, 20, 20)
mini_boss1=mobs("Garde Runique d'Arnaud", 500, 'humain', 0, 500, 2.5, 1000, 100)


goblin=mobs("Goblin Racketteur", 45, 'goblin',0, 100,1.2,10,15)
balai=mobs("Balais Possédé", 60, 'objet', 0, 100, 1.5, 17, 17)
mannequin=mobs("Mannequin de Combat", 90, 'objet', 0, 100, 1.75 , 25, 20)
diff1=[goblin,balai,mannequin]

Chevalier=mobs("Chevalier de la Craie", 100, 'humain', 0, 150, 1.75, 50, 25)
mimik=mobs("Mimique Gourmand", 120, 'objet', 0, 150, 1.6, 60, 27)
diff2=[goblin,balai,mannequin,Chevalier,mimik]

garde=mobs('Garde du Tableau Noir', 200, 'esprit', 0, 200, 2, 100, 30)
loup=mobs('Loup des Ombres', 150, 'esprit', 0, 200, 2.2, 120, 35)
cake=mobs('Gâteau Mutant', 250, 'esprit', 0, 200, 1.8, 135, 40)
diff3=[Chevalier,mimik,garde,loup,cake]

Arnaud=mobs("M. Arnaud", 1500, 'humain', 0, 1000, 1, 50000, 500)

# objets

potion_heal1=objet("Fiole de soin", 4, 15, "Basique", 1)
potion_heal2=objet("Potion de soin", 0, 25, "Rare", 2)
potion_heal3=objet("Patch de soin", 0, 50, "Épique", 3)
potion_mana1=objet("Fiole de mana", 4, 15, "Basique", 4)
potion_mana2=objet("Potion de mana", 0, 25, "Rare", 5)
potion_mana3=objet("Patch de mana", 0, 50, "Épique", 6)

bp=[potion_heal1, potion_heal2, potion_heal3, potion_mana1, potion_mana2, potion_mana3]

# variable stock

a=0 ; temp="" ; totalheal=0 ; diff=1 ; List_player=[] ; list_ferdi=[Ferdi] ; buy=0 ; shop=0 ; stade_equipe=0 ; freetime = 0


#############################################################
#                                                           #
#   Act 1 Prologue                                          #
#   quick contexte + "character creator "                   #
#                                                           #
#############################################################
print("AVANT DE COMMENCER À JOUER / LIRE IMPÉRACTIVEMENT !!!\nPour passer au dialogue suivant appuyer sur Entrée.\nLors des choix bien mettre les chiffres indiquées sinon il faut tout recommencer SURTOUT LORS DES COMBATS !\nIl y a beaucoup de textes donc il faut avoir un certain temps devant soit (et oui c'est un j-rpg (sorte de plutôt lmao))\nUtiliser un shell qui casse pas les couleurs de préférence (*tousse* fish-shell bullshit *tousse*)\n"); input("ENTRÉE POUR PASSER")

print(Fore.WHITE + "Act 1 : Prologue : La rencontre")
print(Fore.WHITE + "Narrateur : C'est une belle fin de journée d'été dans le grand royaume de Monté-Cristo, après une dure journée à vagabondé, vous êtes allé au bar, vous avez bus et vous avez finit par vous endormir.") ; input()
print(Fore.WHITE + "Narrateur : Un grand sage apparait dans votre rêve et vous tend la main.\n")
print(Fore.GREEN + "Grand Sage : Enchanté mon/ma cher(e)... Quel est ton nom ?")
name=str(input(Fore.WHITE +"\nEntrez le nom du personnage : "))
while temp!="oui":
    temp=str(input(Fore.WHITE +"\nVotre nom est bien " + name + " ? (rentrez oui/non)\n"))
    if temp!="oui":
        name=str(input(Fore.WHITE + "Entrez le nom du personnage : "))
print(Fore.GREEN + "Grand Sage : Un nom très exotique, " + name + "... Enfin passons, aujourd'hui j'apparait dans votre inconscient pour vous offrir un pouvoir et vous permettre de sortir de votre routine.") ; input()
print(Fore.GREEN + "Grand Sage : Tout d'abord, quel classeList_player choissirez vous ?")
laclasse=int(input(Fore.WHITE +"\nChoississez votre classe :\n1 = Mêlée\n2 = Ranger\n3 = Mage\n"))
temp=""
while temp!="oui":
    temp=str(input(Fore.WHITE +"\nÊtes vous sûre de choisir " + str(laclasse) + " ? (rentrez oui/non)\n"))
    if temp!="oui":
        laclasse=int(input(Fore.WHITE +"\nChoississez votre classe :\n1 = Mêlée\n2 = Ranger\n3 = Mage\n"))

print(Fore.GREEN + "Grand Sage : Haha, très intéressant... Et enfin, je vous confère un des 4 types de magika, lequel choissirez vous ?\n")
type=int(input(Fore.WHITE +"Choississez votre type de Magika :\n1 = Feu\n2 = Eau\n3 = Terre\n4 = Divine\n"))
temp=""
while temp!="oui":
    temp=str(input(Fore.WHITE +"\nÊtes vous sûre de choisir " + str(type) + " ? (rentrez oui/non)\n"))
    if temp!="oui":
        type=int(input(Fore.WHITE +"Choississez votre type de Magika :\n1 = Feu\n2 = Eau\n3 = Terre\n4 = Divine\n"))

character=chara(name, laclasse, 100, 100,type, 100, null_sword.degat, null_sword.nom, null_sword.dura, 1, 0, randint(25,150))

if laclasse==1:         # classe -> mêlée
    character.vie_base+=25
    character.mana-=25
    character.arme=starter_sword.nom
    character.degat=starter_sword.degat
    character.dura=starter_sword.dura
    character.degat*=1.3
if laclasse==2:         # classe -> ranger
    character.vie_base-=15
    character.arme=starter_bow.nom
    character.degat=starter_bow.degat
    character.dura=starter_bow.dura
    character.degat*=1.25
if laclasse==3:         # classe -> mage
    character.vie_base-=35
    character.mana+=50
    character.arme=starter_staff.nom
    character.degat=starter_staff.degat
    character.dura=starter_staff.dura
    character.degat*=1.1
if character.nom.lower()=="Reaper".lower():
    if laclasse==4:         # la classe secrète (reaper)
        character.vie_base=250
        character.arme=shadow_scythe.nom
        character.degat=shadow_scythe.degat
        character.dura=shadow_scythe.dura
character.vie_max=character.get_maxvie()
character.vie=character.vie_max

print(Fore.GREEN + "Grand Sage : Bien, bien... " + character.nom + " votre nouvelle vie va enfin pouvoir commencer !" + Fore.WHITE + "\nNarrateur : Le grand sage disparait de votre rêve et vous vous rendormez.")

#############################################################
#                                                           #
#   Act 1 - Scène 1                                         #
#   rencontre avec andy                                     #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Écran noir. On entend des conversations, des rires, des verres qui s'entrechoquent et une luthe qui joue une mélodie un peu trop forte. Une voix résonne au loin.") ; input()
print(Fore.CYAN + "Tavernier : Hé ! Toi ! Réveille-toi !" + Fore.WHITE + "\nNarrateur : Rien."); input()
print(Fore.CYAN + "Tavernier : Je te préviens, si tu continues à dormir sur cette table, je te facture la nuit !" + Fore.WHITE + "\nNarrateur : " + character.nom + " ouvre lentement les yeux. "); input()
print(Fore.BLUE + character.nom + " : ... C'est déjà le matin ? "); input()
print(Fore.CYAN + "Tavernier : Non. C'est toujours hier soir. Tu as juste réussi à dormir pendant que tout le monde vivait sa vie. "); input()
print(Fore.BLUE + character.nom + " : Ah." + Fore.WHITE + "\nNarrateur : " + character.nom + " tente de se redresser, puis se rassoit immédiatement. "); input()
print(Fore.BLUE + character.nom +  " : Pourquoi j'ai l'impression qu'un troupeau de chevaux m'est passé sur le crâne ?" ); input()
print(Fore.CYAN + "Tavernier : Parce que tu as dormi sur ma meilleure table pendant trois heures."); input()
print(Fore.BLUE + character.nom + " : Je croyais que c'était une auberge.") ; input()
print(Fore.CYAN + "Tavernier : C'en est une."); input()
print(Fore.BLUE + character.nom + " : Donc les gens ont le droit de dormir."); input()
print(Fore.CYAN + "Tavernier : Dans un lit. Avec une chambre. Et en payant."); input()
print(Fore.BLUE + character.nom + " : Je vois que l'hospitalité est encore une tradition vivante."); input()
print(Fore.CYAN + "Tavernier : Elle l'était avant que tu arrives." + Fore.WHITE + "\nNarrateur : Le tavernier tend la main.")
print(Fore.CYAN + "Tavernier : Une pièce d'argent."); input()
print(Fore.BLUE + character.nom + " : Je viens à peine de me réveiller !"); input()
print(Fore.CYAN + "Tavernier : Et moi, je viens à peine de perdre patience."); input()
print(Fore.WHITE +"Narrateur : " + character.nom + " fouille ses poches." + Fore.BLUE + "\n" + character.nom + " : Je crois que j’ai rien."); input()
print(Fore.CYAN + "Tavernier : Magnifique. Un voyageur sans argent qui dort sur mes tables. Tu collectionnes les mauvaises décisions ou c'est naturel ?"); input()
print(Fore.BLUE + character.nom + " : Je suis en période d'essai." + Fore.WHITE + "\nNarrateur : Le tavernier soupire et s'éloigne en marmonnant. Au même moment, un musicien vient de terminer son morceau sous les applaudissements de quelques clients et les soupirs d'autres."); input()
print(Fore.LIGHTBLACK_EX + "Musicien : Merci ! Merci beaucoup ! Vous avez été un public exceptionnel !"); input()
print(Fore.CYAN + "Client : Je t'ai demandé d'arrêter il y a vingt minutes !") ; input()
print(Fore.LIGHTBLACK_EX + "Musicien : Exactement ! Vous étiez tellement bouleversés par mon talent que vous avez perdu la notion du temps ! "); input()
print(Fore.CYAN + "Client : Je voulais simplement entendre mon ami parler !"); input()
print(Fore.LIGHTBLACK_EX + "Musicien : Alors imagine ce qu'il ressentira quand il découvrira qu'il aurait pu écouter de la musique à la place." + Fore.WHITE + "\nNarrateur : Quelques clients rient. D'autres lèvent les yeux au ciel. "); input()
print(Fore.LIGHTBLACK_EX + "Musicien : Je vous retrouverai demain pour un nouveau concert ! Même heure, même scène !"); input()
print(Fore.CYAN + "Tavernier : Demain, tu joues dehors. "); input()
print(Fore.LIGHTBLACK_EX + "Musicien : Excellente idée ! Un concert en plein air. C'est très tendance. "); input()
print(Fore.CYAN + "Tavernier : Sous la pluie. "); input()
print(Fore.LIGHTBLACK_EX + "Musicien : Une ambiance immersive. J'adore."); input()

print(Fore.WHITE + "Narrateur : Le musicien descend de la scène et range soigneusement sa luthe. Il ajuste sa veste, remet ses cheveux en place et s'approche du comptoir avec la démarche d'un homme persuadé que le monde entier l'attend. Il remarque " + character.nom + ", encore à moitié endormi.") ; input()
print(Fore.LIGHTBLACK_EX + "Musicien : Tiens, un nouveau visage. "); input()
print(Fore.BLUE + character.nom + " : Pardon, qui es tu ? Et pourquoi tu  dis ça comme si les anciens avaient tous disparu. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je me présente, je m'appelle Andy, un musicien d'excellence. Pour ce qui est des anciens, certains sont partis. D'autres ont fui. Quelques-uns ne reviennent que pour me demander de baisser le volume. "); input()
print(Fore.BLUE + character.nom + " : Je comprends pourquoi. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Oh, il est réveillé depuis trente secondes et il a déjà un avis sur mon art. C'est prometteur. "); input()
print(Fore.BLUE + character.nom + " : Ton art m'a réveillé. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Alors j'ai réussi. Un artiste se doit de toucher son public. "); input()
print(Fore.BLUE + character.nom + " : Tu m'as surtout touché les tympans. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : La critique est parfois brutale." + Fore.WHITE + "\nNarrateur : Andy commande une boisson et s'appuie contre le comptoir. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Bon, voyageur mystérieux, qu'est-ce qui t'amène à la capitale de Monté Cristo?"); input()
print(Fore.BLUE + character.nom + " : Je voyage. Je cherche ma route. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Magnifique. Moi aussi, je cherche ma route. "); input()
print(Fore.BLUE + character.nom + " : Tu viens de dire que tu jouais ici demain. "); input()

print(Fore.LIGHTBLACK_EX + "Andy : Ma route professionnelle, pas géographique. Essaie de suivre."); input()
print(Fore.BLUE + character.nom + " : Pardon, monsieur le philosophe. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je préfère « génie incompris ». "); input()
print(Fore.BLUE + character.nom + " : Par qui ? "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Par tout le monde. C'est le principe." + Fore.WHITE + "\nNarrateur : Un court silence s'installe. Andy observe les vêtements poussiéreux de " + character.nom + "."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Tu viens de loin ? "); input()
choix=int(input(Fore.RESET + "Qu'allez vous lui répondre ?\n1 =  « Je cherche simplement un endroit où dormir. »\n2 = « Je cherche quelque chose d'intéressant à vivre. »\n3 = « Ça ne te regarde pas. »\n"))
if choix==1:
    print("Andy : Dans ce cas, tu as choisi la mauvaise taverne. Ici, même les tables sont payantes.")
if choix==2:
    print(Fore.LIGHTBLACK_EX + "Andy : Excellent ! Tu viens de rencontrer l'homme le plus intéressant de cette pièce.")
if choix==3:
    print(Fore.LIGHTBLACK_EX + "Andy : Mystérieux, susceptible... On dirait le début d'une très mauvaise association.")
print(Fore.LIGHTBLACK_EX + "Andy : Tu fuis quelqu'un ? "); input()
print(Fore.BLUE + character.nom + " : Pourquoi cette question ? "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Parce que tu as la tête de quelqu'un qui a fui quelque chose."); input()
print(Fore.BLUE + character.nom + " : Et toi, tu as la tête de quelqu'un qui parle trop. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Touché." + Fore.WHITE + "\nNarrateur : Andy lève sa chope." + Fore.LIGHTBLACK_EX + "\nAndy : À nos défauts respectifs. "); input()
print(Fore.BLUE + character.nom + " : Je n'ai pas encore accepté de trinquer avec toi. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : C'est vrai. Mais je préfère prendre de l'avance." + Fore.WHITE + "\nNarrateur : Il boit. "); input()

#############################################################
#                                                           #
#   Act 1 - Scène 2                                         #
#   les gardes d'arnaud                                     #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : La porte de la taverne s'ouvre brusquement. Un villageois entre, essoufflé, et manque de tomber sur un tabouret. "); input()
print(Fore.CYAN + "Villageois : Fermez les portes ! Les gardes d'Arnaud arrivent !" + Fore.WHITE + "\nNarrateur : Les conversations diminuent immédiatement. "); input()
print(Fore.CYAN + "Tavernier : Encore ? "); input()
print(Fore.CYAN + "Villageois : Ils arrêtent les gens sur la place ! Ils ont emmené le forgeron ce matin !"); input()
print(Fore.CYAN + "Client : Qu'a-t-il fait ? "); input()
print(Fore.CYAN + "Villageois : Il aurait refusé de fabriqueList_playerr des armes pour les soldats. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Ou alors il a fabriqué une épée trop courte. Je connais le problème."); input()
print(Fore.BLUE + character.nom + " : Tu connais le forgeron ? "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Il m'a vendu une corde trop courte une fois. "); input()
print(Fore.BLUE + character.nom + " : Quel rapport ?"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Aucun. Mais je lui en veux encore.") ; input()
print(Fore.CYAN + "Villageois : Ce n'est pas drôle ! Ils arrêtent tous ceux qui critiquent Monsieur Arnaud !" + Fore.WHITE + "\nNarrateur : Le sourire d'Andy s'efface légèrement. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Ce n'est pas nouveau. "); input()
print(Fore.BLUE + character.nom + " : Tu as l'air de bien connaître le sujet. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Disons que certaines de mes chansons ont un public... particulier. "); input()
print(Fore.BLUE + character.nom + " : Des fans ? "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Des gardes.") ; input()
print(Fore.BLUE + character.nom + " : Ce ne sont pas des fans. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Ils viennent à tous mes concerts. Ils connaissent mes paroles. Ils me suivent jusque dans les rues. Je refuse de tirer des conclusions hâtives." + Fore.WHITE + "\nNarrateur : Des coups violents retentissent contre la porte. "); input()
print(Fore.CYAN + "Garde, *derrière la porte* : AU NOM DE MONSIEUR ARNAUD ! OUVREZ IMMÉDIATEMENT !"); input()
print(Fore.WHITE + "Narrateur : Le tavernier se fige." + Fore.CYAN + "\nTavernier : Personne ne bouge ! S'ils trouvent une raison de fermer mon établissement, je perdrai tout ! "); input()
print(Fore.CYAN + "Villageois : Ils vont fouiller la salle ! "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Bon. Je crois que nous avons atteint le moment où ma soirée devient intéressante."); input()
print(Fore.BLUE + character.nom + " : Tu pourrais essayer de ne pas attirer leur attention. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je suis musicien. Attirer l'attention, c'est mon métier. "); input()
print(Fore.BLUE + character.nom + " : Ton métier va nous faire arrêter. "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Tu vois ? Tu comprends déjà les difficultés de la vie d'artiste." + Fore.WHITE + "\nNarrateur : Les coups deviennent plus violents. "); input()
print(Fore.CYAN + "Garde : DERNIER AVERTISSEMENT !"); 

choix=int(input(Fore.WHITE + "CHOIX 1 — Que choix ferait vous ?\n1 = Aider Andy à bloquer la porte.\n2 = Se cacher derrière le comptoir.\n3 = Fuir par la porte arrière.\n"))

if choix==1:
    print(Fore.BLUE + character.nom + " : Si on les laisse entrer, ils vont embarquer la moitié de la salle. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Enfin quelqu'un qui comprend l'importance d'une bonne barricade !" + Fore.WHITE + "\nNarrateur : " + character.nom + " et Andy déplacent une table devant la porte. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Plus à gauche. "); input()
    print(Fore.BLUE + character.nom + " : Elle est déjà à gauche ! ") ; input()
    # (used to be) ligne 666 haha
    print(Fore.LIGHTBLACK_EX + "Andy : Alors à gauche de ta gauche. "); input()
    print(Fore.BLUE + character.nom + " : Je vais finir par te barricader toi-même." + Fore.WHITE + "\nNarrateur : La porte tremble sous les coups. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Si nous survivons, je t'écrirai une chanson. "); input()
    print(Fore.BLUE + character.nom + " : Essaie plutôt de survivre sans chanter. "); input()
if choix==2:
    print(Fore.BLUE + character.nom + " : Je ne vais pas risquer ma peau pour des inconnus. ");input()
    print(Fore.LIGHTBLACK_EX + "Andy : Une décision parfaitement raisonnable. Lâche, mais raisonnable."); input()
    print(Fore.BLUE + character.nom + " : Tu préfères te faire arrêter ? "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Je préfère ne pas me faire arrêter. Mais je suis ouvert aux expériences nouvelles. "); input()
    print(Fore.BLUE + character.nom + " se cache derrière le comptoir. Andy se glisse derrière une étagère, sa luthe à la main. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Si quelqu'un demande, je suis pas la. "); input()
    print(Fore.BLUE + character.nom + " : Ok ? "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Voila."); input()
if choix==3:
    print(Fore.BLUE + character.nom + " : Il y a une sortie derrière ? "); input()
    print(Fore.CYAN + "Tavernier : Oui. Mais si tu pars sans payer, je retiens ton visage !"); input()
    print(Fore.BLUE + character.nom + " : Vous retenez déjà ma dette, ça devrait suffire." + Fore.WHITE + "\nNarrateur : " + character.nom + " rejoint la porte arrière. Andy le suit discrètement. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Tu pars sans moi ? "); input()
    print(Fore.BLUE + character.nom + " : Je pensais que t’étais pas la. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Eh ben Maintenant SI !" + Fore.WHITE + "\nNarrateur : Ils sortent dans la ruelle. "); input()

#############################################################
#                                                           #
#   Act 1 - Scène 3                                         #
#   le conflit                                              #
#                                                           #
#############################################################

if choix==1 or choix==2:
    print(Fore.WHITE + "Narrateur : Les gardes finissent par enfoncer la porte. il entend leurs voix depuis la ruelle et voit Andy reconnu à travers une fenêtre."); input()
    print(Fore.CYAN + "Garde : Toi ! Le musicien ! "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Vous devez me confondre avec quelqu'un de beaucoup plus célèbre. "); input()
    print(Fore.CYAN + "Garde : Tu as chanté contre Monsieur Arnaud hier soir ! "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : C'était une chanson d'amour. "); input()
    print(Fore.CYAN + "Garde : Elle disait que son règne était une maladie ! "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Une maladie métaphorique. Très artistique. "); input()
    print(Fore.CYAN + "Garde : Tu es accusé de troubler l'ordre public ! "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Pour une chanson ? "); input()
    print(Fore.CYAN + "Garde : Pour tes paroles, tes rassemblements et ton refus d'obéir ! "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Je tiens à préciser que j'obéis très bien. Quand les ordres sont raisonnables."); input()
    print(Fore.CYAN + "Garde : Arrêtez-le !" + Fore.WHITE + "\nNarrateur : Un garde saisit Andy par le bras. Andy tente de se dégager, mais deux autres soldats lui barrent le passage. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Messieurs, je vous assure que mon prochain morceau sera beaucoup plus calme !"); input()
    print(Fore.BLUE + character.nom + " : Lâchez-le !"); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Je retire ce que j'ai dit. Mon prochain morceau sera une chanson sur les gens qui arrivent au bon moment !" + Fore.WHITE + "\nNarrateur : Les gardes se tournent vers " + character.nom); input()
    print(Fore.CYAN + "Garde : Encore un opposant ? "); input()
    print(Fore.BLUE + character.nom + " : Je viens juste de me réveiller. Je n'ai pas encore eu le temps de m'opposer à qui que ce soit. "); input()
    print(Fore.CYAN + "Garde : Alors tu peux commencer par nous suivre. "); input()
    print(Fore.BLUE + character.nom + " : Je crois que je préfère rester ici." + Fore.WHITE + "\nNarrateur : Les gardes dégainent leurs armes. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Bon, je voulais éviter d'en arriver là..." + Fore.RESET); input()

    List_player=[character, Andy] ; diff=10 ; did_fight=1
    Andy.set_maxvie() ; character.set_maxvie()
    fight()

    print(Fore.WHITE + "Narrateur : Après plusieurs échanges, les gardes finissent par reculer. "); input()
    print(Fore.CYAN + "Garde : Vous le regretterez ! Monsieur Arnaud saura ce qui s'est passé ici !"); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Dites-lui que je prends les réservations pour mon prochain concert !"); input()
    print(Fore.BLUE + character.nom + " : Andy ! "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Quoi ? Il faut bien faire de la publicité." + Fore.WHITE + "\nNarrateur : Les gardes s'enfuient. La taverne est en désordre. "); input()
    print(Fore.CYAN + "Tavernier : Ma table..."); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Elle est morte en héros. "); input()
    print(Fore.CYAN + "Tavernier : C'était une table en chêne !") ; input()
    print(Fore.BLUE + character.nom + " : Je vais vous aider à la réparer. "); input()
    print(Fore.CYAN + "Tavernier : Avec ton argent ?" + Fore.WHITE + "\nNarrateur : " + character.nom + " reste silencieux."); input()
    print(Fore.CYAN + "Tavernier : C'est bien ce que je pensais. "); input()

#############################################################
#                                                           #
#   Act 1 - Scène 4                                         #
#   pourquoi se battre ?                                    #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : " + character.nom + " et Andy sortent de la taverne. Dans la rue, plusieurs habitants ferment leurs volets. Des affiches d'Arnaud sont placardées sur les murs."); input()
print(Fore.BLUE + character.nom + " : Pourquoi est-ce que tu continues à chanter contre lui ?"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Parce que je chante mieux que je ne me bats. "); input()
print(Fore.BLUE + character.nom + " : Ce n'est pas une réponse." + Fore.WHITE + "\nNarrateur : Andy s'arrête devant une affiche représentant Arnaud, le visage grave et une main levée en signe de paix."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Tu sais ce que cette affiche dit ? « La paix exige l'obéissance. » "); input()
print(Fore.BLUE + character.nom + " : C'est une drôle de définition de la paix."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Exactement. Il a commencé par promettre de protéger les gens. Maintenant, il veut qu'ils aient peur de parler. Si tu critiques ses taxes, tu es un traître. Si tu racontes l'histoire d'avant son règne, tu es un agitateur. Si tu chantes une chanson qu'il n'aime pas... "); input()
print(Fore.BLUE + character.nom + " : Tu es Andy.") ; input()
print(Fore.LIGHTBLACK_EX + "Andy : Voilà. Tu suis." + Fore.WHITE + "\nNarrateur : Andy baisse les yeux vers sa luthe."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je ne prétends pas pouvoir renverser un gouvernement avec trois accords et une voix magnifique. "); input()
print(Fore.BLUE + character.nom + " : Quatre accords ?"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je savais que tu étais jaloux." + Fore.WHITE + "\nNarrateur : Il sourit, puis reprend un ton plus sérieux." + Fore.LIGHTBLACK_EX + "\nAndy : Mais si tout le monde se tait, il pourra raconter ce qu'il veut. Et un jour, plus personne ne se souviendra qu'on avait le droit de dire non. "); input()
print(Fore.WHITE + "Narrateur : " + character.nom + " regarde les rues presque désertes.\n" + Fore.BLUE + character.nom + " : Et tu comptes faire quoi ?"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Trouver ce qu'Arnaud cache. Comprendre pourquoi il a si peur qu'on parle du passé. Puis trouver une façon de le faire tomber."); input()
print(Fore.BLUE + character.nom +" : Tu comptes faire tout ça avec ta luthe ? "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Avec ma luthe, mon intelligence, mon charme et, éventuellement, quelqu'un qui sait donner des coups. "); input()
print(Fore.BLUE + character.nom +" : Tu cherches quelqu'un qui sait donner des coups ? "); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je ne voudrais pas te mettre la pression. "); input()

choix=int(input(Fore.WHITE + "Quelle est la réponse du " + character.nom + " ?\n1 = « Je vais t'aider à faire tomber Arnaud. »\n2 = « Je t'accompagne jusqu'à la prochaine ville. »\n3 = « Je ne veux pas d'ennuis.\n"))

if choix==1:
    print(Fore.BLUE + character.nom + " : D'accord. Je vais t'aider. Mais je ne suis pas ton garde du corps. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Bien sûr que non. Tu es mon partenaire d'aventure. C'est beaucoup moins bien payé. "); input()
    print(Fore.BLUE + character.nom + " : Et tu arrêtes de provoquer les gardes. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Je vais essayer de provoquer les moins dangereux. Mais pour l’instant je dois y aller, j’ai quelque chose à faire, essaye de découvrir les environs avant que je revienne."); input()
    print(Fore.LIGHTBLACK_EX + "Andy part mais avec " + character.nom + ", ils créent officiellement un groupe"); input()

if choix==2:
    print(Fore.BLUE + character.nom + " : Je vais t'accompagner pour l'instant. Après, chacun sa route. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Une alliance temporaire. Très mystérieux. J'adore. "); input()
    print(Fore.BLUE + character.nom + " : Ce n'est pas mystérieux. Je ne te connais pas. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Justement. Il reste encore tant de choses à découvrir sur moi. Mais pour l'instant, je dois y aller, j’ai quelque chose à faire. Essaye de découvrir les environs avant que je ne revienne." + Fore.WHITE + "\nNarrateur : Andy part mais avec " + character.nom + ", ils créaient provisoirement un groupe."); input()

if choix==3:
    print(Fore.BLUE + character.nom + " : Je préfère éviter les problèmes. Je ne suis pas un héros. "); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Bonne nouvelle : moi non plus. Je suis musicien. "); input()
    if did_fight==1:
        print(Fore.BLUE + character.nom + " : Tu viens pourtant de combattre des gardes. "); input()
        print(Fore.LIGHTBLACK_EX + "Andy : C'était une répétition.  Mais pour l'instant, je dois y aller, j’ai quelque chose à faire. Essaye de découvrir les environs avant que je ne revienne." + Fore.WHITE + "\nNarrateur : Andy décide de partir."+ Fore.RESET); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Mais pour l'instant, je dois y aller, j’ai quelque chose à faire. Essaye de découvrir les environs avant que je ne revienne." + Fore.WHITE + "\nNarrateur : Andy décide de partir."+ Fore.RESET); input()
farm=1
while farm!=2:
    freetime=int(input("--------------------------\nQu'est ce que vous souhaitez faire ?\n1 = Allez battre des monstres.\n2 = Allez chez le forgeron.\n3 = Allez chez le vendeur.\n"))
    if freetime==1:
        List_player=[character] ; diff=1 ; stade_equipe=3
        fight()
        if randint(1,10)==1:
            character.set_maxvie()
    elif freetime==2:
        armurerie()
    elif freetime==3:
        shop_heal()
    farm=int(input("Voulez vous continuez de profiter de votre temps libre ?\n1 = OUI\n2 = NON\n"))
print(Fore.WHITE + "Narreteur : Après votre temps libre d'aller vous endormir dans une ruelle allumée par un lampadaire défectueux."); input()

#############################################################
#                                                           #
#   Act 1 - Scène 5                                         #
#   le cri du marchand                                      #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Le lendemain, " + character.nom + " poursuit sa route. Les rues deviennent plus animées à mesure qu'il approche de la place du marché. Une voix puissante retentit au loin." ); input()
print(Fore.CYAN + "Inconnu : JE VAIS TE FAIRE AVALER CETTE ÉPÉE ! "); input()
print(Fore.BLUE + character.nom + " : ... Quel super début de journée..."); input()
print(Fore.WHITE + "Narrateur : On voit un homme immense, un marchand terrorisé et une épée cassée en deux.");input()

#############################################################
#                                                           #
#   Act 2 - Scène 1                                         #
#   une histoire d'épée                                     #
#                                                           #
#############################################################

print(Fore.WHITE + "Lieu : La place du marché de la capital Monté Cristo"); input()
print(Fore.WHITE + "Narrateur : " + character.nom +" arrive sur la place. Des marchands vendent des légumes, des tissus et des objets de toutes sortes. Des gardes surveillent les étals.Au centre, un homme immense fait face à un marchand qui tient une épée brisée."); input()
print(Fore.CYAN + "Marchand : Ferdinand ! Tu m'avais promis de payer cette épée !"); input()
print(Fore.YELLOW + "Ferdinand : Et je t'ai dit que je te paierais. "); input()
print(Fore.CYAN + "Marchand : C'était il y a trois semaines ! "); input()
print(Fore.YELLOW + "Ferdinand : Le temps passe vite quand on a des problèmes. "); input()
print(Fore.CYAN + "Marchand : Tu as cassé mon épée ! "); input()
print(Fore.YELLOW + "Ferdinand : Elle était déjà fragile. "); input()
print(Fore.CYAN + "Marchand : TU L'AS COUPÉE EN DEUX SUR UN ROCHER ! "); input()
print(Fore.YELLOW + "Ferdinand : Le rocher était mal placé." + Fore.WHITE + "\nNarrateur : " + character.nom+" s'approche, curieux."); input()
print(Fore.BLUE + character.nom + " : Excuse-moi. Il y a un problème ? "); input()
print(Fore.CYAN + "Marchand : Oui ! Ce géant m'a détruit une épée et refuse de payer ! "); input()
print(Fore.YELLOW + "Ferdinand : Je ne refuse pas de payer. Je demande juste un délai."); input()
print(Fore.CYAN + "Marchand : Tu as demandé un délai hier ! "); input()
print(Fore.YELLOW + "Ferdinand : Je suis quelqu'un de constant. "); input()
print(Fore.BLUE + character.nom + " : Tu pourrais simplement t'excuser. "); input()
print(Fore.YELLOW + "Ferdinand : Je me suis excusé auprès du rocher. "); input()
print(Fore.BLUE + character.nom + " : ... Tu es sérieux ? "); input()
print(Fore.YELLOW + "Ferdinand : Il ne m'a pas répondu. "); input()
print(Fore.BLUE + character.nom + " : Peut-être qu'il attendait que tu lui offres une épée."); input()
print(Fore.YELLOW + "Ferdinand : Maintenant que tu le dis, c'est possible." + Fore.WHITE + "\nNarrateur : Le marchand se prend la tête entre les mains.") ; input()
print(Fore.CYAN + "Marchand : Je vais finir ruiné à cause de toi ! "); input()
print(Fore.YELLOW + "Ferdinand : Mais non. Je vais t'aider à vendre tes marchandises."); input()
print(Fore.CYAN + "Marchand : Tu as renversé trois paniers en arrivant ! "); input()
print(Fore.YELLOW + "Ferdinand : Ils étaient mal rangés. "); input()
print(Fore.BLUE + character.nom + " : Tu as un problème avec tout ce qui ne bouge pas ? "); input()
print(Fore.YELLOW + "Ferdinand : Non. Seulement avec ce qui se trouve sur chemin. "); input()
print(Fore.WHITE + "Narrateur : " + character.nom + " regarde l'homme de haut en bas.") 
print(character.nom + " : Tu mesures combien ?"); input()
print(Fore.YELLOW + "Ferdinand : Je ne sais pas. "); input()
print(Fore.BLUE + character.nom+ " : Tu ne sais pas ? "); input()
print(Fore.YELLOW + "Ferdinand : Je n'ai jamais vu l'intérêt de mesurer quelqu'un qui est déjà grand."); input()
print(Fore.BLUE + character.nom + " : C'est une philosophie. "); input()
print(Fore.YELLOW + "Ferdinand : Merci. "); input()
print(Fore.BLUE + character.nom + " : Ce n'était pas un compliment. "); input()
print(Fore.YELLOW + "Ferdinand : Je prends ce que je peux. "); input()

choix=int(input("Que dire à Ferdinand ?\n1 = « Tu dois être pratique pour atteindre les étagères. »\n2 = « Tu dois faire peur à beaucoup de monde. »\n3 = « Tu as surtout l'air de manquer de discrétion. »\n"))

if choix==1:
    print("Ferdinand : C'est vrai. Je n'ai plus besoin de demander de l'aide.")
if choix==2:
    print("Ferdinand : Seulement aux gens qui se mettent devant moi.")
if choix==3:
    print("Ferdinand : Je peux être discret.")
    print("Narrateur : Il fait tomber un panier en se retournant")
    print(character.nom + " : Impressionnant...")

#############################################################
#                                                           #
#   Act 2 - Scène 2                                         #
#   les gardes interviennent                                #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Le marchand, à bout de patience, appelle les gardes. "); input()
print(Fore.CYAN + "Marchand : Gardes ! Par ici ! Cet homme refuse de payer et menace mes clients ! "); input()
print(Fore.YELLOW + "Ferdinand : Je n'ai menacé personne ! "); input()
print(Fore.CYAN + "Marchand : Tu as dit que tu allais me faire avaler l'épée ! "); input()
print(Fore.YELLOW + "Ferdinand : J'ai dit que j'allais te montrer comment on tient une épée. "); input()
print(Fore.CYAN + "Marchand : TU AS DIT QUE TU ALLAIS ME LA FAIRE AVALER ! "); input()
print(Fore.YELLOW + "Ferdinand : C'est possible que j'aie parlé un peu fort." + Fore.WHITE + "\nNarrateur : Deux gardes arrivent."); input()
print(Fore.CYAN + "Garde : Ferdinand ! Encore toi ? "); input()
print(Fore.YELLOW + "Ferdinand : Bonjour. "); input()
print(Fore.CYAN + "Garde : Tu es accusé de trouble à l'ordre public. "); input()
print(Fore.YELLOW + "Ferdinand : Pour une épée cassée ? "); input()
print(Fore.CYAN + "Garde : Pour avoir provoqué un rassemblement non autorisé. "); input()
print(Fore.BLUE + character.nom +" : Un rassemblement ? Il y a cinq personnes autour de nous." ); input()
print(Fore.CYAN + "Garde : Six, maintenant que tu es là. "); input()
print(Fore.BLUE + character.nom +" : C'est donc moi qui ai organisé le rassemblement ?"); input()
print(Fore.CYAN + "Garde : Tu poses beaucoup de questions. "); input()
print(Fore.BLUE + character.nom + " : C'est généralement ce qu'on fait quand les réponses n'ont aucun sens."); input()
print(Fore.CYAN + "Garde : Monsieur Arnaud a interdit les rassemblements susceptibles de perturber la paix."); input()
print(Fore.YELLOW + "Ferdinand : Alors je vais perturber sa paix." + Fore.WHITE + "\nNarrateur : Il fait craquer ses doigts."); input()
print(Fore.BLUE + character.nom + " : Tu ne peux pas simplement leur parler ? "); input()
print(Fore.YELLOW + "Ferdinand : Bien sûr que si." + Fore.WHITE + "\nNarrateur : Ferdinand s'avance vers les gardes avec un grand sourire."); input()
print(Fore.YELLOW + "Ferdinand : Bonjour. Pourriez-vous partir avant que je vous jette dans la fontaine ? "); input()
print(Fore.BLUE + character.nom + " : Ce n'est pas vraiment ce que j'appelle parler ! "); input()
print(Fore.YELLOW + "Ferdinand : Pourtant, j'ai utilisé des mots. "); input()
print(Fore.CYAN + "Garde : Attrapez-les ! "); input()

choix=int(input("Comment " + character.nom + " réagit-il ?\n1 = Prendre la défense du marchand\n2 = Prendre la défense de Ferdinand\n3 = Proposer un arrangement\n"))

if choix==1:
    print(Fore.BLUE + character.nom+" : Ferdinand, tu dois payer. Tu ne peux pas casser les affaires des gens et partir comme si de rien n'était. "); input()
    print(Fore.YELLOW + "Ferdinand : Je ne comptais pas partir comme si de rien n'était. "); input()
    print(Fore.BLUE + character.nom +" : Ah bon ? "); input()
    print(Fore.YELLOW + "Ferdinand : Je comptais partir en courant. "); input()
    print(Fore.BLUE + character.nom + " : Ça ne règle pas le problème. "); input()
    print(Fore.YELLOW + "Ferdinand : Je commence à comprendre pourquoi les gens ne t'invitent pas aux fêtes. "); input()
    print(Fore.WHITE +"Narrateur : " + character.nom + " insiste pour que Ferdinand propose une réparation. Le marchand accepte de lui laisser une chance, mais les gardes arrivent avant que l'accord puisse être conclu."); input()

if choix==2:
    print(Fore.BLUE + character.nom+" : Il a peut-être une bonne raison. Laisse-lui une chance de s'expliquer."); input()
    print(Fore.CYAN + "Marchand : Sa bonne raison, c'est qu'il a la force de casser tout ce qu'il touche !"); input()
    print(Fore.YELLOW + "Ferdinand : Ce n'est pas vrai." + Fore.WHITE + "\nNarrateur : Il se retourne et heurte accidentellement un présentoir. Plusieurs paniers tombent."); input()
    print(Fore.YELLOW + "Ferdinand : ... La plupart du temps." + Fore.WHITE + "\nNarrateur : Le marchand appelle les gardes." + character.nom + " se retrouve entraîné dans le conflit."); input()

if choix==3:
    print(Fore.BLUE + character.nom +" : Ferdinand aide le marchand pendant quelques jours et sa dette sera réglée."); input()
    print(Fore.CYAN + "Marchand : Il est capable de casser mes étals ! "); input()
    print(Fore.YELLOW + "Ferdinand : Je peux porter les caisses ! "); input()
    print(Fore.CYAN + "Marchand : Sans les lancer ? "); input()
    print(Fore.YELLOW + "Ferdinand : Je ne promets rien." + Fore.WHITE + "\nNarrateur : Après une longue négociation, le marchand accepte. Ferdinand commence à porter une caisse et la pose beaucoup trop brutalement."); input()
    print(Fore.CYAN + "Marchand : DOUCEMENT ! "); input()
    print(Fore.YELLOW + "Ferdinand : Je l'ai posée ! "); input()
    print(Fore.CYAN + "Marchand : Tu l'as enterrée !" + Fore.WHITE + "\nNarrateur : Les gardes arrivent et interrompent les négociations. "); input()
    print(Fore.WHITE + "Narrateur : Ferdinand part se caché et " + character.nom + "  se retrouve à combattre les gardes tout seul."); input()

List_player=[character]; diff=11
character.set_maxvie()
fight()

#############################################################
#                                                           #
#   Act 2 - Scène 3                                         #
#   le marchand et le symbole noir                          #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Le marchand s'approche, encore tremblant. "); input()
print(Fore.CYAN + "Marchand : Vous êtes complètement fou. Les gardes reviendront avec davantage d'hommes ! "); input()
print(Fore.WHITE + "Narrateur : Ferdinand reviens en courant"); input()
print(Fore.YELLOW + "Ferdinand : Piouf... Désolé, j’avais une envie folle de courir "); input()
print(Fore.BLUE + character.nom+" : T’es stupide ou quoi, tu m’as laissé seul contre les gardes ! "); input()
print(Fore.YELLOW + "Ferdinand : Mais Mr le Marchant pourquoi sont-ils aussi agressifs ces gardes ?" ); input()
print(Fore.CYAN + "Marchand : Parce que tout ce qui dérange Monsieur Arnaud est désormais considéré comme une menace. "); input()
print(Fore.YELLOW + "Ferdinand : Même une épée cassée ? "); input()
print(Fore.CYAN + "Marchand : Surtout si elle appartient à quelqu'un qui ne sait pas se taire." + Fore.WHITE + "\nNarrateur : Le marchand jette un regard autour de lui, puis baisse la voix. "); input()
print(Fore.CYAN + "Marchand : Depuis plusieurs semaines, les hommes d'Arnaud recherchent des objets anciens. Des livres, des reliques, des armes royales. Ils paient très cher pour les obtenir. "); input()
print(Fore.BLUE + character.nom+" : Pourquoi ?" ); input()
print(Fore.CYAN + "Marchand : Je ne sais pas. Mais ils ont pris plusieurs caisses à un antiquaire. Celui qui a refusé de les aider a été arrêté. "); input()
print(Fore.YELLOW + "Ferdinand : C'est honteux. "); input()
print(Fore.CYAN + "Marchand : Tu viens de menacer de me faire avaler une épée. "); input()
print(Fore.YELLOW + "Ferdinand : C'était différent. "); input()
print(Fore.CYAN + "Marchand : En quoi ? "); input()
print(Fore.YELLOW + "Ferdinand : Je ne t'ai pas arrêté. "); input()
print(Fore.WHITE + "Narrateur : " + character.nom + " remarque une caisse près de l'étal. Un symbole y est gravé : un cercle noir traversé d'une ligne rouge. "); input()
print(Fore.BLUE + character.nom + " : Ce symbole... Tu sais ce qu'il signifie ? "); input()
print(Fore.WHITE + "Narrateur : Le marchand pâlit. "); input()
print(Fore.CYAN + "Marchand : Il était sur les caisses que les gardes ont emportées."); input()
print(Fore.BLUE + character.nom +" : Où les ont-ils prises ? "); input()
print(Fore.CYAN + "Marchand : Dans une vieille chapelle, à l'est de la ville. Ils ont aussi emmené un homme qui vivait là. "); input()
print(Fore.YELLOW + "Ferdinand : Un prêtre ? "); input()
print(Fore.CYAN + "Marchand : Je crois. Un homme calme, toujours habillé en noir et blanc doré. Il s'appelait Nathaniel."); input()
print(Fore.BLUE +character.nom+ " : Il est encore là-bas ? "); input()
print(Fore.CYAN + "Marchand : Je l'ignore. Mais si vous voulez en savoir davantage, vous devriez vous rendre à la chapelle. "); input()

choix=int(input("Quelle question poser au marchand ?\n1 = « Pourquoi ces objets intéressent-ils autant Arnaud ? »\n2 = « Combien paient-ils pour ces objets ? »\n3 = « Et vous, vous avez déjà essayé de leur vendre quelque chose ? »\n"))

if choix==1:
    print("Marchand : Je l'ignore, mais ses hommes semblent chercher quelque chose de très précis.")
if choix==2:
    print("Marchand : Assez pour que certains oublient leurs principes.")
if choix==3:
    print("Marchand : Je tiens à ma boutique. Et à ma tête, si possible...")

print(Fore.WHITE + "Narrateur : Ferdinand croise les bras. "); input()
print(Fore.YELLOW + "Ferdinand : Alors nous allons à la chapelle. "); input()
print(Fore.BLUE + character.nom+ " : Nous ? "); input()
print(Fore.YELLOW + "Ferdinand : Tu m'as aidé. Tu as l'air honnête. Et tu sembles avoir besoin de quelqu'un qui sait se battre. "); input()
print(Fore.BLUE + character.nom + " : Je n'ai pas besoin de quelqu'un qui menace les fontaines. "); input()
print(Fore.YELLOW + "Ferdinand : Je peux aussi menacer les puits. "); input()

choix=int(input(character.nom + " accepte-t-il Ferdinand ?\n1 = L'accepter dans le groupe\n2 = Lui demander de régler sa dette d'abord\n"))

if choix==1:
    print(Fore.BLUE + character.nom + " : D'accord. Mais tu m'écoutes quand je te dis de ne pas foncer tête baissée.") ; input()
    print(Fore.YELLOW + "Ferdinand : Marché conclu ! "); input()
    print(Fore.BLUE + character.nom + " : Tu viens de serrer la main d'un inconnu sans discuter. "); input()
    print(Fore.YELLOW + "Ferdinand : Tu m'as aidé. C'est suffisant. "); input()
    print(Fore.WHITE + "Narrateur : Ferdinand rejoint le groupe. Il promet de faire des efforts pour réfléchir avant d'agir."); input()

if choix==2:
    print(Fore.BLUE + character.nom + " : On part ensemble quand tu auras réparé tes erreurs. "); input()
    print(Fore.YELLOW + "Ferdinand : Très bien." + Fore.WHITE + "\nNarrateur : Ferdinand aide le marchand à déplacer les caisses. Il renverse un panier, s'excuse sincèrement, puis en renverse un deuxième. "); input()
    print(Fore.CYAN + "Marchand : Tu sais quoi ? Va sauver le royaume. Ça me coûtera moins cher."); input()
    print(Fore.WHITE + "Narrateur : Ferdinand rejoint le groupe. "); input()

#############################################################
#                                                           #
#   Act 2 - Scène 4                                         #
#   Vers la chapelle                                        #
#                                                           #
#############################################################

print(Fore.BLUE + character.nom + " et Ferdinand quittent le marché. La foule s'écarte devant la carrure imposante du combattant. "); input()
print(Fore.BLUE + character.nom + " : Tu es toujours aussi calme ? "); input()
print(Fore.YELLOW + "Ferdinand : Je suis très calme. "); input()
print(Fore.BLUE + character.nom + " : Tu as menacé un marchand, défié des gardes et parlé de jeter des gens dans une fontaine. "); input()
print(Fore.YELLOW + "Ferdinand : Et je ne me suis énervé qu'une seule fois. "); input()
print(Fore.BLUE + character.nom + " : Quand ? "); input()
print(Fore.YELLOW + "Ferdinand : Quand tu as parlé de la fontaine. Je préfère les puits. "); input()
print(Fore.WHITE + "Narrateur : " + character.nom + " soupire"); input()
print(Fore.YELLOW + "Ferdinand : Tu sais, je ne suis pas un mauvais gars. "); input()
print(Fore.BLUE + character.nom + " : Je n'ai pas dit ça. "); input()
print(Fore.YELLOW + "Ferdinand : Les gens pensent souvent que parce que je suis grand, je dois être violent."); input()
print(Fore.BLUE + character.nom + " : Tu viens de menacer trois personnes en moins de dix minutes. "); input()
print(Fore.YELLOW + "Ferdinand : C'est un mauvais exemple." + Fore.WHITE + "\nNarrateur : Il se gratte la tête, gêné. "); input()
print(Fore.YELLOW + "Ferdinand : Mais je n'aime pas voir les gens se faire écraser. Le marchand avait raison pour l'épée. Je lui devais de l'argent. J'aurais dû régler ça autrement. "); input()
print(Fore.BLUE + character.nom + " : Tu pourrais commencer par t'excuser. "); input()
print(Fore.YELLOW + "Ferdinand : Je l'ai fait. "); input()
print(Fore.BLUE + character.nom + " : Tu lui as dit que le rocher était mal placé. "); input()
print(Fore.YELLOW + "Ferdinand : C'était une excuse. "); input()
print(Fore.BLUE + character.nom + " : C'était une accusation contre un rocher. "); input()
print(Fore.WHITE + "Narrateur : Ferdinand réfléchit sérieusement.\n" + Fore.YELLOW + "Ferdinand : Tu es étonnamment difficile à convaincre. "); input()

choix=int(input("Comment réagir à ses explications ?\n1 =  « Tu n'es peut-être pas aussi idiot que tu en as l'air. »\n2 = « Tu devrais apprendre à réfléchir avant d'agir. »\n3 = « Au moins, tu as de bonnes intentions... »\n"))

if choix==1:
    print("Ferdinand : Merci... Je crois.")
if choix==2:
    print("Ferdinand : J'y travaille. Mais c'est fatigant.")
if choix==3:
    print("Ferdinand : C'est déjà un bon début, non ?")
    print(character.nom + " : En effet...")


print(Fore.WHITE + "Narrateur : Au loin, les tours d'une vieille chapelle se dessinent à travers les arbres."); input()
print(Fore.BLUE + character.nom + " : Allons voir ce que ce Nathaniel sait. "); input()
print(Fore.YELLOW + "Ferdinand : Et après ? "); input()
print(Fore.BLUE + character.nom + " : Nous découvrirons ce qu'Arnaud cherche. "); input()
print(Fore.YELLOW + "Ferdinand : Et ensuite, nous le frapperons ? "); input()
print(Fore.BLUE + character.nom +" : Nous aviserons. "); input()
print(Fore.YELLOW + "Ferdinand : J'aime bien les plans qui laissent de la place à l'improvisation."); input()

#############################################################
#                                                           #
#   Act 3 - Scène 1                                         #
#   la vieille chapelle                                     #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Lieu : Une chapelle abandonnée à l'est de la capitale de Monte Cristo. "); input()
print(Fore.WHITE + "Narrateur : " + character.nom + " et Ferdinand suivent un chemin étroit à travers les arbres. Le vent fait grincer les branches. La chapelle apparaît au sommet d'une petite colline.\nNarrateur : Son toit est abîmé, ses vitraux sont brisés et des traces de pas traversent la boue devant l'entrée. "); input()
print(Fore.YELLOW + "Ferdinand : Charmant." ); input()
print(Fore.BLUE +character.nom + " : Tu trouves ? "); input()
print(Fore.YELLOW + "Ferdinand : Il y a une porte. J'aime les endroits avec des portes. "); input()
print(Fore.BLUE +character.nom + " : C'est le critère le plus bas que j'aie jamais entendu. "); input()
print(Fore.YELLOW + "Ferdinand : Je suis un homme simple. "); input()
print(Fore.BLUE +character.nom + " remarque le symbole noir sur la porte. "); input()
print(Fore.BLUE +character.nom + " : C'est le même symbole que sur la caisse." ); input()
print(Fore.YELLOW + "Ferdinand : Alors nous sommes au bon endroit. "); input()
print(Fore.BLUE +character.nom + " : Ou dans un piège. "); input()
print(Fore.YELLOW + "Ferdinand : C'est souvent la même chose. "); input()

choix=int(input("Comment entrer dans la chapelle ?\n1 = « Entrons discrètement. »\n2 = « Ferdinand, ouvre-nous ça. »\n"))

if choix==1:
    print("Ferdinand : Je peux être discret.")
    print(character.nom + " : C'est précisément ce qui m'inquiète...")
if choix==2:
    print("Ferdinand : Enfin une mission à ma hauteur.")
    print(character.nom + " : C'était simplement une façon de parler...")

print(Fore.WHITE + "Narrateur : Des voix proviennent de l'intérieur. "); input()
print(Fore.CYAN + "Garde : Où sont les documents ? "); input()
print(Fore.RED + "Voix inconnue : Je vous ai déjà dit que vous ne les aurez pas. "); input()
print(Fore.CYAN + "Garde : Monsieur Arnaud ne vous laissera pas le choix. "); input()
print(Fore.RED + "Voix inconnue : Alors dites-lui que je préfère encore désobéir." ); input()
print(Fore.YELLOW + "Ferdinand : Je l'aime bien, ce type. "); input()
print(Fore.BLUE +character.nom + " : Tu ne le connais pas. "); input()
print(Fore.YELLOW + "Ferdinand : Il a l'air de savoir dire non. C'est une qualité. "); input()
print(Fore.WHITE + "Narrateur : " + character.nom + " entrouvre la porte. À l'intérieur, plusieurs gardes encerclent un prêtre vêtu d'une robe sombre. Il tient un vieux livre contre lui."); input()

#############################################################
#                                                           #
#   Act 3 - Scène 2                                         #
#   Nathaniel                                               #
#                                                           #
#############################################################

print(Fore.CYAN + "Garde : Nathaniel, vous êtes accusé de dissimulation de documents interdits."); input()
print(Fore.RED + "Nathaniel : Ce sont des archives historiques. "); input()
print(Fore.CYAN + "Garde : Elles contiennent des informations sur le Coeur de Bedrock."); input()
print(Fore.RED + "Nathaniel : Des informations que votre maître aurait dû laisser enfouies."); input()
print(Fore.CYAN + "Garde : Dernier avertissement. "); input()
print(Fore.RED + "Nathaniel : Vous devriez en profiter pour réfléchir à vos choix. "); input()
print(Fore.CYAN + "Garde : Assez ! "); input()
print(Fore.WHITE + "Narrateur : Le garde s'avance. Tandis que " + character.nom + " ouvre la porte en grand. "); input()
print(Fore.BLUE + character.nom + " : Laissez-le tranquille. "); input()
print(Fore.RED + "Nathaniel : Je vous remercie de votre intervention, mais je crains que vous ne veniez d'aggraver votre situation. "); input()
print(Fore.BLUE + character.nom + " : Pourquoi ? "); input()
print(Fore.RED + "Nathaniel : Parce qu'ils sont plus nombreux que nous. "); input()
print(Fore.YELLOW + "Ferdinand : Enfin une remarque utile ! "); input()
print(Fore.BLUE + character.nom + " : Tu aurais préféré qu'il dise qu'ils sont moins nombreux ? "); input()
print(Fore.YELLOW + "Ferdinand : Cela aurait été encourageant. "); input()
print(Fore.WHITE + "Narrateur : Andy arrive tranquillement entrain de manger du pain"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je suis absent cinq minutes et vous trouvez déjà le moyen de vous faire tuer dans une chapelle. "); input()
print(Fore.BLUE + character.nom + " : Comment tu es arrivé ici ? "); input()
print(Fore.LIGHTBLACK_EX + "Andy : J'ai suivi les bruits de dispute. C'est devenu une méthode de navigation étonnamment efficace. "); input()
print(Fore.CYAN + "Garde : Attrapez-les ! "); input()
print(Fore.WHITE + "Narrateur : Le combat commence. Les gardes tentent d'encercler le groupe."); input()

List_player=[character,Andy,Nath] ; stade_equipe=1 ; diff=11
fight()

print(Fore.WHITE + "Narrateur : Après le combat, les soldats prennent la fuite."); input()
print(Fore.YELLOW + "Ferdinand : Nous aurions dû en garder un pour lui poser des questions."); input()
print(Fore.BLUE + character.nom + " : Tu pouvais simplement le retenir."); input()
print(Fore.YELLOW + "Ferdinand : Je l'ai retenu.") ; input()
print(Fore.BLUE + character.nom + " : Tu l'as envoyé contre une colonne.") ; input()
print(Fore.YELLOW + "Ferdinand : Il s'est retenu tout seul après.") ; input()
print(Fore.WHITE + "Narrateur : Nathaniel ferme la porte de la chapelle et pose le livre sur un autel.") ; input()
print(Fore.RED + "Nathaniel : Je suppose que je vous dois des explications.") ; input()
print(Fore.BLUE + character.nom + " : Tu pourrais commencer par ton nom.") ; input()
print(Fore.RED + "Nathaniel : Nathaniel. Prêtre, archiviste et, apparemment, fugitif.") ; input()
print(Fore.YELLOW + "Ferdinand : Ferdinand. Combattant.") ; input()
print(Fore.LIGHTBLACK_EX + "Andy : Andy. Musicien, artiste et victime permanente de la censure.") ; input()
print(Fore.BLUE + character.nom + " : " + character.nom + ". Voyageur, apparemment aimant les ennuis.") ; input()
print(Fore.RED + "Nathaniel : Vous formez un groupe très inhabituel.") ; input()
print(Fore.LIGHTBLACK_EX + "Andy : Nous avons déjà entendu pire.") ; input()
print(Fore.BLUE + character.nom + " : Par qui ?") ; input()
print(Fore.LIGHTBLACK_EX + "Andy : Par le public de mon dernier concert."); input()

#############################################################
#                                                           #
#   Act 3 - Scène 3                                         #
#   le coeur de bedrock                                     #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Nathaniel ouvre le vieux livre. Les pages sont couvertes de symboles, de cartes et de notes écrites à plusieurs époques."); input()
print(Fore.RED + "Nathaniel : Ce que je vais vous révéler ne doit pas sortir de cette chapelle. Il y a plusieurs siècles, les souverains de Monte Cristo possédaient un artefact appelé le Coeur de bedrock."); input()
print(Fore.BLUE + character.nom + " : Un bijou ?"); input()
print(Fore.RED + "Nathaniel : Un artefact ancien. Il serait capable d'influencer la volonté des autres."); input()
print(Fore.YELLOW + "Ferdinand : Comme leur dire quoi faire ?"); input()

print(Fore.RED + "Nathaniel : Plus que cela. Certains textes parlent d'une simple suggestion. D'autres évoquent un contrôle presque total."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Donc une sorte de couronne magique qui transforme son propriétaire en dictateur ?"); input()
print(Fore.RED + "Nathaniel : Ce n'est pas exactement une couronne."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je comprends. Le problème est qu'il manque un chapeau."); input()
print(Fore.RED + "Nathaniel : Ce n'est pas le moment."); input()
print(Fore.LIGHTBLACK_EX + "Andy : C'est rarement le moment, avec toi."); input()
print(Fore.WHITE + "Narrateur : Nathaniel tourne une page."); input()
print(Fore.RED + "Nathaniel : Le Coeur n'agit pas de la même façon sur tout le monde. Il amplifie ce qui existe déjà chez son porteur. Une personne généreuse pourrait vouloir protéger les autres. Une personne dominatrice pourrait vouloir les contrôler."); input()
print(Fore.BLUE + character.nom + " : Et Arnaud veut le trouver."); input()
print(Fore.RED + "Nathaniel : Oui. Depuis des mois, ses hommes fouillent les anciennes forteresses, les cryptes et les bibliothèques royales."); input()
print(Fore.YELLOW + "Ferdinand : Pourquoi personne ne l'arrête ?"); input()
print(Fore.RED + "Nathaniel : Parce qu'Arnaud contrôle l'armée. Et parce que les habitants ne savent pas ce qu'il recherche."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Et parce qu'une bonne partie des gens préfère ne pas finir dans une cellule."); input()
print(Fore.RED + "Nathaniel : Exactement."); input()
print(Fore.WHITE + "Narrateur : Il referme un instant le livre."); input()
print(Fore.RED + "Nathaniel : Vous devez comprendre quelque chose. Arnaud n'a pas commencé comme un tyran aux yeux de tous. Il a pris le pouvoir après une guerre. Il a promis la stabilité. Beaucoup de gens l'ont soutenu."); input()
print(Fore.BLUE + character.nom + " : Et ensuite ?"); input()
print(Fore.RED + "Nathaniel : Il a progressivement supprimé toute opposition. Il a réécrit l'histoire et fait disparaître les témoins."); input()
print(Fore.YELLOW + "Ferdinand : Il a donc menti à tout le monde."); input()
print(Fore.RED + "Nathaniel : Les mensonges les plus dangereux sont souvent ceux qui commencent par une vérité."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je vais noter ça. Ça ferait une excellente phrase dans une chanson."); input()
print(Fore.RED + "Nathaniel : À condition de ne pas en faire un refrain de cinq minutes."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je ne promets rien.") ; input()

choix=int(input("Qu'est ce que " + character.nom + " pensera de l'artéfact ?\n1 = « Il faut absolument le détruire. »\n2 = « Il pourrait être utile entre de bonnes mains. »\n3 = « Je commence à comprendre pourquoi Arnaud le veut. »\n"))

if choix==1:
    print("Nathaniel : C'est une possibilité, mais nous devons d'abord comprendre ses conséquences.")
if choix==2:
    print("Nathaniel : C'est précisément le genre de raisonnement qui peut devenir dangereux.")
    pre_req_EvilEnding=1
if choix==3:
    print("Andy : Moi, je commence surtout à comprendre pourquoi nous avons besoin de vacances.")
    print(character.nom + " : On vient à peine de commencer les recherches et tu veux déjà des vacances ?")

#############################################################
#                                                           #
#   Act 3 - Scène 4                                         #
#   disparition de la dynastie                              #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Nathaniel sort une carte ancienne."); input()
print(Fore.RED + "Nathaniel : La famille royale a disparu il y a quinze ans. Les documents officiels affirment que le roi a trahi son peuple et provoqué la guerre civile."); input()
print(Fore.BLUE + character.nom + " : Tu n'y crois pas ?"); input()
print(Fore.RED + "Nathaniel : Les registres ont été modifiés. Certaines dates ne correspondent pas. Des signatures ont été copiées. Des pages entières ont été arrachées."); input()
print(Fore.YELLOW + "Ferdinand : Tu peux le prouver ?"); input()
print(Fore.RED + "Nathaniel : Pas encore. Mais une dernière référence mentionne un témoin : un ancien conseiller royal qui aurait survécu à la guerre."); input()
print(Fore.BLUE + character.nom + " : Où est-il ?"); input()
print(Fore.RED + "Nathaniel : Je l'ignore. Les archives ne donnent aucun nom, seulement un lieu : les anciennes archives de la capitale."); input()

choix=int(input("Que faire de cette information ?\n1 = « Il faut retrouver ce témoin. »\n2 = « On devrait d'abord vérifier les archives. »\n3 = « Et si ce témoin est mort depuis quinze ans ? »\n"))

if choix==1:
    print("Nathaniel : C'est notre meilleure piste.")
if choix==2:
    print("Nathaniel : Une approche prudente. J'apprécie.")
if choix==3:
    print("Andy : Alors nous aurons fait tout ce chemin pour parler à un fantôme.")

print(Fore.LIGHTBLACK_EX + "Andy : Donc nous devons aller dans un bâtiment rempli de gardes pour chercher des documents qu'on nous interdit de lire."); input()
print(Fore.BLUE + character.nom + " : En résumé, oui."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je préfère les quêtes où l'objectif est de retrouver un chat."); input()
print(Fore.YELLOW + "Ferdinand : Tu sais retrouver un chat ?"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Non, mais je peux chanter pour l'attirer."); input()
print(Fore.YELLOW + "Ferdinand : Et si ça ne marche pas ?"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je lui laisse un avis négatif."); input()
print(Fore.WHITE + "Narrateur : Nathaniel déroule un autre parchemin."); input()
print(Fore.RED + "Nathaniel : Les archives mentionnent aussi une vieille boulangerie située près de la capitale. Elle aurait servi de refuge aux messagers royaux pendant la guerre."); input()
print(Fore.BLUE + character.nom + " : Pourquoi une boulangerie ?"); input()
print(Fore.RED + "Nathaniel : Les messagers devaient pouvoir se déplacer sans attirer l'attention. Un livreur de pain était moins suspect qu'un soldat transportant des documents."); input()
print(Fore.YELLOW + "Ferdinand : Et il y avait du pain ?"); input()
print(Fore.RED + "Nathaniel : Probablement."); input()
print(Fore.YELLOW + "Ferdinand : Alors c'était une bonne stratégie."); input()
print(Fore.BLUE + character.nom + " : Nous allons chercher les documents. Ensuite, nous trouverons le sceau royal."); input()
print(Fore.RED + "Nathaniel : Attendez. Je n'ai pas encore accepté de vous accompagner."); input()
print(Fore.WHITE + "Narrateur : Silence."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Ah. C'est vrai. Nous venons de décider de toute votre vie sans vous demander votre avis."); input()
print(Fore.YELLOW + "Ferdinand : C'est plus rapide."); input()
print(Fore.RED + "Nathaniel : Je vois cela."); input()

#############################################################
#                                                           #
#   Act 3 - Scène 5                                         #
#   le choix                                                #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Nathaniel observe le groupe."); input()
print(Fore.RED + "Nathaniel : Vous savez que vous risquez votre vie en vous opposant à Arnaud. Pourquoi continuer ?"); input()

choix = int(input("Quelle est votre motivation ?\n1 = « Personne ne devrait vivre sous la peur. »\n2 = « Je veux découvrir la vérité sur le royaume. »\n3 = « Je veux devenir assez puissant pour qu'on ne puisse plus me menacer. »\n"))

if choix == 1:
    print(Fore.BLUE + character.nom + " : Il fait arrêter des innocents. Quelqu'un doit l'arrêter."); input()
    print(Fore.RED + "Nathaniel : Une réponse simple. Mais parfois, les réponses simples sont les plus difficiles à suivre."); input()
    print(Fore.BLUE + character.nom + " : Tu viens avec nous ?"); input()
    print(Fore.RED + "Nathaniel : Oui. Je ne peux pas continuer à protéger des livres pendant que les gens qui les ont écrits sont oubliés."); input()
    print(Fore.WHITE + "Narrateur : Nathaniel rejoint le groupe avec conviction."); input()

elif choix == 2:
    print(Fore.BLUE + character.nom + " : Je ne supporte pas qu'on nous cache ce qui s'est passé. Si Arnaud ment sur son passé, je veux savoir pourquoi."); input()
    print(Fore.RED + "Nathaniel : La vérité peut être dangereuse. Mais l'ignorance l'est parfois davantage."); input()
    print(Fore.BLUE + character.nom + " : Alors, cherchons-la."); input()
    print(Fore.RED + "Nathaniel : Très bien. Je vous accompagnerai. Mais je vous préviens : je ne laisserai personne détruire les archives pour obtenir une victoire facile."); input()
    print(Fore.WHITE + "Narrateur : Nathaniel rejoint le groupe pour enquêter."); input()

elif choix == 3:
    print(Fore.BLUE + character.nom + " : Je ne veux plus jamais être impuissant. Je veux être capable de me défendre."); input()
    print(Fore.RED + "Nathaniel : Je comprends cette peur. Mais prends garde à ne pas devenir ce que tu combats."); input()
    print(Fore.BLUE + character.nom + " : Je sais faire la différence."); input()
    print(Fore.RED + "Nathaniel : Je l'espère."); input()
    print(Fore.WHITE + "Narrateur : Nathaniel rejoint le groupe, mais il surveillera attentivement les décisions de " + character.nom + "."); input()

#############################################################
#                                                           #
#   Act 3 - Scène 6                                         #
#   le départ                                               #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : La nuit tombe. Nathaniel range les documents dans une sacoche."); input()
print(Fore.RED + "Nathaniel : Nous devons partir avant le lever du soleil. Les gardes reviendront."); input()
print(Fore.YELLOW + "Ferdinand : Je peux rester ici et les attendre."); input()
print(Fore.BLUE + character.nom + " : Non."); input()
print(Fore.YELLOW + "Ferdinand : Pourquoi ?"); input()
print(Fore.BLUE + character.nom + " : Parce qu'ils reviendraient à cinquante."); input()
print(Fore.YELLOW + "Ferdinand : Je peux en combattre cinquante."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Et le cinquante et unième ?"); input()
print(Fore.YELLOW + "Ferdinand : Je lui demanderai d'attendre son tour."); input()
print(Fore.WHITE + "Narrateur : Nathaniel secoue la tête, amusé malgré lui."); input()
print(Fore.RED + "Nathaniel : La boulangerie se trouve à une demi-journée de marche. Nous y trouverons peut-être les preuves dont nous avons besoin."); input()
print(Fore.BLUE + character.nom + " : Et si nous ne trouvons rien ?"); input()
print(Fore.RED + "Nathaniel : Alors nous aurons traversé la campagne pour visiter une vieille boulangerie."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Enfin une quête avec une récompense qui m'intéresse."); input()
print(Fore.WHITE + "Narrateur : Le groupe quitte la chapelle. Avant de fermer la porte, Nathaniel se retourne une dernière fois vers l'autel."); input()
print(Fore.RED + "Nathaniel : Si Arnaud recherche le Coeur de Bedrock, c'est qu'il sait quelque chose que nous ignorons."); input()
print(Fore.BLUE + character.nom + " : Quoi donc ?"); input()
print(Fore.RED + "Nathaniel : Peut-être que l'artefact n'a jamais été détruit."); input()
print(Fore.WHITE + "Narrateur : La porte se referme."); input()

farm=2
while farm!=1:
    freetime=int(input("--------------------------\nQu'est ce que vous souhaitez faire ?\n1 = Allez battre des monstres.\n2 = Allez chez le forgeron.\n3 = Allez chez le vendeur."))
    if freetime==1:
        List_player=[character,Andy,Nath] ; diff=2 ; stade_equipe=1
        fight()
        if randint(1,10)==1:
            character.set_maxvie() ; Andy.set_maxvie() ; Nath.set_maxvie()
    elif freetime==2:
        armurerie()
    elif freetime==3:
        shop_heal()
    farm=int(input("Voulez vous continuez de profiter de votre temps libre ?\n1 = OUI\n2 = NON\n"))
print(Fore.WHITE + "Narrateur : Après ce temps libre, les joyeux lurons allèrent dans une auberge pour la nuit avant de partir pour un très long voyage le lendemain."); input()

#############################################################
#                                                           #
#   Act 4 - Scène 1                                         #
#   la boulangerie                                          #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Lieu : Une ancienne boulangerie à l'extérieur de la capitale."); input()

print(Fore.WHITE + "Narrateur : Le groupe suit la carte de Nathaniel. La route devient plus étroite et les habitations se font rares."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Nous marchons depuis des heures."); input()
print(Fore.YELLOW + "Ferdinand : Une demi-journée, c'est normal."); input()
print(Fore.LIGHTBLACK_EX + "Andy : J'ai mal aux pieds."); input()
print(Fore.YELLOW + "Ferdinand : Tu aurais dû prendre de meilleures chaussures."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je suis musicien. Mes pieds sont conçus pour marcher jusqu'à une scène, pas jusqu'à une ruine."); input()
print(Fore.BLUE + character.nom + " : Tu as des chaussures tout à fait normales."); input()
print(Fore.LIGHTBLACK_EX + "Andy : C'est ce que tu crois. Elles ont une âme artistique."); input()
print(Fore.RED + "Nathaniel : Les chaussures n'ont pas d'âme."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Voilà pourquoi tu n'as jamais écrit de chanson célèbre."); input()
print(Fore.WHITE + "Narrateur : Au détour d'un chemin, une vieille bâtisse apparaît. Le toit est partiellement effondré, mais une fine fumée s'échappe de la cheminée."); input()
print(Fore.BLUE + character.nom + " : La boulangerie ?"); input()
print(Fore.RED + "Nathaniel : C'est bien l'endroit indiqué sur la carte."); input()
print(Fore.YELLOW + "Ferdinand : Il y a de la fumée."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Ce qui signifie soit qu'il y a quelqu'un, soit que le bâtiment a développé une activité criminelle."); input()
print(Fore.BLUE + character.nom + " : Comment un bâtiment pourrait-il devenir criminel ?"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je ne veux pas limiter ses ambitions."); input()
print(Fore.WHITE + "Narrateur : Le groupe s'approche de la porte."); input()
print(Fore.YELLOW + "Ferdinand : Je frappe ?"); input()
print(Fore.BLUE + character.nom + " : Non."); input()
print(Fore.YELLOW + "Ferdinand : Je frappe doucement ?"); input()
print(Fore.BLUE + character.nom + " : Non plus."); input()
print(Fore.YELLOW + "Ferdinand : Tu es difficile."); input()
print(Fore.WHITE + "Narrateur : " + character.nom + " frappe normalement. Une voix répond de l'intérieur."); input()
print(Fore.MAGENTA + "Inconnu : Entrez. La porte n'est pas verrouillée."); input()
print(Fore.WHITE + "Narrateur : Le groupe échange un regard, puis entre.") ; input()

#############################################################
#                                                           #
#   Act 4 - Scène 2                                         #
#   Ethan                                                   #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : À l'intérieur, un jeune homme est assis près d'un four éteint. Il lit une lettre, calme et parfaitement à l'aise."); input()
print(Fore.MAGENTA + "Inconnu : Vous êtes en retard."); input()
print(Fore.BLUE + character.nom + " : Pardon ?"); input()
print(Fore.MAGENTA + "Inconnu : Je vous attendais."); input()
print(Fore.LIGHTBLACK_EX + "Andy : C'est une phrase qu'on entend rarement dans un endroit où personne ne devrait vivre."); input()
print(Fore.WHITE + "Narrateur : L'homme replie sa lettre et se lève."); input()
print(Fore.MAGENTA + "Inconnu : Ethan. Enchanté."); input()
print(Fore.BLUE + character.nom + " : Comment savais-tu que nous viendrions ?"); input()
print(Fore.MAGENTA + "Ethan : Je ne le savais pas. Mais quelqu'un qui suit une vieille carte finit généralement par arriver ici."); input()
print(Fore.RED + "Nathaniel : Qui t'a donné cette information ?"); input()
print(Fore.MAGENTA + "Ethan : Disons que j'ai des connaissances."); input()
print(Fore.YELLOW + "Ferdinand : Tu es un espion ?"); input()
print(Fore.MAGENTA + "Ethan : Si j'étais un espion, est-ce que je te le dirais ?"); input()
print(Fore.YELLOW + "Ferdinand : Probablement pas."); input()
print(Fore.MAGENTA + "Ethan : Alors tu progresses."); input()
print(Fore.WHITE + "Narrateur : Andy étouffe un rire."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je l'aime bien. Il a la même manière de parler que moi."); input()
print(Fore.BLUE + character.nom + " : Tu veux dire qu'il parle comme s'il savait tout ?"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Non. Comme s'il savait exactement ce qu'il faut dire pour que les autres pensent qu'il sait tout."); input()
print(Fore.MAGENTA + "Ethan : Une nuance importante."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Tu vois ? Il comprend mon art."); input()
print(Fore.WHITE + "Narrateur : Ethan remarque le livre de Nathaniel."); input()
print(Fore.MAGENTA + "Ethan : Vous cherchez les archives royales."); input()
print(Fore.BLUE + character.nom + " : Comment le sais-tu ?"); input()
print(Fore.MAGENTA + "Ethan : Parce que les gardes d'Arnaud ont fouillé cette boulangerie il y a deux jours. Ils cherchaient exactement la même chose."); input()
print(Fore.RED + "Nathaniel : Et qu'ont-ils trouvé ?"); input()
print(Fore.MAGENTA + "Ethan : Rien. Les documents sont cachés sous le four."); input()
print(Fore.WHITE + "Narrateur : Ferdinand s'avance immédiatement."); input()
print(Fore.YELLOW + "Ferdinand : Enfin, une mission utile."); input()
print(Fore.BLUE + character.nom + " : Attends."); input()
print(Fore.YELLOW + "Ferdinand : Quoi ?"); input()
print(Fore.BLUE + character.nom + " : Tu vas encore tout casser."); input()
print(Fore.YELLOW + "Ferdinand : Je n'ai rien cassé depuis le marché."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Cela fait presque une journée. Un record personnel."); input()
print(Fore.MAGENTA + "Ethan : Laissez-moi faire."); input()
print(Fore.WHITE + "Narrateur : Ethan pousse une brique descellée dans le mur. Un compartiment secret s'ouvre. Il en sort une boîte contenant plusieurs parchemins."); input()
print(Fore.RED + "Nathaniel : Tu connais donc cet endroit."); input()
print(Fore.MAGENTA + "Ethan : Mon père travaillait autrefois pour la cour royale. Il m'a appris quelques secrets avant de disparaître."); input()
print(Fore.WHITE + "Narrateur : Le groupe se tait."); input()
print(Fore.BLUE + character.nom + " : Disparaître comment ?"); input()
print(Fore.WHITE + "Narrateur : Ethan garde le silence quelques secondes."); input()
print(Fore.MAGENTA + "Ethan : Il s'est opposé à Arnaud. Un matin, il n'est jamais rentré."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je suis désolé."); input()
print(Fore.MAGENTA + "Ethan : Ne le sois pas. Je ne cherche pas la pitié. Je cherche des réponses."); input()
print(Fore.BLUE + character.nom + " : Et tu penses les trouver ici ?"); input()
print(Fore.MAGENTA + "Ethan : Je pense que les réponses sont partout. Il suffit de savoir où regarder."); input()
print(Fore.WHITE + "Narrateur : Il ouvre la boîte."); input()

#############################################################
#                                                           #
#   Act 4 - Scène 3                                         #
#   les archives                                            #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Les parchemins portent le sceau de l'ancienne dynastie. Nathaniel les examine avec précaution."); input()
print(Fore.RED + "Nathaniel : Ces documents sont authentiques. Ils datent de la dernière année du règne du roi."); input()
print(Fore.BLUE + character.nom + " : Que disent-ils ?"); input()
print(Fore.RED + "Nathaniel : Le roi avait ordonné le transfert du Coeur de Bedrock vers un sanctuaire sous le château. Il craignait qu'un conseiller ne s'en empare."); input()
print(Fore.YELLOW + "Ferdinand : Et ce conseiller, c'était Arnaud ?"); input()
print(Fore.RED + "Nathaniel : Tout porte à le croire."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Donc notre cher dirigeant a trahi son roi, réécrit l'histoire et veut maintenant récupérer l'objet qu'il avait promis de protéger."); input()
print(Fore.BLUE + character.nom + " : C'est une manière élégante de résumer la situation."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Merci. Je travaille sur un morceau intitulé « Les aventures d'un homme qui aurait dû rester conseiller »."); input()
print(Fore.MAGENTA + "Ethan : Il manque quelque chose."); input()
print(Fore.WHITE + "Narrateur : Ethan se penche sur le parchemin."); input()
print(Fore.MAGENTA + "Ethan : Le Coeur aurait été caché avec un second objet : le sceau royal."); input()
print(Fore.RED + "Nathaniel : Exact. Le sceau permettrait de réveiller l'artefact."); input()
print(Fore.BLUE + character.nom + " : Donc Arnaud doit retrouver les deux."); input()
print(Fore.RED + "Nathaniel : Oui. Sans le sceau, il ne pourrait pas exploiter tout le pouvoir du Coeur."); input()
print(Fore.YELLOW + "Ferdinand : Alors nous prenons le sceau avant lui."); input()
print(Fore.BLUE + character.nom + " : C'est probablement dans les archives de la capitale."); input()
print(Fore.MAGENTA + "Ethan : C'est ce que je pense."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Tu penses beaucoup de choses pour quelqu'un qui vient de nous rencontrer."); input()
print(Fore.MAGENTA + "Ethan : Et toi, tu poses beaucoup de questions pour quelqu'un qui n'a pas encore compris que les informations sont utiles."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Très bien. Je l'aime moins."); input()
print(Fore.WHITE + "Narrateur : Ethan sourit."); input()
print(Fore.MAGENTA + "Ethan : Je vais prendre cela comme un compliment."); input()


#############################################################
#                                                           #
#   Act 4 - Scène 4                                         #
#   la raison d'Ethan                                       #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Le groupe s'installe autour d'une vieille table. Ethan sort une carte de la capitale."); input()
print(Fore.MAGENTA + "Ethan : Vous avez deux possibilités pour atteindre les archives. La première est l'entrée principale, gardée jour et nuit. La seconde passe par un réseau de tunnels sous les anciennes rues."); input()
print(Fore.BLUE + character.nom + " : Et comment connais-tu ces tunnels ?"); input()
print(Fore.MAGENTA + "Ethan : Mon père me les a montrés quand j'étais enfant. Ils servaient à déplacer les documents royaux sans attirer l'attention."); input()
print(Fore.RED + "Nathaniel : Si les gardes découvrent que tu connais ces passages, tu seras recherché."); input()
print(Fore.MAGENTA + "Ethan : Je le suis déjà."); input()
print(Fore.YELLOW + "Ferdinand : Alors autant les utiliser."); input()
print(Fore.BLUE + character.nom + " : Pourquoi ne pas partir seul ? Si tu connais les passages, tu pourrais entrer, récupérer les documents et disparaître."); input()
print(Fore.MAGENTA + "Ethan : Parce que les gardes ont renforcé les accès. Et parce que je ne peux pas faire tout cela seul."); input()
print(Fore.BLUE + character.nom + " : Tu pourrais chercher d'autres personnes."); input()
print(Fore.MAGENTA + "Ethan : J'en ai rencontré beaucoup. La plupart veulent de l'argent. Certains veulent se venger. D'autres veulent prendre la place d'Arnaud."); input()
print(Fore.RED + "Nathaniel : Et toi ?"); input()
print(Fore.WHITE + "Narrateur : Ethan fixe Nathaniel."); input()
print(Fore.MAGENTA + "Ethan : Je veux que personne ne puisse plus jamais décider de la vie des autres."); input()
print(Fore.WHITE + "Narrateur : La réponse semble satisfaire Nathaniel. Mais Ethan détourne les yeux vers sa lettre."); input()
print(Fore.MAGENTA + "Ethan : Mon père croyait qu'il suffisait de dire la vérité pour faire changer les choses. Il a découvert que les gens au pouvoir peuvent enterrer la vérité sous des montagnes de mensonges."); input()
print(Fore.BLUE + character.nom + " : Tu ne veux pas simplement faire tomber Arnaud. Tu veux comprendre ce qui est arrivé à ton père."); input()
print(Fore.MAGENTA + "Ethan : Les deux."); input()
print(Fore.WHITE + "Narrateur : Un silence s'installe."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je vais faire une exception et ne pas plaisanter."); input()
print(Fore.YELLOW + "Ferdinand : C'est grave, alors."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Très grave."); input()

#############################################################
#                                                           #
#   Act 4 - Scène 5                                         #
#   faire confiance à Ethan ?                               #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Ethan pose la carte sur la table."); input()
print(Fore.MAGENTA + "Ethan : Je peux vous guider dans les tunnels. Je connais les passages, les postes de garde et plusieurs endroits où nous pourrons nous cacher."); input()
print(Fore.BLUE + character.nom + " : Et pourquoi devrions-nous te faire confiance ?"); input()
print(Fore.MAGENTA + "Ethan : Vous ne devriez pas. Pas encore."); input()
print(Fore.WHITE + "Narrateur : Cette réponse surprend le groupe."); input()
print(Fore.MAGENTA + "Ethan : La confiance se mérite. Je vous propose de vous aider, et vous déciderez ensuite si j'ai ma place parmi vous."); input()

choix = int(input("Faire confiance à Ethan ?\n1 = L'accepter immédiatement.\n2 = Lui demander de prouver sa loyauté.\n"))

if choix == 1:
    print(Fore.BLUE + character.nom + " : D'accord. Tu viens avec nous."); input()
    print(Fore.MAGENTA + "Ethan : Tu ne le regretteras pas."); input()
    print(Fore.BLUE + character.nom + " : C'est exactement ce que disent les gens qu'on finit par regretter."); input()
    print(Fore.MAGENTA + "Ethan : Alors je vais devoir faire mieux que les autres."); input()
    print(Fore.WHITE + "Narrateur : Ethan rejoint officiellement le groupe."); input()

elif choix == 2:
    print(Fore.BLUE + character.nom + " : Nous ne faisons pas confiance à quelqu'un simplement parce qu'il nous raconte une histoire."); input()
    print(Fore.MAGENTA + "Ethan : C'est raisonnable. Il y a un poste de garde au nord. Je peux vous faire passer sans déclencher l'alarme."); input()
    print(Fore.BLUE + character.nom + " : Très bien. Montre-nous."); input()
    print(Fore.WHITE + "Narrateur : Ethan conduit le groupe par un passage secondaire. Il désactive un mécanisme ancien et permet au groupe d'éviter les gardes."); input()
    print(Fore.YELLOW + "Ferdinand : Je savais que nous aurions dû le recruter dès le début."); input()
    print(Fore.BLUE + character.nom + " : Tu viens de dire que tu le soupçonnais d'être un espion."); input()
    print(Fore.YELLOW + "Ferdinand : Je soupçonne tout le monde. C'est une forme de prudence."); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Non, c'est une forme de paranoïa avec des muscles."); input()
    print(Fore.WHITE + "Narrateur : Ethan rejoint le groupe après avoir prouvé son utilité."); input()

#############################################################
#                                                           #
#   Act 4 - Scène 6                                         #
#   le fragment noir                                        #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Avant de quitter la boulangerie, Nathaniel examine un dernier document."); input()
print(Fore.RED + "Nathaniel : Il y a un passage que je ne comprends pas."); input()
print(Fore.BLUE + character.nom + " : Qu'est-ce qu'il dit ?"); input()
print(Fore.RED + "Nathaniel : « Le Coeur ne choisit pas son maître. Il amplifie ce qui existe déjà en lui. »"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Nous avons déjà parlé de ça."); input()
print(Fore.RED + "Nathaniel : Oui. Mais cette phrase est suivie d'une mise en garde : « Celui qui cherche à soumettre les autres sera lui-même soumis à son désir de domination. »"); input()
print(Fore.YELLOW + "Ferdinand : Donc le Coeur peut rendre quelqu'un fou ?"); input()
print(Fore.RED + "Nathaniel : Pas exactement. Il peut rendre son ambition si puissante qu'il ne voit plus rien d'autre."); input()
print(Fore.BLUE + character.nom + " : Arnaud pourrait finir par perdre le contrôle."); input()
print(Fore.RED + "Nathaniel : Ou il pourrait croire qu'il n'a jamais été aussi raisonnable."); input()
print(Fore.WHITE + "Narrateur : Ethan regarde discrètement un fragment noir tombé de la boîte. Il le ramasse et le glisse dans sa poche."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Bon. Nous avons un tyran, un artefact dangereux et une bibliothèque pleine de gardes."); input()
print(Fore.YELLOW + "Ferdinand : Et nous sommes cinq."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Tu as compté les ennemis ?"); input()
print(Fore.YELLOW + "Ferdinand : Non."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Évidemment."); input()
print(Fore.WHITE + "Narrateur : Le groupe quitte la boulangerie. Ethan reste quelques secondes en arrière, la main dans sa poche."); input()
print(Fore.MAGENTA + "Ethan, à voix basse : À bientôt papa..."); input()

farm=2
while farm!=1:
    freetime=int(input("--------------------------\nQu'est ce que vous souhaitez faire ?\n1 = Allez battre des monstres.\n2 = Allez chez le forgeron.\n3 = Allez chez le vendeur."))
    if freetime==1:
        List_player=[character,Andy,Nath,Ethan] ; diff=2 ; stade_equipe=2
        fight()
        if randint(1,10)==1:
            character.set_maxvie() ; Andy.set_maxvie() ; Nath.set_maxvie() ; Ethan.set_maxvie() 
    elif freetime==2:
        armurerie()
    elif freetime==3:
        shop_heal()
    farm=int(input("Voulez vous continuez de profiter de votre temps libre ?\n1 = OUI\n2 = NON\n"))

#############################################################
#                                                           #
#   Act 5 - Scène 1                                         #
#   devant la bibliothèque                                 #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Lieu : La bibliothèque interdite, au coeur de la capitale."); input()
print(Fore.WHITE + "Narrateur : La nuit est tombée. Le groupe observe la bibliothèque depuis una ruelle. Le bâtiment est immense, entouré de murs et de gardes."); input()
print(Fore.LIGHTBLACK_EX + "Andy : J'ai une question."); input()
print(Fore.BLUE + character.nom + " : Laquelle ?"); input()
print(Fore.LIGHTBLACK_EX + "Andy : Pourquoi toutes les choses importantes sont-elles enfermées dans des endroits où l'on risque de mourir ?"); input()
print(Fore.YELLOW + "Ferdinand : Pour que les gens comme toi ne les touchent pas."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Je suis profondément blessé."); input()
print(Fore.RED + "Nathaniel : La bibliothèque contient les dernières archives de l'ancienne dynastie. Si nous trouvons le sceau royal, nous pourrons peut-être atteindre le sanctuaire avant Arnaud."); input()
print(Fore.BLUE + character.nom + " : Tu es certain que le sceau est là ?"); input()
print(Fore.RED + "Nathaniel : Les documents indiquent qu'il a été transféré à la capitale. Mais nous ignorons s'il s'y trouve encore."); input()
print(Fore.YELLOW + "Ferdinand : Donc nous allons peut-être risquer notre vie pour une boîte vide."); input()
print(Fore.LIGHTBLACK_EX + "Andy : Enfin, quelqu'un qui comprend la logique de nos aventures."); input()
print(Fore.MAGENTA + "Ethan : Nous n'avons pas beaucoup de temps. Les gardes déplacent régulièrement les objets sensibles. Si le sceau est encore dans la bibliothèque, il ne le restera pas longtemps."); input()
print(Fore.BLUE + character.nom + " : Alors nous devons entrer cette nuit."); input()
print(Fore.RED + "Nathaniel : Il existe plusieurs moyens."+Fore.RESET); input()

#############################################################
#                                                           #
#   Act 5 - Scène 2                                         #
#   choisir l'entrée                                        #
#                                                           #
#############################################################

choix=int(input("Comment allez vous pénétrer dans la bibliothèque ?\n1 = Passer par l'entrée principale.\n2 = Utiliser les tunnels.\n"))

if choix == 1:
    print(Fore.BLUE + character.nom + " : Nous allons entrer par devant."); input()
    print(Fore.LIGHTBLACK_EX + "Andy : J'apprécie ton optimisme. Il est totalement déraisonnable, mais je l'apprécie."); input()
    print(Fore.WHITE + "Narrateur : Le groupe s'approche des gardes."); input()
    print(Fore.CYAN + "Garde : Motif de votre visite ?"); input()
    print(Fore.BLUE + character.nom + " : Nous sommes des archivistes."); input()
    print(Fore.CYAN + "Garde : Vos autorisations ?"); input()
    print(Fore.WHITE + "Narrateur : Silence."); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Elles sont... archivées."); input()
    print(Fore.CYAN + "Garde : Vos noms ?"); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Les mêmes que sur nos autorisations."); input()
    print(Fore.CYAN + "Garde : Montrez-les."); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Elles sont très bien conservées."); input()
    print(Fore.BLUE + character.nom + " : Andy."); input()
    print(Fore.LIGHTBLACK_EX + "Andy : Je panique avec élégance."); input()
    print(Fore.WHITE + "Narrateur : Les gardes comprennent la supercherie et attaquent."); input()
    List_player=[character,Andy,Nath,Ethan] ; diff=12
    fight()

elif choix == 2:
    print(Fore.BLUE + character.nom + " : Ethan, montre-nous le passage."); input()
    print(Fore.MAGENTA + "Ethan : Suivez-moi. Et essayez de ne pas toucher aux murs."); input()
    print(Fore.YELLOW + "Ferdinand : Pourquoi ?"); input()
    print(Fore.MAGENTA + "Ethan : Parce que certains mécanismes sont encore actifs."); input()
    print(Fore.YELLOW + "Ferdinand : Je ne touche jamais aux murs."); input()
    print(Fore.WHITE + "Narrateur : Il pose immédiatement la main sur le mur."); input()
    print(Fore.BLUE + character.nom + " : Ferdinand !"); input()
    print(Fore.YELLOW + "Ferdinand : Je vérifiais s'il disait vrai."); input()
    print(Fore.WHITE + "Narrateur : Un mécanisme claque. Une grille tombe derrière le groupe."); input()
    print(Fore.MAGENTA + "Ethan : C'était un avertissement."); input()
    print(Fore.YELLOW + "Ferdinand : Il était très convaincant."); input()
    print(Fore.WHITE + "Narrateur : Le groupe progresse dans les tunnels, évite plusieurs pièges et atteint une porte de service."); input()
    print(Fore.WHITE + "Narrateur : Résultat : le groupe entre discrètement et économise des ressources, mais doit traverser un passage piégé."); input()


#############################################################
#                                                           #
#   Act 5 - Scène 3                                         #
#   les archives de l'ancienne dynastie                     #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Le groupe pénètre dans la bibliothèque. Des rayonnages gigantesques s'élèvent jusqu'au plafond. Une odeur de poussière et de vieux papier flotte dans l'air.")
print(Fore.RED + "Nathaniel : Nous devons trouver le registre de la dernière année du règne royal.")
print(Fore.YELLOW + "Ferdinand : Il ressemble à quoi ?")
print(Fore.RED + "Nathaniel : Un livre.")
print(Fore.YELLOW + "Ferdinand : Très utile.")
print(Fore.LIGHTBLACK_EX + "Andy : Il faut reconnaître que les bibliothèques sont conçues avec un manque d'imagination flagrant. Des livres partout, et pas une seule pancarte indiquant où se trouve le livre que tu cherches.")
print(Fore.BLUE + character.nom + " : C'est une bibliothèque, pas une auberge.")
print(Fore.LIGHTBLACK_EX + "Andy : Justement. Une auberge possède au moins un tavernier qui peut te dire où se trouve la bière.")
print(Fore.WHITE + "Narrateur : Nathaniel se dirige vers une section interdite. Il examine plusieurs registres avant d'en retirer un volume épais.")
print(Fore.RED + "Nathaniel : Je l'ai trouvé.")
print(Fore.BLUE + character.nom + " : Qu'est-ce qu'il dit ?")
print(Fore.WHITE + "Narrateur : Nathaniel tourne les pages avec précaution.")
print(Fore.RED + "Nathaniel : Les registres officiels affirment que le roi a trahi son peuple et provoqué la guerre civile. Mais les dates ont été falsifiées. Certaines signatures ont été copiées.")
print(Fore.MAGENTA + "Ethan : Continue.")
print(Fore.RED + "Nathaniel : Voici un document qui mentionne le conseiller Arnaud. Il avait accès aux archives, aux armureries et aux ordres militaires.")
print(Fore.BLUE + character.nom + " : Il avait donc les moyens d'organiser la révolte.")
print(Fore.RED + "Nathaniel : Oui. Et regarde cette note. Le roi avait demandé le transfert du Coeur de Bedrock vers le sanctuaire sous le château. Il craignait qu'un conseiller ne s'en empare.")
print(Fore.YELLOW + "Ferdinand : Arnaud.")
print(Fore.RED + "Nathaniel : Tout porte à le croire.")
print(Fore.LIGHTBLACK_EX + "Andy : Résumons. Un conseiller est chargé de protéger son roi, trahit la famille royale, prend le pouvoir et réécrit les livres d'histoire. Puis il part à la recherche de l'artefact qu'il était censé protéger.")
print(Fore.BLUE + character.nom + " : C'est bien ça.")
print(Fore.LIGHTBLACK_EX + "Andy : Je crois que j'ai trouvé le sujet de mon prochain album.")
print(Fore.RED + "Nathaniel : Tu pourrais peut-être attendre la fin de notre aventure.")
print(Fore.LIGHTBLACK_EX + "Andy : Et perdre l'occasion d'écrire un album intitulé Le Conseiller qui avait besoin de vacances ?")
print(Fore.YELLOW + "Ferdinand : Je l'achèterais.")
print(Fore.LIGHTBLACK_EX + "Andy : Enfin un homme de culture.")

#############################################################
#                                                           #
#   Act 5 - Scène 4                                         #
#   le sceau royal                                          #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Nathaniel trouve un second document, plus ancien que les autres.")
print(Fore.RED + "Nathaniel : Le Coeur de Bedrock ne pouvait pas être activé seul. Il fallait le sceau royal.")
print(Fore.BLUE + character.nom + " : Et où est-il ?")
print(Fore.RED + "Nathaniel : Le document indique qu'il a été conservé dans cette bibliothèque pendant plusieurs années.")
print(Fore.MAGENTA + "Ethan : Ce qui signifie qu'Arnaud l'a probablement récupéré.")
print(Fore.BLUE + character.nom + " : Tu sembles très sûr de toi.")
print(Fore.MAGENTA + "Ethan : J'ai vu ses hommes transporter un objet portant le sceau royal il y a plusieurs jours.")
print(Fore.RED + "Nathaniel : Pourquoi ne nous l'as-tu pas dit plus tôt ?")
print(Fore.MAGENTA + "Ethan : Parce que je voulais être certain.")
print(Fore.LIGHTBLACK_EX + "Andy : Et maintenant, tu es certain ?")
print(Fore.MAGENTA + "Ethan : Oui.")
print(Fore.LIGHTBLACK_EX + "Andy : Je pose la question parce que je préfère découvrir les mauvaises nouvelles avant qu'elles nous tombent dessus.")
print(Fore.YELLOW + "Ferdinand : Moi, je préfère les découvrir quand je peux frapper quelqu'un.")
print(Fore.RED + "Nathaniel : Le sceau permettrait à Arnaud de réveiller le Coeur. S'il l'a déjà, nous devons agir rapidement.")
print(Fore.BLUE + character.nom + " : Alors nous allons au château.")
print(Fore.RED + "Nathaniel : Ce ne sera pas simple. Le château est entouré de soldats et le sanctuaire se trouve sous la salle du trône.")
print(Fore.MAGENTA + "Ethan : Je connais un passage qui mène aux quartiers intérieurs.")
print(Fore.BLUE + character.nom + " : Tu connais toujours un passage secret.")
print(Fore.MAGENTA + "Ethan : C'est un talent utile.")
print(Fore.LIGHTBLACK_EX + "Andy : Moi, je connais une chanson qui peut faire pleurer un homme adulte.")
print(Fore.BLUE + character.nom + " : Ce n'est pas vraiment comparable.")
print(Fore.LIGHTBLACK_EX + "Andy : Tu n'as jamais entendu le deuxième couplet.")

#############################################################
#                                                           #
#   Act 5 - Scène 5                                         #
#   déclenchement de l'alarme                               #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Un bruit de pas résonne dans le couloir.")
print(Fore.CYAN + "Garde, *au loin* : Ils sont dans la bibliothèque ! Fouillez toutes les salles !")
print(Fore.BLUE + character.nom + " : On doit partir !")
print(Fore.YELLOW + "Ferdinand : Enfin !")
print(Fore.RED + "Nathaniel : Prenez les documents importants. Nous ne pouvons pas les laisser derrière nous.")
print(Fore.WHITE + "Narrateur : Le groupe se dirige vers une porte secondaire. Ethan la maintient ouverte pendant que les autres passent.")
print(Fore.LIGHTBLACK_EX + "Andy : Je voudrais signaler que je déteste les bibliothèques.")
print(Fore.RED + "Nathaniel : Tu disais pourtant aimer les livres.")
print(Fore.LIGHTBLACK_EX + "Andy : J'aime les livres qui ne sont pas protégés par des hommes armés.")
print(Fore.WHITE + "Narrateur : Ils traversent une petite salle de lecture et barricadent la porte."+ Fore.RESET)

choix=int(input("Que faire des documents ?\n1 = Les emporter tous.\n2 = Ne prendre que le plan du sanctuaire.\n3 = Détruire les documents compromettants\n"))

if choix == 1:
    print(Fore.BLUE + character.nom + " : Nous ne laissons aucune preuve derrière nous.")
    print(Fore.RED + "Nathaniel : Très bien. Mais cela nous ralentira.")
    print(Fore.WHITE + "Narrateur : Le groupe conserve toutes les archives. Plus tard, elles permettront de découvrir une entrée secrète du château et d'obtenir davantage d'informations sur Arnaud.")

elif choix == 2:
    print(Fore.BLUE + character.nom + " : Nous n'avons pas le temps. Prenons le plan.")
    print(Fore.RED + "Nathaniel : C'est risqué, mais efficace.")
    print(Fore.WHITE + "Narrateur : Le groupe s'enfuit rapidement.")

elif choix == 3:
    print(Fore.BLUE + character.nom + " : Si Arnaud les récupère, il pourra effacer toutes les traces.")
    print(Fore.RED + "Nathaniel : Nous devons préserver la vérité, pas la faire disparaître à notre tour.")
    print(Fore.BLUE + character.nom + " : Et si ces documents permettent à Arnaud de nous retrouver ?")
    print(Fore.RED + "Nathaniel : Alors nous trouverons un moyen de les protéger.")

if pre_req_EvilEnding==1:
    if choix==1 or choix==3:
        req_EvilEnding=int(input(Fore.RESET + "Souhaitez vous revenir sur votre décision ?\n1 = OUI\n2 = NON\n"))
        if choix==1:
            print(Fore.BLUE + character.nom + " : Vous êtes vraiment sûr qu'on ne devrait pas les détruire ? Elles pourraient vraiment nous attirer des problèmes")
            print(Fore.RED + "Nathaniel : Oui, il faut impérativement que la vérité ne soit surtout pas détruite.")
            print(Fore.LIGHTBLACK_EX + "Andy : fait comment bon te semble. Honnêtement tu peux en faire ce que tu veux ça ne changera pas ma musique.")
            print(Fore.YELLOW + "Ferdinand : Ça pourrait faire du bon combustible pour la cheminer de l'auberge.")
            print(Fore.MAGENTA + "Ethan : Moi je suis pour nous en débarrassez.")
            print(Fore.WHITE + "Narrateur : " + character.nom + " n'a donc pas écoutez Nathaniel et à donc détruit les documents")
        if choix==2:
            print(Fore.WHITE + "Narrateur : " + character.nom + " décide de ne pas s'en débarraser et les donnes à Nathaniel.")


#############################################################
#                                                           #
#   Act 5 - Scène 6                                         #
#   la dernière veille                                      #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Le groupe finit par sortir de la bibliothèque et rejoint une ruelle silencieuse. Ils se cachent dans un entrepôt abandonné.")
print(Fore.YELLOW + "Ferdinand : Je déteste me cacher.")
print(Fore.LIGHTBLACK_EX + "Andy : Tu préfères te faire arrêter ?")
print(Fore.YELLOW + "Ferdinand : Non.")
print(Fore.LIGHTBLACK_EX + "Andy : Voilà. Tu progresses.")
print(Fore.YELLOW + "Ferdinand : Tu sais, pour quelqu'un qui parle autant, tu es parfois très agaçant.")
print(Fore.LIGHTBLACK_EX + "Andy : C'est mon charme.")
print(Fore.BLUE + character.nom + " : C'est surtout ton volume sonore.")
print(Fore.WHITE + "Narrateur : Nathaniel étale les documents sur une caisse.")
print(Fore.RED + "Nathaniel : Nous savons maintenant où se trouve le sanctuaire. Sous le château d'Arnaud.")
print(Fore.BLUE + character.nom + " : Et le Coeur est probablement là-bas.")
print(Fore.RED + "Nathaniel : Oui. Mais il nous manque une information essentielle : comment neutraliser l'artefact.")
print(Fore.MAGENTA + "Ethan : Nous n'avons pas besoin de le neutraliser. Nous devons empêcher Arnaud de l'utiliser.")
print(Fore.RED + "Nathaniel : Et si nous échouons ?")
print(Fore.MAGENTA + "Ethan : Alors nous le détruirons.")
print(Fore.RED + "Nathaniel : Tu sais ce que cela pourrait provoquer ?")
print(Fore.MAGENTA + "Ethan : Mieux vaut détruire un pouvoir dangereux que de le laisser entre les mains d'un tyran.")
print(Fore.WHITE + "Narrateur : Ethan parle avec une intensité inhabituelle. " + character.nom + " le remarque.")
print(Fore.BLUE + character.nom + " : Tu as vraiment envie qu'Arnaud tombe.")
print(Fore.MAGENTA + "Ethan : Tu n'as aucune idée de ce qu'il m'a pris.")
print(Fore.BLUE + character.nom + " : Alors aide-nous à l'arrêter.")
print(Fore.MAGENTA + "Ethan : C'est précisément ce que je compte faire.")
print(Fore.WHITE + "Narrateur : Un silence s'installe. Nathaniel rassemble les documents.")
print(Fore.RED + "Nathaniel : Nous devons nous préparer. Demain, nous entrerons dans le château.")
print(Fore.LIGHTBLACK_EX + "Andy : Très bien. Je propose que nous dormions, que nous mangions et que nous évitions de parler de notre mort imminente.")
print(Fore.YELLOW + "Ferdinand : Je peux monter la garde.")
print(Fore.BLUE + character.nom + " : Tu devrais dormir aussi.")
print(Fore.YELLOW + "Ferdinand : Je ne suis pas fatigué.")
print(Fore.WHITE + "Narrateur : Il bâille.")
print(Fore.LIGHTBLACK_EX + "Andy : Impressionnant. Même ton corps ne croit pas à tes mensonges.")
print(Fore.WHITE + "Narrateur : Le groupe se prépare pour la dernière étape de son voyage. Dans un coin sombre, Ethan sort discrètement le fragment noir qu'il avait récupéré dans la boulangerie.")
print(Fore.MAGENTA + "Ethan, *à voix basse* : Encore un peu de patience."+ Fore.RESET)

farm=2
while farm!=1:
    freetime=int(input("--------------------------\nQu'est ce que vous souhaitez faire ?\n1 = Allez battre des monstres.\n2 = Allez chez le forgeron.\n3 = Allez chez le vendeur."))
    if freetime==1:
        List_player=[character,Andy,Nath,Ethan] ; diff=2 ; stade_equipe=2
        fight()
        if randint(1,10)==1:
            character.set_maxvie() ; Andy.set_maxvie() ; Nath.set_maxvie() ; Ethan.set_maxvie()
    elif freetime==2:
        armurerie()
    elif freetime==3:
        shop_heal()
    farm=int(input("Voulez vous continuez de profiter de votre temps libre ?\n1 = OUI\n2 = NON\n"))

#############################################################
#                                                           #
#   Act 6 - Scène 1                                         #
#   devant le chateau                                       #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Lieu : Le château de Monsieur Arnaud.")
print(Fore.WHITE + "Narrateur : Le ciel est sombre. Le groupe arrive devant les portes du château. Des gardes patrouillent sur les remparts. Une cloche annonce le changement de garde.")
print(Fore.BLUE + character.nom + " : C'est ici que tout se termine.")
print(Fore.LIGHTBLACK_EX + "Andy : Je préférerais que tout se termine dans une auberge, avec un repas chaud et un public qui m'applaudit.")
print(Fore.YELLOW + "Ferdinand : Après avoir battu Arnaud, tu pourras chanter autant que tu veux.")
print(Fore.LIGHTBLACK_EX + "Andy : Je vais prendre ça pour une promesse.")
print(Fore.RED + "Nathaniel : Restons concentrés. Le sanctuaire se trouve sous la salle du trône. Si nous atteignons le Coeur avant Arnaud, nous pourrons peut-être empêcher son activation.")
print(Fore.BLUE + character.nom + " : Et si nous arrivons trop tard ?")
print(Fore.RED + "Nathaniel : Alors nous devrons l'affronter avec le pouvoir du Coeur à sa disposition.")
print(Fore.YELLOW + "Ferdinand : J'aime mieux le premier plan.")
print(Fore.LIGHTBLACK_EX + "Andy : Pour une fois, nous sommes tous d'accord.")
print(Fore.WHITE + "Narrateur : Ethan observe les remparts.")
print(Fore.MAGENTA + "Ethan : Je connais un passage qui mène aux quartiers intérieurs. Il passe derrière l'ancienne salle des archives.")
print(Fore.BLUE + character.nom + " : Comment peux-tu connaître autant de passages dans ce château ?")
print(Fore.MAGENTA + "Ethan : Mon père travaillait pour la cour royale. Il m'a appris à reconnaître les endroits où les puissants cachent leurs secrets.")
print(Fore.RED + "Nathaniel : Nous devons rester prudents. Les gardes peuvent avoir modifié les accès.")
print(Fore.MAGENTA + "Ethan : Faites-moi confiance.")
print(Fore.WHITE + "Narrateur : Un court silence.")
print(Fore.LIGHTBLACK_EX + "Andy : C'est exactement la phrase que je voulais entendre juste avant d'entrer dans un château rempli de gardes.")
print(Fore.BLUE + character.nom + " : Tu as une meilleure idée ?")
print(Fore.LIGHTBLACK_EX + "Andy : Oui. Une porte ouverte, aucun garde et un buffet.")
print(Fore.YELLOW + "Ferdinand : On peut garder le buffet pour après.")
print(Fore.WHITE + "Narrateur : Le groupe emprunte un passage étroit derrière une vieille tour.")

#############################################################
#                                                           #
#   Act 6 - Scène 3                                         #
#   les portraits effacés                                   #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Le groupe traverse un couloir couvert de portraits. Plusieurs tableaux ont été lacérés, et certains visages ont été complètement effacés.")
print(Fore.RED + "Nathaniel : Regardez ces tableaux. Ils représentent les derniers membres de l'ancienne dynastie.")
print(Fore.BLUE + character.nom + " : Pourquoi leurs visages ont-ils été détruits ?")
print(Fore.RED + "Nathaniel : Pour effacer leur mémoire. Arnaud ne veut pas que les habitants puissent comparer son règne à celui des anciens souverains.")
print(Fore.YELLOW + "Ferdinand : Il a peur d'un tableau ?")
print(Fore.RED + "Nathaniel : Il a peur de ce que le tableau représente.")
print(Fore.LIGHTBLACK_EX + "Andy : C'est une différence importante. Moi, j'ai surtout peur des tableaux qui me représentent. Les peintres ont parfois une vision très personnelle de la réalité.")
print(Fore.WHITE + "Narrateur : " + character.nom + " s'arrête devant un portrait dont le visage est encore visible. Un roi tient un sceau gravé du symbole royal.")
print(Fore.BLUE + character.nom + " : C'est le sceau.")
print(Fore.RED + "Nathaniel : Oui. Le même symbole apparaît sur les documents de la boulangerie.")
print(Fore.MAGENTA + "Ethan : Nous sommes proches du sanctuaire.")
print(Fore.WHITE + "Narrateur : Ethan semble tendu. Il regarde alternativement le couloir et le sol.")
print(Fore.BLUE + character.nom + " : Tout va bien ?")
print(Fore.MAGENTA + "Ethan : Oui.")
print(Fore.BLUE + character.nom + " : Tu es sûr ?")
print(Fore.MAGENTA + "Ethan : Je suis simplement impatient d'en finir.")
print(Fore.LIGHTBLACK_EX + "Andy : C'est drôle. Moi, quand je suis impatient, je parle encore plus. Et je parle déjà beaucoup.")
print(Fore.MAGENTA + "Ethan : Tu devrais écrire une chanson sur le silence.")
print(Fore.LIGHTBLACK_EX + "Andy : J'y ai pensé. Mais j'ai peur que le public ne m'entende pas.")
print(Fore.WHITE + "Narrateur : Le groupe continue d'avancer.")


#############################################################
#                                                           #
#   Act 6 - Scène 3                                         #
#   la trahison d'éthan                                     #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Ethan s'arrête devant une porte massive.")
print(Fore.MAGENTA + "Ethan : Nous y sommes.")
print(Fore.YELLOW + "Ferdinand : Alors ouvrons.")
print(Fore.MAGENTA + "Ethan : Attendez. Il y a quelque chose que je dois vous dire.")
print(Fore.WHITE + "Narrateur : Le groupe se retourne vers lui.")
print(Fore.BLUE + character.nom + " : Quoi ?")
print(Fore.WHITE + "Narrateur : Ethan baisse la tête. Lorsqu'il relève les yeux, son expression a changé.")
print(Fore.MAGENTA + "Ethan : Je vous ai menti depuis le début.")
print(Fore.LIGHTBLACK_EX + "Andy : ... Je savais que tu étais mystérieux, mais je pensais que c'était juste une mauvaise habitude.")
print(Fore.RED + "Nathaniel : Ethan. Que signifie tout cela ?")
print(Fore.MAGENTA + "Ethan : Je n'ai jamais voulu simplement faire tomber Arnaud. Je voulais prendre sa place.")
print(Fore.WHITE + "Narrateur : Le silence devient pesant.")
print(Fore.BLUE + character.nom + " : Tu es sérieux ?")
print(Fore.MAGENTA + "Ethan : Toute ma vie, j'ai vu les puissants décider du sort des autres. Mon père a été détruit parce qu'il s'est opposé à Arnaud. J'ai passé des années à chercher un moyen de ne plus jamais être impuissant.")
print(Fore.RED + "Nathaniel : Tu veux utiliser le Coeur Bedrock.")
print(Fore.MAGENTA + "Ethan : Exactement.")
print(Fore.BLUE + character.nom + " : Tu sais ce que cet artefact peut faire !")
print(Fore.MAGENTA + "Ethan : Je sais qu'il peut me donner le pouvoir de changer le royaume.")
print(Fore.RED + "Nathaniel : Il ne changera pas le royaume. Il te changera, toi.")
print(Fore.MAGENTA + "Ethan : Peut-être. Mais je préfère risquer de devenir un monstre plutôt que de rester un homme que personne ne peut entendre.")
print(Fore.BLUE + character.nom + " : Nous t'avons fait confiance.")
print(Fore.MAGENTA + "Ethan : Et vous m'avez été utiles. Vous avez trouvé les archives, révélé le sanctuaire et éliminé plusieurs obstacles. Sans vous, je n'aurais jamais pu arriver jusqu'ici.")
print(Fore.LIGHTBLACK_EX + "Andy : Tu nous as utilisés.")
print(Fore.MAGENTA + "Ethan : Oui.")
print(Fore.YELLOW + "Ferdinand : Je vais lui faire ravaler ses paroles.")
print(Fore.RED + "Nathaniel : Ferdinand, attends.")
print(Fore.YELLOW + "Ferdinand : Quoi ? Tu veux lui offrir un livre ?")
print(Fore.RED + "Nathaniel : Je veux comprendre jusqu'où il est allé.")
print(Fore.WHITE + "Narrateur : Ethan sort le fragment noir de sa poche.")
print(Fore.MAGENTA + "Ethan : Ce fragment provient du Coeur. Il m'a permis de sentir sa présence et de suivre les indices qui menaient jusqu'ici.")
print(Fore.BLUE + character.nom + " : Tu l'avais depuis la boulangerie ?")
print(Fore.MAGENTA + "Ethan : Oui.")
print(Fore.BLUE + character.nom + " : Et tu nous as laissé chercher l'artefact en sachant que tu voulais le prendre pour toi ?")
print(Fore.MAGENTA + "Ethan : Je savais que vous pouviez trouver les documents. Je savais que Nathaniel comprendrait les archives. Et je savais que vous finirez par atteindre le château.")
print(Fore.LIGHTBLACK_EX + "Andy : Tu as donc planifié tout ça.")
print(Fore.MAGENTA + "Ethan : Chaque étape.")
print(Fore.LIGHTBLACK_EX + "Andy : Je déteste reconnaître le talent chez mes ennemis.")
print(Fore.MAGENTA + "Ethan : Je vous ai donné une chance de vous retirer.")
print(Fore.BLUE + character.nom + " : Tu ne nous as jamais dit la vérité !")
print(Fore.MAGENTA + "Ethan : Parce que vous m'auriez arrêté.")
print(Fore.RED + "Nathaniel : Bien sûr que nous t'aurions arrêté.")
print(Fore.MAGENTA + "Ethan : Voilà pourquoi je ne vous ai rien dit.")
print(Fore.WHITE + "Narrateur : Ethan frappe le sol avec le fragment noir. Un mécanisme s'active. Des grilles tombent et séparent le groupe.")
print(Fore.BLUE + character.nom + " : ETHAN !")
print(Fore.MAGENTA + "Ethan : Je suis désolé, " + character.nom + ". Mais je ne peux pas laisser quelqu'un d'autre décider de mon avenir.")
print(Fore.WHITE + "Narrateur : Une porte s'ouvre derrière lui. Il disparaît dans le sanctuaire.")

#############################################################
#                                                           #
#   Act 6 - Scène 3                                         #
#   le choix du mc                                          #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Le groupe se retrouve enfermé dans le couloir. Ferdinand frappe la grille de ses deux mains.")
print(Fore.YELLOW + "Ferdinand : Je vais ouvrir cette porte.")
print(Fore.RED + "Nathaniel : Attends. Il doit y avoir un mécanisme.")
print(Fore.YELLOW + "Ferdinand : Je suis le mécanisme.")
print(Fore.WHITE + "Narrateur : Il frappe la grille. Elle tremble, mais ne s'ouvre pas.")
print(Fore.LIGHTBLACK_EX + "Andy : Impressionnant. La grille est toujours là, mais elle a probablement peur.")
print(Fore.BLUE + character.nom + " : Arrêtez tous les deux !")
print(Fore.WHITE + "Narrateur : Le " + character.nom + " observe le mécanisme et cherche une commande. Nathaniel l'aide à comprendre les symboles gravés sur le mur. Après quelques instants, la grille se soulève.")
print(Fore.YELLOW + "Ferdinand : Tu vois ? J'avais presque réussi.")
print(Fore.BLUE + character.nom + " : Tu étais en train de te faire mal aux mains.")
print(Fore.YELLOW + "Ferdinand : C'était une stratégie.")
print(Fore.LIGHTBLACK_EX + "Andy : La stratégie du poing douloureux.")
print(Fore.WHITE + "Narrateur : Le groupe rejoint un escalier qui descend vers le sanctuaire.") 

choix=int(input(Fore.RESET + "Comment réagit le character.nom à la trahison ?\n1 = « Je te ferai payer ce que tu as fait. »\n2 = « Il est encore temps de renoncer. »\n3 = « Tu n'as jamais été notre ami. »\n")) 

if choix == 1:
    print(Fore.BLUE + character.nom + " : Tu as trahi des gens qui te faisaient confiance. Je ne te laisserai pas utiliser cet artefact.")
    print(Fore.LIGHTBLACK_EX + "Andy : Je suis avec toi. Et je tiens à préciser que je n'ai jamais aimé ses chaussures.")
    print(Fore.BLUE + character.nom + " : Ses chaussures ?")
    print(Fore.LIGHTBLACK_EX + "Andy : Je cherche encore une raison logique de lui en vouloir.")
    print(Fore.YELLOW + "Ferdinand : Moi, j'en ai une. Il nous a trahis.")
    print(Fore.RED + "Nathaniel : Alors nous devons l'arrêter avant qu'il ne soit trop tard.")
    print(Fore.WHITE + "Narrateur : Le groupe poursuit Ethan, déterminé à le vaincre.")

elif choix == 2:
    print(Fore.BLUE + character.nom + " : Ethan, tu peux encore faire marche arrière. Ne deviens pas ce que tu détestes.")
    print(Fore.MAGENTA + "Ethan, au loin : Tu ne comprends pas. Je ne veux plus revenir en arrière.")
    print(Fore.BLUE + character.nom + " : Je sais que tu as souffert. Mais ce que tu as vécu ne te donne pas le droit de décider de la vie de tous les autres.")
    print(Fore.WHITE + "Narrateur : Un silence suit.")
    print(Fore.MAGENTA + "Ethan : Tu parles comme mon père.")
    print(Fore.WHITE + "Narrateur : Ethan disparaît dans le sanctuaire. Nathaniel remarque qu'il a hésité.")
    print(Fore.RED + "Nathaniel : Il n'est peut-être pas entièrement perdu.")
    Req_TrueEnding=1

elif choix == 3:
    print(Fore.BLUE + character.nom + " : Tout ce que tu nous as raconté n'était qu'un mensonge.")
    print(Fore.MAGENTA + "Ethan : Certaines choses étaient vraies. C'est ce qui rend les mensonges efficaces.")
    print(Fore.LIGHTBLACK_EX + "Andy : Je vais devoir reconnaître que cette phrase est très bonne. Et ça m'énerve.")
    print(Fore.YELLOW + "Ferdinand : Moi, je n'ai pas besoin d'une bonne phrase pour le frapper.")
    print(Fore.RED + "Nathaniel : Nous devons rester concentrés. La colère ne nous aidera pas à gagner.")
    print(Fore.WHITE + "Narrateur : Le groupe poursuit Ethan, mais la confiance entre les personnages est profondément ébranlée.")

#############################################################
#                                                           #
#   Act 6 - Scène 3                                         #
#   salle du trone                                          #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Le groupe arrive devant une immense salle. Des bannières noires pendent au plafond. Au fond, Monsieur Arnaud se tient devant les portes du sanctuaire.")
print(Fore.GREEN + "Monsieur Arnaud : Vous voilà enfin.")
print(Fore.BLUE + character.nom + " : C'est terminé, Arnaud.")
print(Fore.GREEN + "Monsieur Arnaud : Terminé ? Vous avez traversé mon royaume, détruit mes postes de garde et pillé mes archives. Et vous pensez pouvoir m'arrêter avec quelques discours ?")
print(Fore.LIGHTBLACK_EX + "Andy : Je peux aussi faire des chansons. Elles sont particulièrement désagréables.")
print(Fore.GREEN + "Monsieur Arnaud : Le musicien. Toujours aussi bruyant.")
print(Fore.LIGHTBLACK_EX + "Andy : Et vous, toujours aussi laid dans vos choix politiques.")
print(Fore.YELLOW + "Ferdinand : Andy, concentre-toi !")
print(Fore.LIGHTBLACK_EX + "Andy : Je me concentre. Je peux être sarcastique et attentif en même temps.")
print(Fore.GREEN + "Monsieur Arnaud : Vous ne comprenez rien. Les gens sont faibles. Ils se battent, se trahissent et détruisent tout ce qu'ils touchent. J'ai apporté l'ordre à ce royaume.")
print(Fore.RED + "Nathaniel : Vous avez apporté la peur.")
print(Fore.GREEN + "Monsieur Arnaud : La peur est le prix de la paix.")
print(Fore.BLUE + character.nom + " : Non. La paix n'a aucune valeur si personne n'est libre.")
print(Fore.WHITE + "Narrateur : Arnaud descend lentement les marches du trône.")
print(Fore.GREEN + "Monsieur Arnaud : La liberté est un mot que les gens utilisent quand ils ne veulent pas assumer les conséquences de leurs décisions. Regardez votre groupe. Un musicien qui provoque les autorités, un combattant qui casse tout ce qu'il touche, un prêtre qui préfère les livres aux réalités et un voyageur qui se prend pour un héros.")
print(Fore.YELLOW + "Ferdinand : Je ne casse pas tout ce que je touche.")
print(Fore.LIGHTBLACK_EX + "Andy : Tu as cassé une épée, trois paniers et une grille depuis que je te connais.")
print(Fore.YELLOW + "Ferdinand : La grille était solide.")
print(Fore.GREEN + "Monsieur Arnaud : Vous voyez ? Ils ne savent même pas s'entendre entre eux. Et vous prétendez être capables de gouverner un royaume ?")
print(Fore.BLUE + character.nom + " : Nous ne voulons pas gouverner le royaume.")
print(Fore.RED + "Nathaniel : Nous voulons qu'il puisse choisir son avenir.")
print(Fore.GREEN + "Monsieur Arnaud : Alors vous êtes plus naïfs que je ne le pensais.")
print(Fore.WHITE + "Narrateur : Arnaud ouvre les portes du sanctuaire. Une lueur noire se répand dans la salle.")

#############################################################
#                                                           #
#   Act 6 - Scène 3                                         #
#   le coeur de bedrock                                     #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Au centre de la salle souterraine, le Coeur de Bedrock flotte au-dessus d'un socle. Le sceau royal repose devant lui. Ethan se tient à ses côtés.")
print(Fore.MAGENTA + "Ethan : Nous y sommes.")
print(Fore.GREEN + "Monsieur Arnaud : Tu as accompli ta tâche, Ethan. Maintenant, écarte-toi.")
print(Fore.MAGENTA + "Ethan : Non.")
print(Fore.WHITE + "Narrateur : Arnaud se tourne lentement vers lui.")
print(Fore.GREEN + "Monsieur Arnaud : Pardon ?")
print(Fore.MAGENTA + "Ethan : Vous avez utilisé mon père, détruit sa réputation et m'avez laissé grandir dans un monde où votre parole valait plus que la vérité. Je ne vous servirai pas.")
print(Fore.GREEN + "Monsieur Arnaud : Tu crois pouvoir me remplacer ?")
print(Fore.MAGENTA + "Ethan : Je sais que je le peux.")
print(Fore.GREEN + "Monsieur Arnaud : Tu es un enfant qui joue avec des forces qu'il ne comprend pas.")
print(Fore.MAGENTA + "Ethan : Et vous êtes un vieil homme qui croit encore que tout lui appartient.")
print(Fore.WHITE + "Narrateur : Ethan s'empare du Coeur de Bedrock.")
print(Fore.RED + "Nathaniel : Ethan, lâche cet artefact !")
print(Fore.MAGENTA + "Ethan : Il est trop tard.")
print(Fore.WHITE + "Narrateur : Une lueur noire traverse la salle. Les pierres vibrent et les flammes vacillent.")
print(Fore.GREEN + "Monsieur Arnaud : Idiot ! Tu ne sais pas ce que tu réveilles !")
print(Fore.MAGENTA + "Ethan : Je sais exactement ce que je fais.")
print(Fore.BLUE + character.nom + " : Tu ne sais même pas si tu pourras contrôler ce pouvoir !")
print(Fore.MAGENTA + "Ethan : Je n'ai pas besoin de le contrôler parfaitement. J'ai seulement besoin qu'il soit de mon côté.")
print(Fore.RED + "Nathaniel : Le Coeur n'est jamais du côté de personne. Il amplifie les désirs de son porteur jusqu'à ce qu'ils deviennent impossibles à ignorer.")
print(Fore.MAGENTA + "Ethan : Alors il amplifiera mon désir de justice.")
print(Fore.BLUE + character.nom + " : Ce n'est pas de la justice que tu cherches. Tu veux être certain que personne ne puisse jamais te faire de mal.")
print(Fore.WHITE + "Narrateur : Ethan serre le Coeur contre lui.")
print(Fore.MAGENTA + "Ethan : Tu ne sais rien de ce que j'ai vécu.")
print(Fore.BLUE + character.nom + " : Peut-être. Mais je sais ce que tu es en train de faire.")
print(Fore.WHITE + "Narrateur : Arnaud saisit son arme.")
print(Fore.GREEN + "Monsieur Arnaud : Si je ne peux pas régner sur ce royaume, personne ne le fera !")
print(Fore.BLUE + character.nom + " : Alors nous allons vous arrêter tous les deux.")


#############################################################
#                                                           #
#   Act 6 - Scène 3                                         #
#   combat final                                            #
#                                                           #
#############################################################

print(Fore.WHITE + "Narrateur : Arnaud attaque le premier. Il utilise des techniques précises")
print(Fore.GREEN + "Monsieur Arnaud : Vous avez confondu mon calme avec de la faiblesse !")
print(Fore.YELLOW + "Ferdinand : Et vous avez confondu votre couronne avec un cerveau !")
print(Fore.LIGHTBLACK_EX + "Andy : C'était presque une bonne phrase, Ferdinand !")
print(Fore.YELLOW + "Ferdinand : Je peux la refaire !")
print(Fore.BLUE + character.nom + " : Pas maintenant !")
print(Fore.WHITE + "Narrateur : Le combat commence.")

List_player=[character,Andy,Nath]; stade_equipe=1
character.set_maxvie() ; Andy.set_maxvie() ; Nath.set_maxvie()
boss_fight(IsArnaudDead=0)


print(Fore.WHITE + "Narrateur : Après un long combat, Arnaud finit par tomber à genoux. Son arme glisse sur le sol.")
print(Fore.GREEN + "Monsieur Arnaud : Impossible... Vous n'êtes que des voyageurs.")
print(Fore.BLUE + character.nom + " : Et vous n'êtes qu'un homme.")
print(Fore.GREEN + "Monsieur Arnaud : Ethan ! Fais ce que tu as à faire !")
print(Fore.MAGENTA + "Ethan : Avec plaisir.")

#############################################################
#                                                           #
#   Act 6 - Scène 8                                         #
#   ethan et le coeur de bedrock                            #
#                                                           #
#############################################################

# deuxieme combat / contre éthan 

print(Fore.WHITE + "Narrateur : Ethan s'avance. Ses attaques deviennent plus rapides et plus puissantes.")
print(Fore.MAGENTA + "Ethan : Je vous avais dit de ne pas me suivre.")
print(Fore.BLUE + character.nom + " : Nous ne t'abandonnerons pas au pouvoir de cet artefact !")
print(Fore.MAGENTA + "Ethan : Je n'ai pas besoin d'être sauvé !")
print(Fore.RED + "Nathaniel : Tu n'as pas besoin de tout contrôler pour avoir de la valeur !")
print(Fore.MAGENTA + "Ethan : Tais-toi !")
print(Fore.WHITE + "Narrateur : Ethan lance une attaque puissante. Le groupe est repoussé.")
print(Fore.LIGHTBLACK_EX + "Andy : Bon. Je retire tout ce que j'ai dit sur les petites aventures tranquilles.")
print(Fore.YELLOW + "Ferdinand : On ne peut pas abandonner maintenant !")
print(Fore.BLUE + character.nom + " : Ensemble !")

character.set_maxvie() ; Andy.set_maxvie() ; Nath.set_maxvie()
boss_fight(IsArnaudDead=1)

#############################################################
#                                                           #
#   Act 6 - Scène 9                                         #
#   the last choice                                         #
#                                                           #
#############################################################

print(Fore.RESET + "Que ferai vous du coeur de Bedrock ?")
Print("1 : Détuitre le Coeur de Bedrock.")
if Req_TrueEnding==1:
    print("2 : Convaincre Ethan de lâcher le Coeur")
if req_EvilEnding==1:
    print("3 : Utiliser le Coeur pour prendre le pouvoir")

ending=int(input(""))

########################################
#                                      #
#   Good ending                        #
#                                      #
########################################

if ending == 1:
    print(character.nom + " : Aucun de nous ne devrait posséder ce pouvoir.")
    print("Nathaniel : Si tu le détruis, le royaume sera libéré de son influence. Mais personne ne sait quelles autres conséquences cela entraînera.")
    print("Ethan : Non ! C'est la seule chose qui pouvait me donner le pouvoir de changer les choses !")
    print(character.nom + " : Tu pouvais changer les choses sans contrôler les autres.")
    print("Ethan : Tu ne comprends pas !")
    print(character.nom + " : Alors explique-moi. Mais pas avec un artefact qui te permet de décider pour tout le monde.")
    print("Narrateur : Le " + character.nom + " s'approche du Coeur.")
    print("Ethan : Si tu le détruis, tout ce que j'ai fait aura été inutile !")
    print(character.nom + " : Ce n'est pas le pouvoir qui donne un sens à ta vie.")
    print("Narrateur : Le " + character.nom + " frappe le Coeur. L'artefact se brise et sa lumière disparaît.")
    print("Narrateur : Le silence retombe dans la salle.")
    print("Ethan : Tout ce que j'ai fait... pour rien...")
    print("Narrateur : Ethan tombe à genoux. Arnaud, privé de son dernier avantage, est capturé.")
    # Espace
    print("Narrateur : Quelques semaines plus tard, les habitants de Monté Cristo se rassemblent sur la place du marché. Les archives prouvent les crimes d'Arnaud. Un conseil provisoire est établi pour reconstruire le royaume.")
    print("Andy : Je dois reconnaître une chose : nous avons accompli quelque chose d'incroyable.")
    print("Ferdinand : Et personne n'a même eu besoin de me payer une épée.")
    print("Andy : Ne gâche pas le moment.")
    print("Nathaniel : Le royaume devra apprendre à vivre sans tyran. Cela ne sera pas facile, mais c'est un début.")
    print(character.nom + " : La liberté ne se donne pas. Elle se protège.")
    print("Narrateur : Ethan est arrêté et devra répondre de ses actes.")


elif ending == 2 and Req_TrueEnding == 1:
    print(character.nom + " : Ethan, regarde ce que tu es devenu. Tu voulais arrêter un tyran et tu es en train de prendre sa place.")
    print("Ethan : Je voulais seulement que ma vie ait un sens.")
    print(character.nom + " : Elle peut en avoir un sans que tu contrôles tout le monde.")
    print("Narrateur : Le " + character.nom + " tend la main.")
    print(character.nom + " : Lâche l'artefact. Nous pouvons encore empêcher qu'il détruise tout.")
    print("Narrateur : Ethan regarde le Coeur, puis les visages de ses anciens compagnons.")
    print("Ethan : Et si je ne sais pas comment vivre autrement ?")
    print("Nathaniel : Alors tu apprendras. Personne ne naît en sachant réparer ses erreurs.")
    print("Andy : Pour une fois, je suis d'accord avec le prêtre. Et je tiens à préciser que c'est une journée historiquement importante.")
    print("Ferdinand : Ethan. Tu peux encore choisir.")
    print("Narrateur : Ethan hésite, puis laisse tomber le Coeur. Nathaniel le recouvre d'un sceau ancien.")
    print("Ethan : Je ne sais pas si je pourrai réparer ce que j'ai fait.")
    print(character.nom + " : Tu devras commencer par en assumer les conséquences.")
    # Espace
    print("Narrateur : Arnaud est arrêté. Ethan est placé sous surveillance et devra répondre de sa trahison. Le Coeur est enfermé dans un lieu protégé par plusieurs gardiens.")
    print("Narrateur : Le groupe quitte le château ensemble, mais Ethan marche derrière les autres, silencieux.")
    print("Andy : Alors... quelqu'un connaît une bonne auberge ?")
    print("Ferdinand : Tant qu'il y a de quoi manger.")
    print("Nathaniel : Vous ne pensez jamais à autre chose ?")
    print(character.nom + " : Pour une fois, laissons le royaume respirer.")
    print("Narrateur : Le groupe s'éloigne sur la route. Ethan les suit à distance, sans savoir s'il sera un jour de nouveau accepté.")


elif ending == 3 and req_EvilEnding == 1:
    print("Narrateur : Le " + character.nom + " regarde l'artefact. Il pourrait le détruire, le sceller ou s'en servir pour imposer sa propre vision du royaume.")
    print("Nathaniel : " + character.nom + ", ne fais pas cette erreur.")
    print("Andy : Nous avons combattu Arnaud pour être libres. Ne deviens pas un otro Arnaud.")
    print("Ferdinand : Je te fais confiance. Ne me force pas à le regretter.")
    print("Ethan : Tu comprends enfin. Le pouvoir est la seule chose qui empêche les autres de te piétiner !")
    print(character.nom + " : Si je peux empêcher les guerres et les injustices, pourquoi ne pas utiliser ce pouvoir ?")
    print("Nathaniel : Parce que tu ne pourras jamais garantir que tu auras toujours raison. Et parce que personne ne pourra te dire que tu as tort.")
    print("Narrateur : Le " + character.nom + " saisit le Coeur. Une lueur noire se répand dans la salle.")
    print("Nathaniel : Tu as fait ton choix.")
    print("Narrateur : Andy recule. Ferdinand baisse les yeux. Nathaniel quitte la salle, incapable d'accepter cette décision.")
    print("Ethan : Bienvenue dans le monde réel.")
    # Espace
    print("Narrateur : Le " + character.nom + " prend le contrôle du royaume au nom de la paix grâce aux ancienne archives volées.")
    print("Narrateur : Les conflits diminuent, mais les habitants n'ont plus le droit de s'opposer à ses décisions.")
    print("Narrateur : Arnaud a disparu, mais son système de domination survit sous un nouveau visage.")
    print("Narrateur : Le " + character.nom + " est assis sur le trône, le Coeur de Bedrock dans la main.")
    print(character.nom + " : Adieu misérable chaos...")


elif ending == 2:
    print("Narrateur : Après la bataille, Nathaniel retrouve une lettre dans les affaires d'Ethan. Elle a été écrite par son père avant sa disparition.")
    print("Nathaniel : J'ai trouvé quelque chose.")
    print(character.nom + " : Qu'est-ce que c'est ?")
    print("Nathaniel : Une lettre. Elle est adressée à Ethan.")
    print("Narrateur : Le " + character.nom + " prend la lettre et commence à lire.")
    print("Lettre : Ethan,\n " 
        + "Si tu lis cette lettre, c'est que je n'ai pas réussi à revenir.\n"
        + "Ne cherche pas à me venger. Arnaud m'a offert le pouvoir, et j'ai refusé. C'est pour cela qu'il m'a fait disparaître.\n"
        + "J'ai cru longtemps que la vérité suffirait à sauver le royaume. Je me trompais. La vérité a besoin de personnes prêtes à la défendre, mais elle ne justifie pas tous les moyens.\n"
        + "Le Coeur de Bedrock ne rend pas les hommes forts. Il donne simplement plus de place à ce qu'ils portent déjà en eux.\n"
        + "Si tu veux changer le monde, ne deviens pas prisonnier de ta propre colère.\n"
        + "Je ne te demande pas d'oublier ce qui nous est arrivé. Je te demande de ne pas laisser notre malheur décider de toute ta vie.\n"
        + "Ton père.")
    print("Narrateur : Le " + character.nom + " referme la lettre.")
    print(character.nom + " : Il voulait venger son père. Mais il a fini par poursuivre la même chose qu'Arnaud.")
    print("Nathaniel : La souffrance peut expliquer les choix d'un homme. Elle ne les justifie pas tous.")
    print("Andy : Je crois que c'est la première fois que je n'ai aucune plaisanterie à faire.")
    print("Ferdinand : Alors c'est vraiment grave.")
    print("Narrateur : Le groupe quitte le château. Les cloches de Monté Cristo sonnent pour la première fois depuis des années.")
    print("Narrateur : Les habitants sortent de leurs maisons. Certains pleurent, d'autres applaudissent, et beaucoup restent simplement silencieux, comme s'ils n'osaient pas encore croire que la peur avait pris fin.")
    print(character.nom + " : Nous avons réussi.")
    print("Nathaniel : Nous avons commencé. Le reste dépendra de ce que les habitants feront de leur liberté.")
    print("Andy : Et de ce que je ferai de ma carrière musicale.")
    print("Ferdinand : Tu vas encore donner des concerts ?")
    print("Andy : Bien évidemment.")
    print(character.nom + " : Comment va-t-il s'appeler ?")
    print("Andy : Cinq idiots et un tyran.")
    print("Ferdinand : Pourquoi cinq idiots ?")
    print("Andy : Parce que je me compte dedans. Je suis humble.")
    print("Nathaniel : C'est la chose la moins crédible que tu aies jamais dite.")
    print("Andy : Merci. Je travaille dur pour rester cohérent.")

# Crédits
print("------------------------\n"
    + "Développeur : Nathaniel\n"
    + "Écriture de l'histoire et playtesteur : Andy\n"
    + "Support moral : Ferdinand\n"
    + "------------------------"
    + "MERCI D'AVOIR JOUÉ !!!")
