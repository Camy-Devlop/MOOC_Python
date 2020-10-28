class Point():
    """
      Auteur: ISMAIL ADBAIBI
      date : 15/10/2020
      But du programme :
      :class: la classe point permet connaitre les coordonner d'un point
            elle peut recevoir plusieur parametre coordonner a deux entier,
            ou un tuple a deux entier

      :param x : x entier pour l'axe des ordoners
    """

    def __init__(self, x=None, y=None, coord=None):
        """
            :init:constructeur class Point
            :param x: x valeur entier pour l'ordonner de l'axe des x
            :param y: y valeur entier pour l'absise de l'axe des y
            :param coord: coord est tuple avec deux entiers x et y
            """

        if x != None and y != None:  # verifier si la valeur a ete donne doit etre diffier de null
            self.x = x
            self.y = y
        elif coord != None:  # verifier si l'argument n'es pas null
            if not isinstance(coord, tuple):
                self.x, self.y = coord.point
            else:
                self.x, self.y = coord
        else:  # si les deux argument sont null x et y et l'argument coord aussi alors il
            # donne x, y vaut 0,0
            self.x = 0
            self.y = 0

    @property
    def point(self):
        """
          :methods point : est une  methode getteur retourne la coordonne du point
          :return: returne un tuple de x et y
          """

        return (self.x, self.y)

    @point.setter
    def point(self, coord: tuple):
        """
            :methods point : est une methode qui modifier les valeur x et y
            :param coord: elle recoi en parlametre coord qui est un tuple de deux entier x,y
            """
        self.x, self.y = coord

    def __str__(self):
        """
        :methode __str__: returne un string avec la coordonner du point des deux entier x,y
        :return: coordonne en format string ex: (x,y)
        """
        return "({0},{1})".format(self.x, self.y)
