# exercices 2
import random
class NPC:

    def chiffre_aléatoire(self):
        dé1 = random.randint(1,6)
        dé2 = random.randint(1,6)
        dé3 = random.randint(1,6)
        dé4 = random.randint(1,6)
        caractéristique = 0
        if dé1 & dé2 & dé3 > dé4:
            caractéristique = dé1 + dé2 + dé3
        elif dé1 & dé3 & dé4 > dé2:
            caractéristique = dé1 + dé4 + dé3
        elif dé2 & dé3 & dé4 > dé1:
            caractéristique = dé4 + dé2 + dé3
        elif dé1 & dé2 & dé4 > dé3:
            caractéristique = dé1 + dé2 + dé4

        return caractéristique

    def __init__(self, nom, race, profession):
        self.force = self.chiffre_aléatoire()
        self.agilité = self.chiffre_aléatoire()
        self.constitution = self.chiffre_aléatoire()
        self.intelligence = self.chiffre_aléatoire()
        self.sagesse = self.chiffre_aléatoire()
        self.charisme = self.chiffre_aléatoire()
        self.armure = random.randint(1,12)
        self.nom = nom
        self.race = race
        self.pv = random.randint(1,20)
        self.profession = profession

    def afficher_caractéristiques(self):
        print('force=', self.force)
        print('agilité=', self.agilité)
        print('constitution=', self.constitution)
        print('intelligence=', self.intelligence)
        print('sagesse=', self.sagesse)
        print('charisme=', self.charisme)
        print('armure=', self.armure)
        print('nom=', self.nom)
        print('race=', self.race)
        print('point de vie=', self.pv)
        print('profession=', self.profession)

class Kobold(NPC):
    def __init__(self):
        super.__init__()

    def attaquer(self, cible):
        pass

    def subir_dommage(self, dommage):
        self.pv -= dommage-self.armure

class Héros(NPC):
    def __init__(self):
        super.__init__()

    def attaquer(self, cible):
        attaque = random.randint(1,20)
        if attaque == 20:
            cible.subir_dommage(random.randint(1,8))
        elif attaque == 1:
            pass
        elif attaque == random.randint(2,19):
            if self.attaque >= cible.armure:
                cible.subir_dommage()
            elif self.attaque <= cible.armure:
                pass

    def subir_dommage(self, dommage):
        self.dommage = random.randint(1, 6)

#ca devrait marcher