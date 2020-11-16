from Outils.debut_code import *
from Outils.couloir import Couloir
from Outils.mur import Mur
from Outils.objectif import Objectif
from Outils.objet import Objet
from Outils.porte import Porte
from Outils.vue import Vue


class Joueur(Cercle):
    def __init__(self, coord: tuple, coter: int):
        super().__init__(coord, coter, 1, 1, COULEUR_PERSONNAGE)
        self.plan_ch: list
        self.ecoute = turtle.Screen()
        self.crayon = turtle.Turtle()
        self.crayon.speed(0)
        self.dx = coter  # permet de faire un placement de 10 pixelle en x
        self.dy = coter
        self.ecoute.listen()
        self.ecoute.onkeypress(self.deplacer_left, "Left")
        self.ecoute.onkeypress(self.deplacer_right, "Right")
        self.ecoute.onkeypress(self.deplacer_up, "Up")
        self.ecoute.onkeypress(self.deplacer_down, "Down")
        self.crayon.hideturtle()
        self.update()

    def update(self):
        self.trace_case(self.crayon)

    def set_plan_chateau(self, p):
        self.plan_ch = p

    def d_left(self):
        x, y = self.position
        print(type(self.plan_ch[y][x]))
        print("celulle ", self.plan_ch[y][x], " joueur", self.position)
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x - self.dx - 1, y)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()

    def d_right(self):
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x + self.dx + 1, y)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()

    def d_up(self):
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x, y + self.dy + 1)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()

    def d_down(self):
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x, y - self.dx - 1)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()

    def new_couleur(self, nouvelle_couleur):
        super().new_couleur(nouvelle_couleur)

    def deplacer(self, matrice: list, position: tuple, mouvement) -> bool:

        print("joueur", position)
        if mouvement == "droite":
            longueur = abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])
            hauteur = abs(ZONE_PLAN_MINI[1]) + abs(ZONE_PLAN_MAXI[1])
            print("la longueur", longueur)
            print("la hauteur", hauteur)
            print("la diference x", longueur - abs(position[0]))
            print("la diference y", (hauteur - abs(position[1])))
            x = ((longueur // abs(position[0]))) - 1
            y = ((hauteur // abs(position[1]))) - 1

            if type(self.plan_ch[y][x + 1]) in [Objectif, Porte, Objet]:
                pass  # TODO: les test des objet dans la liste
            print("celulle ", x, y, " joueur", self.position)

        elif mouvement == "gauche":
            longueur = abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])
            hauteur = abs(ZONE_PLAN_MINI[1]) + abs(ZONE_PLAN_MAXI[1])
            x = ((longueur // abs(position[0]))) - 1
            y = ((hauteur // abs(position[1]))) - 1

            if type(self.plan_ch[y][x - 1]) in [Objectif, Porte, Objet, Couloir]:
                pass  # TODO: les test des objet dans la liste
            print("celulle ", x, y, " joueur", self.position)
        elif mouvement == "haut":
            longueur = abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])
            hauteur = abs(ZONE_PLAN_MINI[1]) + abs(ZONE_PLAN_MAXI[1])

            x = ((longueur // abs(position[0]))) - 1
            y = ((hauteur // abs(position[1]))) - 1

            if type(self.plan_ch[y - 1][x]) in [Objectif, Porte, Objet]:
                pass  # TODO: les test des objet dans la liste
            print("celulle ", x, y, " joueur", self.position)
        elif mouvement == "bas":
            longueur = abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])
            hauteur = abs(ZONE_PLAN_MINI[1]) + abs(ZONE_PLAN_MAXI[1])

            x = ((longueur // abs(position[0]))) - 1
            y = ((hauteur // abs(position[1]))) - 1

            if type(self.plan_ch[y + 1][x]) in [Objectif, Porte, Objet]:
                pass  # TODO: les test des objet dans la liste
            print("celulle ", x, y, " joueur", self.position)

    def deplacer_right(self):
        self.ecoute.onkeypress(None, "Right")
        self.deplacer(self.plan_ch, self.position, "droite")
        self.ecoute.onkeypress(self.deplacer_right, "Right")

    def deplacer_left(self):
        self.ecoute.onkeypress(None, "Left")
        self.deplacer(self.plan_ch, self.position, "gauche")
        self.ecoute.onkeypress(self.deplacer_left, "Left")

    def deplacer_up(self):
        self.ecoute.onkeypress(None, "Up")
        self.deplacer(self.plan_ch, self.position, "haut")
        self.ecoute.onkeypress(self.deplacer_up, "Up")

    def deplacer_down(self):
        self.ecoute.onkeypress(None, "Down")
        self.deplacer(self.plan_ch, self.position, "bas")
        self.ecoute.onkeypress(self.deplacer_down, "Down")