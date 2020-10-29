from Outils.debut_code import *


class Mur(Carrer, Crayon):
    def __init__(self, point, coter, dx, dy, forme):
        """

        :param point:
        :param coter:
        :param dx:
        :param dy:
        :param forme:
        """
        super().__init__(point, coter, dx, dy, forme, COULEUR_MUR)

        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()

        # self.porte=CONFIGS.COULEURS.COULEUR_PORTE

    def update(self):
        """

        :return:
        """
        self.crayon.penup()
        super().dessiner(self.crayon)
        self.crayon.penup()