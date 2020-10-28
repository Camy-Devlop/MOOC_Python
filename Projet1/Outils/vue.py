from Outils.debut_code import *


class Vue(Carrer):
    def __init__(self, point, coter, dx, dy, forme):
        super().__init__(point, coter, dx, dy, forme, COULEUR_VUE)
        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()

    def update(self):
        self.crayon.penup()
        super().dessiner(self.crayon)
        self.crayon.penup()