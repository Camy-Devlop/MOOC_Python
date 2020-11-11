from Outils.debut_code import *
from Outils.question import Question


class Porte(Carrer, Question):
    def __init__(self, point, coter, dx, dy, ques:tuple):
        Carrer.__init__(self,point, coter, dx, dy, COULEUR_PORTE)
        Question.__init__(self,ques)
        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()

    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()