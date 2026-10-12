from time import * ; from random import * ; from colorama import *
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

# mon bullshit d'amour

()

# default weapon

null_sword=arme("null sword",6969,1000,6969)
starter_sword=arme("Épée basique", 1, 25,50)
starter_bow=arme("Arc basique", 1, 25, 50)
starter_staff=arme("Sceptre basique", 1, 0, 50)
starter_music=arme("Luthe basique", 1, 25, 50)
starter_cook=arme("Couteau à pain", 1, 25, 50)

# tier 1 weapon



# tier 2 weapon



#ultimate weapon

Ferdi_sword=arme("L'épée de Fertiplouf", 10, 1, 50)

# personnages

Nath=chara("Nathaniel", 3, 80, 4, 150, starter_staff.degat, starter_staff.nom, starter_staff.dura, 1, 0, randint(25,150))
Andy=chara("Andy", 0, 100, 2, 100, starter_music.degat, starter_music.nom, starter_music.dura, 1, 0, randint(25,150))
Ferdi=chara("Ferdinand", 1, 150, 3, 75, Ferdi_sword.degat, Ferdi_sword.nom, Ferdi_sword.dura, 1, 0, 0)
Ethan=chara("Éthan", 0, 120, 1, 80, starter_cook.degat, starter_cook.nom, starter_cook.dura, 1, 0, randint(25,150))

# mobs

goblin=mobs("Goblin Racketteur", 45, 'goblin',0, 100,1.2,10,5)
balai=mobs("Balais Possédé", 60, 'objet', 0, 100, 1.5, 17, 7)
mannequin=mobs("Mannequin de Combat", 90, 'objet', 0, 100, 1.75 , 25, 10)

Chevalier=mobs("Chevalier de la Craie", 100, 'humain', 0, 150, 1.75, 50, 15)
mimik=mobs("Mimique Gourmand", 120, 'objet', 0, 150, 1.6, 60, 17)

garde=mobs('Garde du Tableau Noir', 200, 'esprit', 0, 200, 2, 100, 20)
loup=mobs('Loup des Ombres', 150, 'esprit', 0, 200, 2.2, 120, 25)
cake=mobs('Gâteau Mutant', 250, 'esprit', 0, 200, 1.8, 135, 30)

Arnaud=mobs("M. Arnaud", 5000, 'humain', 0, 1000, 2, 50000, 300)

# variable stock

a=0 ; temp="" ; totalheal=0 ; diff=1 ; List_player=[] ; list_ferdi=[Ferdi] ; bossfinal=Arnaud

#############################################################
#                                                           #
#   Act 1 Prologue                                          #
#   quick contexte (bcp de blabla) + "character creator "   #
#                                                           #
#############################################################

print(Fore.BLUE + "Act 1 : Prologue : La rencontre")
print(Fore.WHITE + "Narrateur : C'est une belle fin de journée d'été dans le grand royaume de Monté-Cristo, après une dure journée à votre emploi, vous êtes allé au bar, vous avez bus et vous avez finit par vous endormir.") #; sleep(3.5)

print(Fore.WHITE +"\nNarrateur : Un grand sage apparait dans votre rêve et vous tend la main.\n")
print(Fore.GREEN + "Grand Sage : Enchanté mon/ma cher(e)... Quel est ton nom ?")
name=str(input(Fore.BLUE +"\nEntrez le nom du personnage : "))
while temp!="oui":
    temp=str(input(Fore.BLUE +"\nVotre nom est bien " + name + " ? (rentrez oui/non)\n"))
    if temp!="oui":
        name=str(input("Entrez le nom du personnage : "))

print("Grand Sage : Un nom très exotique, " + name + "... Enfin passons, aujourd'hui j'apparait dans votre inconscient pour vous offrir un pouvoir et vous permettre de sortir de votre routine.") #; sleep(3.5)

print("Grand Sage : Tout d'abord, quel classe choissirez vous ?")
laclasse=int(input(Fore.BLUE +"\nChoississez votre classe :\n1 = Mêlée\n2 = Ranger\n3 = Mage\n"))
temp=""
while temp!="oui":
    temp=str(input(Fore.BLUE +"\nÊtes vous sûre de choisir " + str(laclasse) + " ? (rentrez oui/non)\n"))
    if temp!="oui":
        laclasse=int(input(Fore.BLUE +"\nChoississez votre classe :\n1 = Mêlée\n2 = Ranger\n3 = Mage\n"))

print("Grand Sage : Haha, très intéressant... Et enfin, je vous confère un des 5 types de magika, lequel choissirez vous ?\n")
type=int(input(Fore.BLUE +"Choississez votre type de Magika :\n1 = Feu\n2 = Eau\n3 = Terre\n4 = Divine\n"))
temp=""
while temp!="oui":
    temp=str(input(Fore.BLUE +"\nÊtes vous sûre de choisir " + str(type) + " ? (rentrez oui/non)\n"))
    if temp!="oui":
        type=int(input(Fore.BLUE +"Choississez votre type de Magika :\n1 = Feu\n2 = Eau\n3 = Terre\n4 = Divine\n"))

character=chara(name,laclasse,100,type,100,1,null_sword, 0, 1, 0, randint(25,150))
List_player=[character, Nath, Andy, Ferdi]

if laclasse==1:         # classe -> mêlée
    character.vie+=25
    character.mana-=25
    character.degat*=1.1
    character.arme=starter_sword.nom
if laclasse==2:         # classe -> ranger
    character.vie-=15
    character.degat*=1.2
    character.arme=starter_bow.nom
if laclasse==3:         # classe -> mage
    character.vie-=35
    character.mana+=50
    character.degat*=1.1
    character.arme=starter_staff.nom
print("Grand Sage : Bien, bien... " + character.nom + " votre nouvelle vie va enfin pouvoir commencer !\nNarrateur : Le grand sage disparait de votre rêve et vous vous rendormez") ; #sleep(3.5)

print("Narrateur : ")