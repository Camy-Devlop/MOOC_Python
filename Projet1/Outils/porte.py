from Outils.debut_code import *


class Porte(Carrer):
    def __init__(self, point, coter, dx, dy, forme):
        super().__init__(point, coter, dx, dy, forme, COULEUR_PORTE)
        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()
        # self.porte=CONFIGS.COULEURS.COULEUR_PORTE

    def update(self):
        self.crayon.penup()
        super().dessiner(self.crayon)
        self.crayon.penup()
        