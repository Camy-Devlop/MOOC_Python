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
        self.dessiner_Bar(crayon)
        crayon.goto(self.point.x, self.point.y)
        crayon.shape(self.forme)
        crayon.color(self.couleur)
        crayon.stamp()


    def dessiner_Bar(self, crayon: Turtle):
        crayon.shapesize(0.02,1.5,None)
        crayon.shape("square")
        crayon.goto(self.point.x, self.point.y+20)
        crayon.color("white")
        crayon.width(30)
        #crayon.shape(self.forme)
        crayon.pendown()
        crayon.setheading(0)
        crayon.stamp()
        crayon.shapesize(1.0, 1.0, None)
        crayon.penup()
