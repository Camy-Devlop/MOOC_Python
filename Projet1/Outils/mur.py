from Outils.debut_code import *


class Mur(Carrer):
    """
      Auteur: ISMAIL ADBAIBI
      date : 15/10/2020
      But du programme :
      :class: la classe Mur permet de cree un mur avec toute les classe
              quelle hérite la classe Carrer et Crayon

    """

    def __init__(self, point, coter, dx, dy):
        """
            :param point: Class Point donne la coordonné du mur
            :param coter: la longueur du morceau de mur
            :param dx:
            :param dy:

            """
        super().__init__(point, coter, dx, dy, COULEUR_MUR)
        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()

    def update(self):
        """
        :methods update: methode qui permet de mettre à jour les donne
                        elle va position le mur a la nouvelle coordonné
                        et le redessiner si la couleur a changer aussi


        """
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()