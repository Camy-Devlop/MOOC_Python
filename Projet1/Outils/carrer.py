from turtle import Turtle
class Carrer():
    def __init__(self,point,dx,dy,forme, couleur):
        self.point=point
        self.forme=forme
        self.couleur=couleur
        self.dx=dx
        self.dy=dy
    def update(self,borneh,bornel):
        if borneh // 2 < self.point.x:
            self.dx = self.dx * (-1)
        if bornel // 2 < self.point.y:
            self.dy = self.dy * (-1)

        if self.point.x < -(bornel // 2):
            self.dx = self.dx * (-1)
        if self.point.y < -(borneh // 2):
            self.dy = self.dy * (-1)

        self.point.x += self.dx
        self.point.y += self.dy

    def dessiner(self,crayon:Turtle):
        crayon.goto(self.point.x, self.point.y)
        crayon.shape(self.forme)
        crayon.color(self.couleur)
        crayon.stamp()