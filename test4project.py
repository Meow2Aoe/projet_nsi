from time import * ; from random import * ; from colorama import *
totalheal=0
a=0
class chara:
    '''
    Classe pour la création du personnage contenant (pour l'instant) son nom, sa vie, sa classe, son type de magie, son mana et son multiplicateur de dégat
    '''
    def __init__(self,nom,classe,vie,magika,mana,degat,arme):
        self.nom=nom
        self.classe=classe
        self.vie=vie
        self.magika=magika
        self.mana=mana
        self.degat=degat
        self.arme=arme

class mobs:
    def __init__(self, nom, pv, race, magika, degat, argent):
        self.nom=nom
        self.race=race
        self.magika=magika
        self.degat=degat
        self.argent=argent
        self.pv=pv



class arme:
    def __init__(self, nom, degat, durabilite):
        self.nom=nom
        self.degat=degat
        self.dura=durabilite

null_sword=arme("null sword",0,0)
starter_sword=arme("Épée basique", 1, 20)
starter_bow=arme("Arc basique", 1, 20)
starter_staff=arme("Sceptre basique", 1, 20)
starter_music=arme("Luthe basique", 1, 20)
starter_cook=arme("Couteau à pain", 1, 20)
Ferdi_sword=arme("L'épée de Fertiplouf", 10, 1)

# character creator

name=str(input("Entrez le nom du personnage : "))
laclasse=int(input("Choississez votre classe :\n 1 = Mêlée\n 2 = Ranger\n 3 = Mage\n"))
type=int(input("Choississez votre type de Magika :\n 1 = Feu\n 2 = Eau\n 3 = Terre\n 4 = Esprit\n 5 = Chaos\n"))

character=chara(name,laclasse,100,type,100,1,null_sword)
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
    

#print(character.nom, character.classe, character.vie, character.magika, character.mana, character.degat, character.arme)
'''
Nom , classe , vie , type de magie , nombre de mana , multiplicateur de dégat, arme
'''

Nath=chara("Nathaniel", 3, 80, 4, 150, 1.1, starter_staff.nom)
Andy=chara("Andy", 0, 100, 2, 100, 1, starter_music.nom, )
Ferdi=chara("Ferdinand", 1, 150, 3, 75, 10, Ferdi_sword.nom)
Ethan=chara("Éthan", 0, 120, 1, 80, 0.7, starter_cook.nom)
List_player=[character, Nath, Andy, Ferdi]

enemi=mobs("mob1",100,'moche',1,1,100)






def affichage_combat():
    move=int(input("--------------------------\n1 = attaque  /  2 = magie\n3 = test\n--------------------------"))
    if move==1:
        pass
    elif move==2:
        pass
    elif move==3:
        pass



def totalpv(List_player):
    totalheal=0
    for i in List_player:
        totalheal+=i.vie

print(totalpv(List_player))
def attack(List_player):
    pass



def fight():
    totalpv(List_player)
    while totalheal>=0:
        print(1)
        for i in List_player:
            i.vie-=15
            if i.vie<=0:
                List_player.pop(i.)
        
fight()
