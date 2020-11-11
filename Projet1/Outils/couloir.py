from Outils.debut_code import *


class Couloir(Carrer):
    def __init__(self, point, coter, dx, dy):
        super().__init__(point, coter, dx, dy, COULEUR_COULOIR)
        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()

    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()