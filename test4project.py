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

class arme:
    def __init__(self, nom, degat, durabilite):
        self.nom=nom
        self.degat=degat
        self.dura=durabilite

null_sword=arme('null sword',0,0)
starter_sword=arme("Épée basique", 1, 20)
starter_bow=arme("Arc basique", 1, 20)
starter_staff=arme("Sceptre basique", 1, 20)

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
    

print(character.nom, character.classe, character.vie, character.magika, character.mana, character.degat, character.arme)
'''
Nom , classe , vie , type de magie , nombre de mana , multiplicateur de dégat, arme
'''
