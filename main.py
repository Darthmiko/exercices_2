# exercices 2
class NPC:

    def chiffe_aléatoire():
        if
            dé1 + dé2 + dé3 > dé4
        elif
            dé1 + dé3 + dé4 > dé2
        elif
            dé2 + dé3 + dé4 > dé1
        elif
            dé1 + dé2 + dé4 > dé3

    def __init__(self):
        self.force =
        self.agilité =
        self.constitution =
        self.intelligence =
        self.sagesse =
        self.charisme =

    def __init__(self):
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
        self.dommage = random.randint(1,6)

class Héros(NPC):
    def __init__(self):
        super.__init__()

    def attaquer(self, cible):
        pass

    def subir_dommage(self, dommage):
        self.dommage = random.randint(1, 6)
