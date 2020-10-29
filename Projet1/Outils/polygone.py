from Outils.point import Point
from turtle import Turtle
class Polygone(Point):
    
    def __init__(self,couleur,position:tuple,longueur:list,rot:list):
        super(Polygone, self).__init__(position)
        self.couleur=couleur
        self.position=position
        self.longueur:list=longueur
        self.rot=rot
        self.crayon=Turtle()
        
    def dessiner(self):
        self.crayon.speed(0)
        self.crayon.penup()
        self.crayon.goto(self.position)
        self.crayon.color(self.couleur)
        self.crayon.pendown()
        for j,i in enumerate(self.longueur):
            self.crayon.forward(i)
            self.crayon.left(self.rot[j])
            
