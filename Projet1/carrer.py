from turtle import Turtle
class Carrer():
    def __init__(self,point,dx,dy,forme, couleur):
        self.point=point
        self.forme=forme
        self.couleur=couleur
        self.dx=dx
        self.dy=dy
    def update(self):
        self.point.x+=self.dx
        self.point.y+=self.dy

    def dessiner(self,crayon:Turtle):
        crayon.goto(self.point.x, self.point.y)
        crayon.shape(self.forme)
        crayon.color(self.couleur)
        crayon.stamp()