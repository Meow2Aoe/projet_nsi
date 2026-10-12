from time import * ; from random import * ; from colorama import *
totalheal=0
a=0
list_enemi=[]
diff=1
class chara:
    '''
    Classe pour la création du personnage contenant (pour l'instant) son nom, sa vie, sa classe, son type de magie, son mana et son multiplicateur de dégat
    '''
    def __init__(self, nom, classe, vie, magika, mana, degat, arme, dura_arme, lvl, xp, argent):
        self.nom=nom
        self.classe=classe
        self.vie=vie
        self.magika=magika
        self.mana=mana
        self.degat=degat
        self.arme=arme
        self.lvl=lvl
        self.xp=xp
        self.dura=dura_arme
        self.argent=argent

class mobs:
    def __init__(self, nom, pv, race, magika, mana, degat, argent, xp):
        self.nom=nom
        self.race=race
        self.magika=magika
        self.degat=degat
        self.argent=argent
        self.pv=pv
        self.xp=xp
        self.mana=mana

class arme:
    def __init__(self, nom, degat, durabilite, prix):
        self.nom=nom
        self.degat=degat
        self.dura=durabilite
        self.prix=prix

null_sword=arme("null sword",6969,1000,6969)
starter_sword=arme("Épée basique", 1, 25,50)
starter_bow=arme("Arc basique", 1, 25, 50)
starter_staff=arme("Sceptre basique", 1, 0, 50)
starter_music=arme("Luthe basique", 1, 25, 50)
starter_cook=arme("Couteau à pain", 1, 25, 50)
Ferdi_sword=arme("L'épée de Fertiplouf", 10, 1, 50)

# character creator
name=str(input("Entrez le nom du personnage : "))
laclasse=int(input("Choississez votre classe :\n1 = Mêlée\n2 = Ranger\n3 = Mage\n"))
type=int(input("Choississez votre type de Magika :\n1 = Feu\n2 = Eau\n3 = Terre\n4 = Divin\n"))

character=chara(name,laclasse,100,type,100,1,null_sword, 0, 1, 0, randint(25,150))
if laclasse==1:         # classe -> mêlée
    character.vie+=25
    character.mana-=25
    character.degat*=1.3
    character.arme=starter_sword.nom
    character.dura=starter_sword.dura
if laclasse==2:         # classe -> ranger
    character.vie-=15
    character.degat*=1.25
    character.arme=starter_bow.nom
    character.dura=starter_bow.dura
if laclasse==3:         # classe -> mage
    character.vie-=35
    character.mana+=50
    character.degat*=1.1
    character.arme=starter_staff.nom
    character.dura=starter_staff.dura


Nath=chara("Nathaniel", 3, 80, 4, 150, starter_staff.degat, starter_staff.nom, starter_staff.dura, 1, 0, randint(25,150))
Andy=chara("Andy", 0, 100, 2, 100, starter_music.degat, starter_music.nom, starter_music.dura, 1, 0, randint(25,150))
Ferdi=chara("Ferdinand", 1, 150, 3, 75, Ferdi_sword.degat, Ferdi_sword.nom, Ferdi_sword.dura, 1, 0, 0)
Ethan=chara("Éthan", 0, 120, 1, 80, starter_cook.degat, starter_cook.nom, starter_cook.dura, 1, 0, randint(25,150))
List_player=[character, Nath, Andy]
list_ferdi=[Ferdi]


goblin=mobs("Goblin Racketteur", 45, 'goblin',0, 100,1.2,10,5)
balai=mobs("Balais Possédé", 60, 'objet', 0, 100, 1.5, 17, 7)
mannequin=mobs("Mannequin de Combat", 90, 'objet', 0, 100, 1.75 , 25, 10)

Chevalier=mobs("Chevalier de la Craie", 100, 'humain', 0, 150, 1.75, 50, 15)
mimik=mobs("Mimique Gourmand", 120, 'objet', 0, 150, 1.6, 60, 17)

garde=mobs('Garde du Tableau Noir', 200, 'esprit', 0, 200, 2, 100, 20)
loup=mobs('Loup des Ombres', 150, 'esprit', 0, 200, 2.2, 120, 25)
cake=mobs('Gâteau Mutant', 250, 'esprit', 0, 200, 1.8, 135, 30)


Arnaud=mobs("M. Arnaud", 5000, 'humain', 0, 1000, 2, 50000, 300)

bossfinal=Arnaud


def affichage_combat(k,enemi,List_player):
    print(character.nom + " : " + str(character.vie) + "pv / Nathaniel : " + str(Nath.vie) + "pv / Andy : " + str(Andy.vie) + "pv")
    move=int(input("-------------------------------------\nTour de " + k.nom +"\n1 = attaque  /  2 = magie / 3 = Objet\n--------------------------------------\n"))
    if move==1:
        attack(k,enemi)
    elif move==2:
        if k.mana<=10:
            print("Vous n'avez pas assez de Mana pour attaquer")
        else:    
            magie(k,enemi,List_player)
    elif move==3:
        backpack()

def backpack():
    pass

def lookup_arme(List_player):
    for i in List_player:
        if i.dura==0:
            return 0
    return 1

def lvlup():
    for i in List_player:
        while i.xp>=100:
            i.lvl+=0.2
            i.xp-=100
        print("Félicitation ! " + i.nom + " a augmenté d'un niveau, il est maintenant niveau " + str(i.lvl)+ ".")

def totalpv(List_player):
    totalheal=0
    for i in List_player:
        totalheal+=i.vie
    return totalheal

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
            sort=int(input("--------------------------\n1 = Lumière Divine (-10 mana) /  2 =  (-20mana)\n3 = Hamaon (-1 mana)\n--------------------------\n"))
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


def attack(k,enemi):
    enemi.pv-=5*k.degat*k.lvl
    return enemi

def attack_enemi(enemi, List_player):
    for i in List_player:
        if i.vie<=0:
            List_player.remove(i)
    perso=choice(List_player)
    perso.vie-=5*enemi.degat

def rdm_enemi():
    if diff==1:
        enemi1=randint(0,2)
        if enemi1==0:
            enemi=goblin
        elif enemi1==1:
            enemi=balai
        elif enemi1==2:
            enemi=mannequin
    if diff==2:
        enemi1=randint(0,4)
        if enemi1==0:
            enemi=goblin
        elif enemi1==1:
            enemi=balai
        elif enemi1==2:
            enemi=mannequin
        elif enemi1==3:
            enemi=Chevalier
        elif enemi1==4:
            enemi=mimik
    if diff==3:
        enemi1=randint(0,4)
        if enemi1==0:
            enemi=garde
        elif enemi1==1:
            enemi=cake
        elif enemi1==2:
            enemi=loup
        elif enemi1==3:
            enemi=Chevalier
        elif enemi1==4:
            enemi=mimik
    return enemi

def fight():
    arme_equipe=lookup_arme(List_player)
    if arme_equipe==1:
        enemi=rdm_enemi()
        print("\nUn " + str(enemi.nom) + " apparait et il a " + str(enemi.pv) + " PV")
        nb_entity=len(List_player)+1
        while totalpv(List_player)>0:
            for k in List_player:
                if enemi.pv>=0:
                    affichage_combat(k,enemi,List_player)
                    print(k.nom + " attaque  ->  " + str(enemi.pv))
                    print()
                else:
                    for i in List_player:
                        i.xp+=enemi.xp
                    break
            attack_enemi(enemi,List_player)
        lvlup()
        for i in List_player:
            i.dura-=1
    else:
        print("Vous ne pouvez pas vous battre car vous n'avez pas d'arme.")

fight()

def shop_heal():
    print("-----------------------------------\nAntoine le vendeur : Bien le bonjour ! Qu'est ce qu'il vous faudrait ?\n1 = ")
    print("aaaaaaaaaaaa\n-----------------------------------")


def armurerie():
    print("-----------------------------------\nKilliann le forgeron : Bonjour. Vous avez b'soin d'quoi ?")
    shop=int(input("1 = " + character.nom + "\n2 = Nath\n3 = Andy\n4 = Ethan\n-----------------------------------"))
    if shop==1:
        if laclasse==1:     # mêlée
            achat=int(input("1 = " + tier1_sword.nom + '  ->  ' + str(tier1_sword.prix) +
            "2 = " + tier2_sword.nom + "  ->  " + str(tier2_sword.prix) + 
            "3 = " + ultimate_sword.nom + "  ->  " + str(ultimate_sword.prix)))
            if achat==1:
                if character.argent>=tier1_sword.prix:
                    character.arme=tier1_sword.nom
                    character.dura=tier1_sword.dura
                    character.degat=tier1_sword.degat
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
            if achat==2:
                if character.argent>=tier2_sword.prix:
                    character.arme=tier2_sword.nom
                    character.dura=tier2_sword.dura
                    character.degat=tier2_sword.degat
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
            if achat==3:
                if character.argent>=ultimate_sword.prix:    
                    character.arme=ultimate_sword.nom
                    character.dura=ultimate_sword.dura
                    character.degat=ultimate_sword.degat
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
        elif laclasse==2:   # ranger
            achat=int(input("1 = " + tier1_bow.nom + '  ->  ' + str(tier1_bow.prix) +
            "2 = " + tier2_bow.nom + "  ->  " + str(tier2_bow.prix) + 
            "3 = " + ultimate_bow.nom + "  ->  " + str(ultimate_bow.prix)))
            if achat==1:
                if character.argent>=tier1_bow.prix:
                    character.arme=tier1_bow.nom
                    character.dura=tier1_bow.dura
                    character.degat=tier1_bow.degat
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
            if achat==2:
                if character.argent>=tier2_bow.prix:
                    character.arme=tier1_bow.nom
                    character.dura=tier1_bow.dura
                    character.degat=tier1_bow.degat
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
            if achat==3:
                if character.argent>=ultimate_bow.prix:    
                    character.arme=ultimate_bow.nom
                    character.dura=ultimate_bow.dura
                    character.degat=ultimate_bow.degat
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
        elif laclasse==3:   # mage
            achat=int(input("1 = " + tier1_staff.nom + '  ->  ' + str(tier1_staff.prix) +
            "2 = " + tier2_staff.nom + "  ->  " + str(tier2_staff.prix) + 
            "3 = " + ultimate_staff.nom + "  ->  " + str(ultimate_staff.prix)))
            if achat==1:
                if character.argent>=tier1_staff.prix:
                    character.arme=tier1_staff.nom
                    character.dura=tier1_staff.dura
                    character.degat=tier1_staff.degat
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
            if achat==2:
                if character.argent>=tier2_staff.prix:
                    character.arme=tier1_staff.nom
                    character.dura=tier1_staff.dura
                    character.degat=tier1_staff.degat
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
            if achat==3:
                if character.argent>=ultimate_staff.prix:    
                    character.arme=ultimate_staff.nom
                    character.dura=ultimate_staff.dura
                    character.degat=ultimate_staff.degat
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
    elif buy==2:
        achat=int(input("1 = " + tier1_staff.nom + '  ->  ' + str(tier1_staff.prix) +
            "2 = " + tier2_staff.nom + "  ->  " + str(tier2_staff.prix) + 
            "3 = " + ultimate_staff.nom + "  ->  " + str(ultimate_staff.prix)))
        if achat==1:
            if character.argent>=tier1_staff.prix:
                character.arme=tier1_staff.nom
                character.dura=tier1_staff.dura
                character.degat=tier1_staff.degat
            else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci")
        if achat==2:
            if character.argent>=tier2_staff.prix:
                character.arme=tier1_staff.nom
                character.dura=tier1_staff.dura
                character.degat=tier1_staff.degat
            else:
                print("Vous n'avez pas assez d'argent pour acheter ceci")
        if achat==3:
            if character.argent>=ultimate_staff.prix:    
                character.arme=ultimate_staff.nom
                character.dura=ultimate_staff.dura
                character.degat=ultimate_staff.degat
            else:
                print("Vous n'avez pas assez d'argent pour acheter ceci")
    elif buy==3:
        print()
    elif buy==4:
        print()



armurerie()

# sac a dos (objet)