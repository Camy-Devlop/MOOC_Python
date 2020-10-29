from turtle import Turtle
from Outils.point import Point


class Carrer(Point):
    """
    Auteur: ISMAIL ADBAIBI
    date : 15/10/2020
    But du programme :
    :class Carrer: la classe Carrer permet de dessiner un carré avec une longeur donner
                   donne en argumentn et avec un couleur et une position donnée
                   c'est une classe qui herite de la classe Point

    """

    def __init__(self, point: Point, coter, dx, dy, forme, couleur):
        """

        :param point: coordonne du carre le point coter inferieur gauche du carré class                Point
        :param coter: la longeur du coté
        :param dx:
        :param dy:
        :param forme:
        :param couleur: la couleur du carrer
        """
        super().__init__(coord=point)
        # print(coord)
        self.forme = forme
        self.couleur = couleur
        self.coter = coter
        self.dx = dx
        self.dy = dy

    def dessiner(self, crayon: Turtle):
        """
        :methods dessiner: est une methode qui va dessiner le carrer a la coordonner donne en x et y
        garce la methode turtle qui a été import
        :param crayon: est argument passer du type Turtle qui c'est ui qui va desiner le carrée
        """
        crayon.penup()
        crayon.goto(super().point)
        crayon.pendown()
        crayon.color(self.couleur)
        crayon.begin_fill()
        for i in range(4):
            crayon.forward(self.coter)
            crayon.left(90)
        crayon.end_fill()
        crayon.penup()

    @property
    def position(self):
        """
        :methods position : est une  methode getteur retourne la coordonne du point
        :return: returne un tuple de x et y
        """
        return super().point

    @position.setter
    def position(self, new_point):
        """
        :methods point : est une methode setter qui modifier les valeur x et y
        :param coord: elle recoi en argument coord qui est un tuple de deux entier x,y
        """
        self.point = new_point

    def new_couleur(self, nouvealle_couleur):
        """
        :methods new_couleur : est une methode qui modifier la couleur
        :param new_couleur: elle recoi en parlametre nouvelle couleur qui est str
        """
        self.couleur = nouvealle_couleur