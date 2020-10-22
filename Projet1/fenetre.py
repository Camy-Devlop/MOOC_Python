from turtle import Screen, Turtle

class Fenetre():
    def __init__(self,longueur,largeur,couleur_bg,titre):
        self.f=Screen()
        self.f.bgcolor(couleur_bg)
        self.f.title(titre)
        self.f.setup(longueur,largeur)
        self.f.tracer(0)
        self.crayon=Turtle()
        self.crayon.speed(0)
        self.list_objet = []
        self.f.window_height()
        self.f.window_width()

    def add_objet(self, objet):
        self.list_objet.append(objet)

    def dessiner(self):
        while True:
            self.crayon.clear()
            self.crayon.penup()
            for j in self.list_objet:

                j.update()

                j.dessiner(self.crayon)

            self.f.update()


