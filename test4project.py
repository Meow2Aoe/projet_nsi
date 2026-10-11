from time import * ; from random import * ; from colorama import *
totalheal=0
a=0
list_enemi=[]
class chara:
    '''
    Classe pour la création du personnage contenant (pour l'instant) son nom, sa vie, sa classe, son type de magie, son mana et son multiplicateur de dégat
    '''
    def __init__(self, nom, classe, vie, magika, mana, degat, arme, lvl, xp):
        self.nom=nom
        self.classe=classe
        self.vie=vie
        self.magika=magika
        self.mana=mana
        self.degat=degat
        self.arme=arme
        self.lvl=lvl
        self.xp=xp

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
    def __init__(self, nom, degat, durabilite):
        self.nom=nom
        self.degat=degat
        self.dura=durabilite

null_sword=arme("null sword",0,1000)
starter_sword=arme("Épée basique", 1, 25)
starter_bow=arme("Arc basique", 1, 25)
starter_staff=arme("Sceptre basique", 1, 25)
starter_music=arme("Luthe basique", 1, 25)
starter_cook=arme("Couteau à pain", 1, 25)
Ferdi_sword=arme("L'épée de Fertiplouf", 10, 1)

# character creator
name=str(input("Entrez le nom du personnage : "))
laclasse=int(input("Choississez votre classe :\n1 = Mêlée\n2 = Ranger\n3 = Mage\n"))
type=int(input("Choississez votre type de Magika :\n1 = Feu\n2 = Eau\n3 = Terre\n4 = Divin\n"))

character=chara(name,laclasse,100,type,100,1,null_sword,1,0)
if laclasse==1:         # classe -> mêlée
    character.vie+=25
    character.mana-=25
    character.degat*=1.3
    character.arme=starter_sword.nom
if laclasse==2:         # classe -> ranger
    character.vie-=15
    character.degat*=1.25
    character.arme=starter_bow.nom
if laclasse==3:         # classe -> mage
    character.vie-=35
    character.mana+=50
    character.degat*=1.1
    character.arme=starter_staff.nom


Nath=chara("Nathaniel", 3, 80, 4, 150, 1.1, starter_staff.nom,1,0)
Andy=chara("Andy", 0, 100, 2, 100, 1, starter_music.nom,1,0 )
Ferdi=chara("Ferdinand", 1, 150, 3, 75, 10, Ferdi_sword.nom,1,0)
Ethan=chara("Éthan", 0, 120, 1, 80, 0.7, starter_cook.nom,1,0)
List_player=[character, Nath, Andy]
list_ferdi=[Ferdi]


goblin=mobs("Goblin Racketteur", 45, 'goblin',0, 100,1.2,10,5)
balai=mobs("Balais Possédé", 60, 'objet', 0, 100, 1.5, 17, 7)
mannequin=mobs("Mannequin de Combat", 90, 'objet', 0, 100, 1.75 , 25, 10)

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
        attack(k,enemi)

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
                    enemi.pv=randint(7,15)*k.degat*k.lvl
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
                    enemi.pv=randint(7,15)*k.degat*k.lvl
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
                    enemi.pv=randint(7,15)*k.degat*k.lvl
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
                enemi.pv=randint(7,15)*k.degat*k.lvl
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
                enemi.pv=randint(7,15)*k.degat*k.lvl
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


def rdm_enemi1():
    enemi_faible=randint(0,2)
    if enemi_faible==0:
        enemi=goblin
    elif enemi_faible==1:
        enemi=balai
    elif enemi_faible==2:
        enemi=mannequin
    return enemi

def fight():
    enemi=rdm_enemi1()
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
        
        
        
fight()


# sac a dos (objet)