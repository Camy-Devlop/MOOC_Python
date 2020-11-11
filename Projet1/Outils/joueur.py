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

    def d_left(self):
        self.ecoute.onkeypress(None, "Left")
        if self.deplacer(self.plan_ch, self.position):
            x, y = self.position
            print(type(self.plan_ch[celulle[0]][celulle[1]]))
            print("celulle ", celulle, " joueur", self.position)
            self.new_couleur(COULEUR_VUE)
            self.update()
            self.position = (x - self.dx - 1, y)
            self.new_couleur(COULEUR_PERSONNAGE)
            self.update()
        self.ecoute.onkeypress(self.deplacer_left, "Left")

    def set_plan_chateau(self, p):
        self.plan_ch = p

    def d_right(self):
        self.ecoute.onkeypress(None, "Right")
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x + self.dx + 1, y)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()
        self.ecoute.onkeypress(self.deplacer_right, "Right")

    def d_up(self):
        self.ecoute.onkeypress(None, "Up")
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x, y + self.dy + 1)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()
        self.ecoute.onkeypress(self.deplacer_up, "Up")

    def d_down(self):
        self.ecoute.onkeypress(None, "Down")
        x, y = self.position

        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x, y - self.dx - 1)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()
        self.ecoute.onkeypress(self.deplacer_down, "Down")

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
        self.deplacer(self.plan_ch, self.position, "droite")

    def deplacer_left(self):
        self.deplacer(self.plan_ch, self.position, "gauche")

    def deplacer_up(self):
        self.deplacer(self.plan_ch, self.position, "haut")

    def deplacer_down(self):
        self.deplacer(self.plan_ch, self.position, "bas")