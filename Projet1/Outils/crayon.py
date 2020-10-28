import turtle

class Crayon():

  def __init__(self):
    self.crayon=turtle.Turtle()
    self.crayon.hideturtle()
    self.crayon.speed(0)
    self.update()
    #self.porte=CONFIGS.COULEURS.COULEUR_PORTE

  def update(self):
    self.crayon.penup()
    super().dessiner(self.crayon)
    self.crayon.penup()