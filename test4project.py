from time import * ; from random import * ; from colorama import *
totalheal=0
a=0
list_enemi=[]
diff=1
buy=0
shop=0
stade_equipe=0
num=0
finished=0
IsArnaudDead=0
temp_objet=0
objetprecedent=0
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

class objet:
    def __init__(self, nom, quantite, prix, rarete, ID):
        self.nom=nom
        self.quantite=quantite
        self.prix=prix
        self.rarete=rarete
        self.ID=ID

null_sword=arme("null sword",6969,1000,6969)
starter_sword=arme("Épée basique", 1, 5,50)
starter_bow=arme("Arc basique", 1, 5, 50)
starter_staff=arme("Sceptre basique", 1, 5, 50)
starter_music=arme("Luthe basique", 1, 5, 50)
starter_cook=arme("Couteau à pain", 1, 5, 50)
Ferdi_sword=arme("L'épée de Fertiplouf", 10, 1, 50)

tier1_sword=arme("Katana de Yone", 1.75, 25,350)
tier1_bow=arme("...", 1.75, 25, 350)
tier1_staff=arme("...", 1.75, 25, 350)
tier1_music=arme("...", 1.75, 25, 350)
tier1_cook=arme("Couteau à beurre", 1.75, 25, 350)

tier2_sword=arme("Rapière du dieu Arès", 2.5, 25,750)
tier2_bow=arme("Arc de la déese d'Arthémis", 2.5, 25, 750)
tier2_staff=arme("Aghanim's scepter", 2.5, 25, 750)
tier2_music=arme("Harpe de Apollon", 2.5, 25, 750)
tier2_cook=arme("Mbappe's Dagger", 2.5, 25, 750)

ultimate_sword=arme("...", 5, 50,1250)
ultimate_bow=arme("M4A1", 5, 50, 1250)
ultimate_staff=arme("", 5, 50, 1250)
ultimate_music=arme("Méga Ukulele", 5, 50, 1250)
ultimate_cook=arme("Baguette de Pain Traditionnelle Française", 5, 50, 1250)
Ferdi_sword=arme("L'épée de Fertiplouf", 10, 6969, 50)
shadow_scythe=arme("Faux des ombres", 25, 100, 0)

potion_heal1=objet("Fiole de soin", 1, 15, "Basique", 1)
potion_heal2=objet("Potion de soin", 0, 25, "Rare", 2)
potion_heal3=objet("Patch de soin", 1, 50, "Épique", 3)
potion_mana1=objet("Fiole de mana", 0, 15, "Basique", 4)
potion_mana2=objet("Potion de mana", 1, 25, "Rare", 5)
potion_mana3=objet("Patch de mana", 0, 50, "Épique", 6)

bp=[potion_heal1,potion_heal2,potion_heal3,potion_mana1,potion_mana2,potion_mana3]

# character creator
name=str(input("Entrez le nom du personnage : "))
laclasse=int(input("Choississez votre classe :\n1 = Mêlée\n2 = Ranger\n3 = Mage\n"))
typee=int(input("Choississez votre type de Magika :\n1 = Feu\n2 = Eau\n3 = Terre\n4 = Divin\n"))

character=chara(name, laclasse, 100, typee, 100, null_sword.degat, null_sword.nom, null_sword.dura, 1, 0, randint(25,150))
if laclasse==1:         # classe -> mêlée
    character.vie+=25
    character.mana-=25
    character.degat*=1.3
    character.arme=starter_sword.nom
    character.degat=starter_sword.degat
    character.dura=starter_sword.dura
if laclasse==2:         # classe -> ranger
    character.vie-=15
    character.degat*=1.25
    character.arme=starter_bow.nom
    character.degat=starter_bow.degat
    character.dura=starter_bow.dura
if laclasse==3:         # classe -> mage
    character.vie-=35
    character.mana+=50
    character.degat*=1.1
    character.arme=starter_staff.nom
    character.degat=starter_staff.degat
    character.dura=starter_staff.dura
if character.nom.lower()=="Reaper".lower():
    if laclasse==4:         # la classe secrète (reaper)
        character.degat=1
        character.arme=shadow_scythe.nom
        character.degat=shadow_scythe.degat
        character.dura=shadow_scythe.dura
'''
Nath=chara("Nathaniel", 3, 80, 4, 150, starter_staff.degat, starter_staff.nom, starter_staff.dura, 1, 0, randint(25,150))
Andy=chara("Andy", 0, 100, 2, 100, starter_music.degat, starter_music.nom, starter_music.dura, 1, 0, randint(25,150))
Ferdi=chara("Ferdinand", 1, 150, 3, 75, Ferdi_sword.degat, Ferdi_sword.nom, Ferdi_sword.dura, 1, 0, 0)
Ethan=chara("Éthan", 0, 120, 1, 80, starter_cook.degat, starter_cook.nom, starter_cook.dura, 1, 0, randint(25,150))
'''
Nath=chara("Nathaniel", 3, 80, 4, 150, starter_staff.degat, starter_staff.nom, starter_staff.dura, 1, 0, 5000)
Andy=chara("Andy", 0, 100, 2, 100, starter_music.degat, starter_music.nom, starter_music.dura, 1, 0, 5000)
Ferdi=chara("Ferdinand", 1, 150, 3, 75, Ferdi_sword.degat, Ferdi_sword.nom, Ferdi_sword.dura, 1, 0, 5000)
Ethan=chara("Éthan", 0, 120, 1, 80, starter_cook.degat, starter_cook.nom, starter_cook.dura, 1, 0, 5000)


max_vie=character.vie
List_player=[character, Andy,Nath]
list_ferdi=[Ferdi]


goblin=mobs("Goblin Racketteur", 45, 'goblin',0, 100,1.2,10,5)
balai=mobs("Balais Possédé", 60, 'objet', 0, 100, 1.5, 17, 7)
mannequin=mobs("Mannequin de Combat", 90, 'objet', 0, 100, 1.75 , 25, 10)

Chevalier=mobs("Chevalier de la Craie", 100, 'humain', 0, 150, 1.75, 50, 15)
mimik=mobs("Mimique Gourmand", 120, 'objet', 0, 150, 1.6, 60, 17)

garde=mobs('Garde du Tableau Noir', 200, 'esprit', 0, 200, 2, 100, 20)
loup=mobs('Loup des Ombres', 150, 'esprit', 0, 200, 2.2, 120, 25)
cake=mobs('Gâteau Mutant', 250, 'esprit', 0, 200, 1.8, 135, 30)

Arnaud=mobs("M. Arnaud", 1500, 'humain', 0, 1000, 1, 50000, 300)
Ethan_boss=mobs("Éthan", 750, 'humain', 0, 500, 2, Ethan.argent/4, 100*Ethan.lvl)

def affichage_combat(k,enemi,List_player):
    if stade_equipe==0:
        print(character.nom + " : " + str(character.vie) + "pv / Andy : " + str(Andy.vie) + "pv")
    elif stade_equipe==1:
        print(character.nom + " : " + str(character.vie) + "pv / Nathaniel : " + str(Nath.vie) + "pv / Andy : " + str(Andy.vie) + "pv")
    elif stade_equipe==2:
        print(character.nom + " : " + str(character.vie) + "pv / Nathaniel : " + str(Nath.vie) + "pv / Andy : " + str(Andy.vie) + "pv / Éthan : " + str(Ethan.vie) + "pv")
    elif stade_equipe==3:
        print(character.nom + " : " + str(character.vie) + "pv")
    move=int(input("-------------------------------------\nTour de " + k.nom + " (" + str(k.mana) + " mana)"  +"\n1 = attaque  /  2 = magie / 3 = Objet\n--------------------------------------\n"))
    if move==1:
        attack(k,enemi)
    elif move==2:
        if k.mana<=10:
            print("Vous n'avez pas assez de Mana pour attaquer")
        else:    
            magie(k,enemi,List_player)
    elif move==3:
        backpack(bp, k)

def backpack(bp, k):
    for i in bp:
        if i.quantite>=1:
            print(str(i.ID) + " = " + i.nom +" (" + str(i.quantite) +")")
    choic=int(input("Choississez l'objet (son ID)\n"))
    for i in bp:
        if i.ID == choic and i.quantite > 0:
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

def lookup_arme(List_player):
    for i in List_player:
        if i.dura==0:
            return 0
    return 1

def lvlup():
    for i in List_player:
        while i.xp>=100:
            i.degat+=0.2
            i.lvl+=1
            i.vie*=1.15
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

def attack(k,enemi):
    enemi.pv-=5*k.degat*k.lvl
    return enemi

def attack_enemi(enemi, List_player):
    for i in List_player:
        if i.vie<=0:
            List_player.remove(i)
        elif character.vie<=0:
            gameover()
    perso=choice(List_player)
    perso.vie-=5*enemi.degat
    return perso

def rdm_enemi():
    if diff==10:
        enemi=garde_1
    if diff==11:
        enemi=garde_2
    if diff==12:
        enemi=mini_boss1
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
        while totalpv(List_player)>0 and enemi.pv>0:
            for k in List_player:
                affichage_combat(k, enemi, List_player)
                print(k.nom + " attaque  ->  " + str(enemi.pv) + "\n")
            cible=attack_enemi(enemi,List_player)
            print(enemi.nom + " attaque " + cible.nom + " -> " + str(cible.vie) + "pv.")
        for i in List_player:
            i.xp+=enemi.xp
        lvlup()
        for i in List_player:
            i.dura-=1
    else:
        print("Vous ne pouvez pas vous battre car vous n'avez pas d'arme.")
        armurerie()
        fight()

def bossfightrdm(IsArnaudDead):
    if IsArnaudDead==0:
        enemi=Arnaud
    else:
        enemi==Ethan_boss
    return enemi

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
                cible,a,objet_vole_ce_tour,temp_objet=attack_arnaud(enemi,List_player,bp)
                print(enemi.nom + " attaque " + cible.nom + " -> " + str(cible.vie) + "pv.")
                if objet_vole_ce_tour!=0:
                    objetprecedent=objet_vole_ce_tour
                if objetprecedent!=None:
                    objetprecedent=temp_objet
                    print("Vous avez récuperer vos objets")
                    objetprecedent=0
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
        fight()



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


def attack_ethan(enemi, List_player):
    if 500<enemi.pv<=750:        # phase 1
        pass

def gameover():
    pass

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
            + potion_mana3.nom + " ("+ str(potion_mana3.prix) + ")\n"))
            if achat==1:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_heal1.prix*quantity:
                    potion_heal1.quantite+=quantity
                    i.argent-=potion_heal1.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de fiole de soin ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            if achat==2:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_heal2.prix*quantity:
                    potion_heal2.quantite+=quantity
                    i.argent-=potion_heal2.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de potion de soin ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            if achat==3:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_heal3.prix*quantity:
                    potion_heal3.quantite+=quantity
                    i.argent-=potion_heal3.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de patch de soin ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            if achat==4:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_mana1.prix*quantity:
                    potion_mana1.quantite+=quantity
                    i.argent-=potion_mana1.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de fiole de mana ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            if achat==5:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_mana2.prix*quantity:
                    potion_mana2.quantite+=quantity
                    i.argent-=potion_mana2.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de potion de mana ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
            if achat==6:
                quantity=int(input("Combien voulez vous en achetez ?\n"))
                if i.argent>=potion_mana3.prix*quantity:
                    potion_mana3.quantite+=quantity
                    i.argent-=potion_mana3.prix*quantity
                    print("Vous avez achetés " + str(quantity) + " de fiole de soin ! (vous avez maintenant " + str(i.argent) + ")")
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ceci (vous avez maintenant " + str(i.argent) + ").")
        finished=int(input("Mathieu le vendeur : Ce sera tout ?\n1 = OUI\n2 = NON\n"))

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

armurerie()
List_player=[character, Andy, Nath] ; stade_equipe=1
boss_fight(IsArnaudDead=0)

'''
Boss Fight
Phase 1 : 1500 hp
    - Attaque basique(15hp)
    - Boost les dégats
    - Attaque tout le monde (10hp)
Phase 2 : 900 hp
    - Attaque basique + (25hp)
    - Enlève un objet au hasard (1 tour)
    - Attaque tout le monde + (20hp)
Phase 3 : 300hp
    - Attaque basique ++ (40hp)
    - Enlève tout les objets
    - Attaque tout le monde ++ (30hp)
    - Possibilité de se rendre (1 des fins du jeu)
'''
