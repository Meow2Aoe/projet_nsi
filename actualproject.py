from time import * ; from random import * ; from colorama import *
class chara:
    def __init__(self,nom,classe,vie,magika,mana,degat,arme,argent):
        self.nom=nom
        self.classe=classe
        self.vie=vie
        self.magika=magika
        self.mana=mana
        self.degat=degat
        self.arme=arme
        self.argent=argent

class mobs:
    def __init__(self, nom, race, magika, degat, argent):
        self.nom=nom
        self.race=race
        self.magika=magika
        self.degat=degat
        self.argent=argent

class arme:
    def __init__(self, nom, degat, durabilite):
        self.nom=nom
        self.degat=degat
        self.dura=durabilite

# default weapon
null_sword=arme("null sword",0,0)
starter_sword=arme("Épée basique", 1, 20)
starter_bow=arme("Arc basique", 1, 20)
starter_staff=arme("Sceptre basique", 1, 20)
starter_music=arme("Luthe basique", 1, 20)

# tier 1 weapon


# tier 2 weapon


Ferdi_sword=arme("L'épée de Fertiplouf", 10, 1)

# personnages secondaires
Nath=chara("Nathaniel", 3, 80, 4, 150, 1.1, starter_staff.nom, randint(0,250))
Andy=chara("Andy", 0, 100, 2, 100, 1, starter_music.nom, randint(0,250))
Ferdi=chara("Ferdinand", 1, 150, 3, 75, 10, Ferdi_sword.nom, randint(0,250))
Ethan=chara()

# variable stock
a=0;temp=""

#############################################################
#                                                           #
#   Act 1 Prologue                                          #
#   quick contexte (bcp de blabla) + "character creator "   #
#                                                           #
#############################################################

print(Fore.BLUE + "Act 1 : Prologue : La rencontre")
print(Fore.WHITE + "Narrateur : C'est une belle fin de journée d'été dans le grand royaume de Monté-Cristo, après une dure journée à votre emploi, vous êtes allé au bar, vous avez bus et vous avez finit par vous endormir.") ; sleep(3.5)

print(Fore.WHITE +"\nNarrateur : Un grand sage apparait dans votre rêve et vous tend la main.\nGrand Sage : Enchanté mon/ma cher(e)... Quel est ton nom ?")
name=str(input(Fore.BLUE +"\nEntrez le nom du personnage : "))
while temp!="oui":
    temp=str(input(Fore.BLUE +"\nVotre nom est bien " + name + " ? (rentrez oui/non)\n"))
    if temp!="oui":
        name=str(input("Entrez le nom du personnage : "))

print("Grand Sage : Un nom très exotique, " + name + "... Enfin passons, aujourd'hui j'apparait dans votre inconscient pour vous offrir un pouvoir et vous permettre de sortir de votre routine.") ; sleep(2)
sleep(3.5)

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
character=chara(name,laclasse,100,type,100,1,null_sword.nom,150)
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
print("Grand Sage : Bien, bien... " + character.nom + " votre nouvelle vie va enfin pouvoir commencer !\nNarrateur : Le grand sage disparait de votre rêve et vous vous rendormez") ; sleep(3.5)
print("Narrateur :  ")
