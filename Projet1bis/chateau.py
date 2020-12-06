"""
    Auteur: ISMAIL ADBAIBI
    date : 15/10/2020
    test git
"""
from turtle import textinput as demander
import turtle
from turtle import Turtle
from CONFIGS import *

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

class Carrer(Point):
    """
    Auteur: ISMAIL ADBAIBI
    date : 15/10/2020
    But du programme :
    :class Carrer: la classe Carrer permet de dessiner un carré avec une longeur donner
                   donne en argumentn et avec un couleur et une position donnée
                   c'est une classe qui herite de la classe Point

    """

    def __init__(self, point: Point, coter, dx, dy, couleur):
        """

        :param point: coordonne du carre le point coter inferieur gauche du carré class Point
        :param coter: la longeur du coté
        :param dx:
        :param dy:
        :param couleur: la couleur du carrer
        """

        self.forme = "square"
        super().__init__(coord=point)
        self.couleur = couleur
        self.coter = coter
        self.dx = dx
        self.dy = dy

    def trace_case(self, crayon: Turtle):
        """
        :methods trace_case: il va dessiner le carré
        :param crayon: il recoit class qui appartient a turtle qui va dessiner  le carré
        """
        crayon.penup()
        crayon.goto(super().point)
        crayon.pendown()
        crayon.color(self.couleur)
        crayon.begin_fill()
        for i in range(4):
            crayon.forward(self.coter)
            crayon.left(-90)
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
        :param new_point: elle recoi en argument coord qui est un tuple de deux entier x,y
        """
        self.point = new_point

    def new_couleur(self, nouvealle_couleur):
        """
        :methods new_couleur : est une methode qui modifier la couleur
        :param nouvealle_couleur: elle recoi en parlametre nouvelle couleur qui est str
        """
        self.couleur = nouvealle_couleur

class Cercle(Point):
    """
    Auteur: ISMAIL ADBAIBI
    date : 15/10/2020
    But du programme :
    :class Carrer: la classe Carrer permet de dessiner un carré avec une longeur donner
                   donne en argumentn et avec un couleur et une position donnée
                   c'est une classe qui herite de la classe Point

    """

    def __init__(self, point: Point, coter, dx, dy, couleur):
        """

        :param point: coordonne du carre le point coter inferieur gauche du carré class                Point
        :param coter: la longeur du coté
        :param dx:
        :param dy:
        :param couleur: la couleur du carrer
        """
        self.forme = "square"
        super().__init__(coord=point)
        self.couleur = couleur
        self.coter = coter
        self.dx = dx
        self.dy = dy

    def trace_case(self, crayon: Turtle):
        """
        :methods trace_case: fonction qui va tracer la forme de classe
        :param crayon: outil qui va dessiner la forme
        """
        crayon.penup()
        crayon.goto(super().point)
        crayon.pendown()
        crayon.dot(self.coter, self.couleur)
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

class Crayon():
    """
    Auteur: ISMAIL ADBAIBI
    date : 15/10/2020
    But du programme :
    :class Crayon: la classe Crayon permet de dessiner la frome demander avec une longeur donner
                   donne en argumentn et avec un couleur et une position donnée
                   c'est une classe qui herite de la classe Point

        """
    def __init__(self):
        self.crayon=turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()


    def update(self):
        self.crayon.penup()
        super().dessiner(self.crayon)
        self.crayon.penup()

class Couloir(Carrer):
    def __init__(self, point, coter, dx, dy):
        super().__init__(point, coter, dx, dy, COULEUR_COULOIR)
        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()

    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()

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

class Objet(Carrer):
    def __init__(self, point, coter, dx, dy,message:str):
        super().__init__(point, coter, dx, dy, COULEUR_OBJET)
        self.message=message
        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()

    def get_message(self)->str:
        return self.message

    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()

class Question():

    def __init__(self,sujet:tuple):
        self.question=sujet[0]
        self.reponce=sujet[1]

    def poser_question(self):
        if demander("Question",self.question)==self.reponce:
            turtle.listen()
            return True
        else:
            turtle.listen()
            return False

    def __str__(self):
        return "Question ?"
#TODO:faire documentation
class Porte(Carrer, Question):
    """

    """
    def __init__(self, point, coter, dx, dy, ques:tuple):
        Carrer.__init__(self,point, coter, dx, dy, COULEUR_PORTE)
        Question.__init__(self,ques)
        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()

    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()

class Porte_sortie(Carrer):
    def __init__(self, point, coter, dx, dy):
        super().__init__( point, coter, dx, dy, COULEUR_PORTE)

        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.update()

    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()

class Chateau():
    """
      Auteur: ISMAIL ADBAIBI
      date : 15/10/2020
      But du programme :
      :class Chateau: la classe Chateau permet cree et de dessiner le
                      chateau
    """

    def __init__(self, fichier: str, couleur: list, zone_plan1, zone_plan2):
        """

            :param fichier: l'adressse du fichier pour le dessin du chateau
            :param couleur: liste des couleur des mur et des porte
                            COULEUR_CASES = \'white\'
                            COULEUR_COULOIR = \'white\'
                            COULEUR_MUR = \'grey\'
                            COULEUR_OBJECTIF = \'yellow\'
                            COULEUR_PORTE = \'orange\'
                            COULEUR_OBJET = \'green\'
                            COULEUR_VUE = \'wheat\'
                            COULEURS = [COULEUR_COULOIR, COULEUR_MUR, COULEUR_OBJECTIF, COULEUR_PORTE, COULEUR_OBJET, COULEUR_VUE]
            :param taille_ecran: zone du debut du plan du chateau de type tuple
            """

        self.chateau_str: str = None
        self.couleur = couleur
        self.ZONE_PLAN1: tuple = zone_plan1
        self.ZONE_PLAN2: tuple = zone_plan2
        self.dico_question = self.lire_dico_portes()
        self.dico_objet=self.creer_dictionnaire_des_objets()
        self.matrice = self.lire_matrice(fichier)
        self.COTER = (min(abs(self.ZONE_PLAN1[0]) + abs(self.ZONE_PLAN2[0]),
                          abs(self.ZONE_PLAN1[1]) + abs(self.ZONE_PLAN2[1]))) // max(len(self.matrice),
                                                                                     len(self.matrice[0]))
        self.plan_matrice: list = []
        self.nombre_case_y:int=None
        self.nombre_case_x:int=None

    def lire_matrice(self, fichier) -> list:
        """
          :methode lire_matrice: methode qui va lire un fichier qui contient le plan du chateau
          :param fichier: l'adresse ou se trouve le fichier qui contient le plan
        """
        chateau_str: str = ""
        matrice: list

        with open(fichier, "r", encoding="utf-8") as lecture:
            chateau_str = lecture.read()
        matrice = chateau_str.split('\n')  # il va crée les ligne de la matrice

        for v, i in enumerate(
                matrice):  # en soit il va cree les colone grace au ligne on utilise fonction enumeratepour les
            matrice[v] = i.split(" ")
            tmp_list = []
            for j in matrice[v]:
                tmp_list.append(int(j))
            matrice[v] = tmp_list
        self.nombre_case_x=len(matrice[0])
        self.nombre_case_y = len(matrice)
        return matrice

    def afficher_plan(self, matrice=[]):
        """
        :methods afficher_plan: methode qui va se charger de constrire le cheateau garce a la matrice recu en paaramter
        :param matrice: paramtre que recoi la methode afficher_plan est un tableau
                        de matricr n x m contenant des valeur de 0 à 4

        """

        tb_tmp = []
        tmp_x = self.ZONE_PLAN1[0]
        tmp_y = self.ZONE_PLAN2[1]

        for ey, i in enumerate(self.matrice):
            for ex,j in enumerate(i):
                if j == 0:
                    tb_tmp.append(Couloir((tmp_x, tmp_y), self.COTER, 1, 1))
                elif j == 1:
                    tb_tmp.append(Mur((tmp_x, tmp_y), self.COTER, 1, 1))
                elif j == 2:
                    tb_tmp.append(Porte_sortie((tmp_x, tmp_y), self.COTER, 1, 1))
                elif j == 3:
                    tb_tmp.append(Porte((tmp_x, tmp_y), self.COTER, 1, 1, self.dico_question[(ey, ex)]))
                elif j == 4:
                    tb_tmp.append(Objet((tmp_x, tmp_y), self.COTER, 1, 1,self.dico_objet[(ey, ex)]))
                tmp_x += self.COTER + 1
            self.plan_matrice.append(tb_tmp)
            tb_tmp = []
            tmp_y -= self.COTER + 1
            tmp_x = -240


    def update(self):  # TODO: afaire pour le depalcement du chateau
        pass

    def get_chateau(self) -> list:
        return self.plan_matrice

    def get_coter(self):
        return self.COTER

    def lire_dico_portes(self) -> dict:

        #from CONFIGS import fichier_questions
        memoire_qr = ""
        import io
        d:str
        with open(fichier_questions, "r", encoding="utf-8") as lec:
            d = lec.read()
        f = d.strip('\n')

        f = f.split("\n")

        f_dico = dict()
        for v in f:
            d1, d2 = v.split("),")
            d1 = d1[1:]
            d1 = d1.split(",")
            d1 = (int(d1[0]), int(d1[1]))

            d2=d2.strip(" ")
            if len(d2.split("',")) == 2:
                d2 = d2.split("',")
            else:
                d2 = d2.split("\",")

            d2[0] = d2[0].strip(" ('\"")
            d2[1] = d2[1].strip(" \'")
            d2[1] = d2[1].strip(")")
            d2[1] = d2[1].strip(" '")
            f_dico[d1] = (d2[0], d2[1])
        return f_dico

    def creer_dictionnaire_des_objets(self) -> dict:
        #TODO:j'ai pas fini le trètement pour les objets
        #from CONFIGS import fichier_questions

        d:str
        with open(fichier_objets, "r", encoding="utf-8") as lec:
            d = lec.read()
        f = d.strip('\n')
        f = f.split("\n")
        f_dico = dict()
        for v in f:
            d1, d2 = v.split("),")
            d1 = d1[1:]
            d1 = d1.split(",")
            d1 = (int(d1[0]), int(d1[1]))
            d2=d2.strip(" ")
            d2 = d2[1:len(d2)-1]
            f_dico[d1] = d2
        return f_dico

class Annonceur(Point):
    """
    Auteur: ISMAIL ADBAIBI
    date : 15/11/2020
    But du programme :
    :class Annonceur: la classe Annonceur permet d'ecrie du texte donner
                   donne en argumentn message et avec en standard couleur noir et une position donnée
                   dans le fichier CONFIGS.py dans la constante POINT_AFFICHAGE_ANNONCES
                   c'est une classe qui herite de la classe Point

    """
    def __init__(self):
        super().__init__(coord=(POINT_AFFICHAGE_ANNONCES[0],POINT_AFFICHAGE_ANNONCES[1]-15))
        self.font_police:str="arial"
        self.taille_police:int=12
        self.type_police:str="normal"
        self.COULEUR_POLICE:str="black"
        self.message_debut="bonjour bienvenue dans mon jeux amusez vous bien !!!!! "
        self.crayon=Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.crayon.penup()
        self.crayon.goto(super().point)
        self.crayon.pendown()
        self.crayon.write(self.message_debut,font=(self.font_police,self.taille_police,self.type_police))

    def affiche_nouveau_message(self,message:str):
        """
        :methods affiche_nouveau_message: permet d'afficher le massage
        :param message: variable str qui permet de tdeterminer quelle texte a afficher
        :return: ne retourne rien
        """
        self.efface_annonce()# il va effacer le texte avant d'afficher le texte voulue
        self.crayon.penup()
        self.crayon.goto(super().point[0] - 4, super().point[1])
        self.crayon.pendown()
        self.crayon.color(self.COULEUR_POLICE)
        self.crayon.write(message,font=(self.font_police,self.taille_police,self.type_police))

    def efface_annonce(self):
        """
        :methods efface_annonce: permet d'affacer le texte qui afficher

        """
        self.crayon.penup()
        self.crayon.goto(super().point[0]-4,super().point[1])
        self.crayon.pendown()
        self.crayon.color(COULEUR_EXTERIEUR)
        self.crayon.begin_fill()
        test=False
        for i in range(4):
            if test==False:
                self.crayon.forward(ZONE_PLAN_MINI[0]*-2)
                test=True
            else:
                self.crayon.forward(30)
                test=False
            self.crayon.left(90)
        self.crayon.end_fill()
        self.crayon.penup()

class Inventaire(Point):
    """
    Auteur: ISMAIL ADBAIBI
    date : 15/11/2020
    But du programme :
    :class Inventaire: ajouter des objets trouver par le joueur
    """
    def __init__(self):
        """
        inisialisation de la classe Inventaire
        """
        super().__init__(coord=POINT_AFFICHAGE_INVENTAIRE)
        self.font_police: str = "arial"
        self.taille_police: int = 12
        self.type_police: str = "normal"
        self.COULEUR_POLICE: str = "black"
        self.message_debut = "Invantaire"
        self.crayon = Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.crayon.penup()
        self.crayon.goto(super().point)
        self.crayon.pendown()
        self.crayon.write(self.message_debut, font=(self.font_police, self.taille_police, self.type_police))
        self.cpt:int=0
        self.objet:list=list()

    def affichage_inventaire(self):
        self.crayon.penup()

        x,y=super().point
        print(x, y)
        y-=10
        self.point=(x,y)

        print(super().point)
        self.crayon.goto(super().point)
        self.crayon.pendown()
        self.cpt+=1
        self.crayon.write("N°{0}: {1}".format(self.cpt, self.objet[self.cpt-1]))


    def get_nombre_objet(self)->int:
        """
        :methods get_nombre_objet: retourne le nombre d'objet trouver
        :return: return un entier nombre d'abjet dans le set
        """
        return len(self.objet)

    def set_objet(self,objet):
        """
        :methods set_objet:permet d'ajouter un objet trouver par le joueur pas de doublons
        :param objet: objet trouver

        """
        self.objet.append(objet)
        self.affichage_inventaire()


class Joueur(Cercle):
    """
    Auteur: ISMAIL ADBAIBI
    date : 15/11/2020
    But du programme :
    :class Inventaire: Joueur est le joueur qui va evoluer dans le chateau

    """
    def __init__(self, coord: tuple, coter: int):
        """

        :param coord: c'est les coordonne du joueur ou se trouvre l'entre du chateau
        :param coter: c'est le diametre du cercle elle depent de la taille du carrer pour qu'il
                      se positionne bien au centre du carrer
        """
        super().__init__(coord, coter, 1, 1, COULEUR_PERSONNAGE)
        self.inventaire=Inventaire()
        self.annonceur=Annonceur()
        self.coordoner_tableau:tuple=[1,0]
        self.plan_ch: list
        self.ecoute = turtle.Screen()
        self.crayon = turtle.Turtle()
        self.crayon.hideturtle()
        self.crayon.speed(0)
        self.dx = coter  # permet de faire un placement de 10 pixelle en x
        self.dy = coter
        self.ecoute.listen()
        self.ecoute.onkeypress(self.deplacer_left, "Left")
        self.ecoute.onkeypress(self.deplacer_right, "Right")
        self.ecoute.onkeypress(self.deplacer_up, "Up")
        self.ecoute.onkeypress(self.deplacer_down, "Down")
        self.nombre_objet_a_trouver:int=None
        self.update()
        
    def update(self):
        """
        :methods update:va actualiser les donne et redessiner
        :return:
        """
        self.trace_case(self.crayon)
    def nombre_objet_a_trouvers(self,n:int):
        """
        :methods nombre_objet_a_trouvers:permet de savoir combien d'objet nous devons trouver
        :param n: le nombre d'objet sur le chateau
        """
        self.nombre_objet_a_trouver=n
    def set_plan_chateau(self, p):
        """
        :methods set_plan_chateau:le plant du chateah sout la forme d'une matrice deux d
        :param p: la matrice
        """
        self.plan_ch = p

    def d_left(self):
        """
        :methods d_left:va faire deplace le joueur vers la gauche
        """
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x - self.dx - 1, y)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()

    def d_right(self):
        """
        :methods d_right:va faire deplace le joueur vers la droite
        """
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x + self.dx + 1, y)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()

    def d_up(self):
        """
        :methods d_up:va faire deplace le joueur vers le haut
        """
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x, y + self.dy + 1)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()

    def d_down(self):
        """
        :methods d_down:va faire deplace le joueur vers le bas
        """
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x, y - self.dx - 1)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()

    def new_couleur(self, nouvelle_couleur):
        """
        :methods new_couleur: va permetre de changer la couleur du joueur
        :param nouvelle_couleur: argument de type str qui recoye la couleur en anglaid
        """
        super().new_couleur(nouvelle_couleur)

    def deplacer(self, matrice: list, position: tuple, mouvement):
        """
        :methods deplacer:fonction qui va verifier sur le matrice si le deplace respecter les condition
        :param matrice: le plan du chateau
        :param position:
        :param mouvement: le sens de deplacement du joueur
        """

        if mouvement == "droite":

            x = self.coordoner_tableau[0]
            y = self.coordoner_tableau[1]


            if x<len(self.plan_ch[0]):
                if self.plan_ch[y][x + 1].__class__ in [Couloir.__mro__[0], Objet.__mro__[0],Porte.__mro__[0],Porte_sortie.__mro__[0]]:
                    if self.plan_ch[y][x + 1].__class__ == Couloir.__mro__[0]:
                        self.coordoner_tableau[0]+=1
                        self.d_right()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()
                    elif self.plan_ch[y][x + 1].__class__ == Objet.__mro__[0]:
                        self.coordoner_tableau[0] += 1
                        self.d_right()
                        self.inventaire.set_objet(self.plan_ch[y][x+1].get_message())
                        self.annonceur.affiche_nouveau_message("Vous avez trouvez un nouvelle Objet "+self.plan_ch[y][x+1].get_message())
                        self.plan_ch[y][x+1]=Couloir(self.plan_ch[y][x+1].position,self.plan_ch[y][x+1].coter,1,1)
                        self.plan_ch[y][x + 1].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x + 1].update()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()
                    elif self.plan_ch[y][x + 1].__class__ == Porte.__mro__[0]:
                        self.annonceur.affiche_nouveau_message("Porte est fermer !!!!")
                        if self.plan_ch[y][x + 1].poser_question():
                            self.annonceur.affiche_nouveau_message("Ouverture de porte")
                            self.coordoner_tableau[0] += 1
                            self.d_right()
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.plan_ch[y][x + 1] = Couloir(self.plan_ch[y][x + 1].position,self.plan_ch[y][x + 1].coter, 1, 1)
                            self.plan_ch[y][x + 1].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x + 1].update()
                            self.update()
                        else:
                            self.annonceur.affiche_nouveau_message("Porte est fermer !!!!")
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.update()
                    elif self.plan_ch[y][x + 1].__class__ == Porte_sortie.__mro__[0]:
                        if self.inventaire.get_nombre_objet()==self.nombre_objet_a_trouver:
                            self.coordoner_tableau[0] += 1
                            self.d_right()
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.plan_ch[y][x].update()
                            self.update()
                            self.annonceur.affiche_nouveau_message("Bravo, Vous avez gagner!!!!!")
                            for i in range(1000000):#pour pas que la fenetre se referme directement
                                pass
                            exit(0)
                        else:
                            self.annonceur.affiche_nouveau_message("Vous avez pas trouver tout les objets!!!!!")

        elif mouvement == "gauche":

            x = self.coordoner_tableau[0]
            y = self.coordoner_tableau[1]

            if x>=1:
                if self.plan_ch[y][x - 1].__class__ in [Couloir.__mro__[0], Objet.__mro__[0],Porte.__mro__[0],Porte_sortie.__mro__[0]]:
                    if self.plan_ch[y][x - 1].__class__ == Couloir.__mro__[0]:
                        self.coordoner_tableau[0] -= 1
                        self.d_left()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()

                    elif self.plan_ch[y][x - 1].__class__ == Objet.__mro__[0]:
                        self.coordoner_tableau[0] -= 1
                        self.d_left()
                        self.inventaire.set_objet(self.plan_ch[y][x - 1].get_message())
                        self.annonceur.affiche_nouveau_message(
                            "Vous avez trouvez un nouvelle Objet " + self.plan_ch[y][x - 1].get_message())
                        self.plan_ch[y][x - 1] = Couloir(self.plan_ch[y][x - 1].position, self.plan_ch[y][x - 1].coter,1, 1)
                        self.plan_ch[y][x - 1].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x - 1].update()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()

                    elif self.plan_ch[y][x - 1].__class__ == Porte.__mro__[0]:
                        self.annonceur.affiche_nouveau_message("Porte est fermer !!!!")
                        if self.plan_ch[y][x - 1].poser_question():
                            self.annonceur.affiche_nouveau_message("Ouverture de porte")
                            self.coordoner_tableau[0] -= 1
                            self.d_left()
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.plan_ch[y][x - 1] = Couloir(self.plan_ch[y][x - 1].position, self.plan_ch[y][x - 1].coter, 1, 1)
                            self.plan_ch[y][x - 1].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x - 1].update()
                            self.update()

                        else:
                            self.annonceur.affiche_nouveau_message("Porte est fermer !!!!")
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.update()

                    elif self.plan_ch[y][x - 1].__class__ == Porte_sortie.__mro__[0]:
                        if self.inventaire.get_nombre_objet() == self.nombre_objet_a_trouver:
                            self.coordoner_tableau[0] -= 1
                            self.d_left()
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.plan_ch[y][x].update()
                            self.plan_ch[y][x - 1] = Couloir(self.plan_ch[y][x - 1].position,self.plan_ch[y][x - 1].coter, 1, 1)
                            self.plan_ch[y][x - 1].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x - 1].update()
                            self.update()
                            self.annonceur.affiche_nouveau_message("Bravo, Vous avez gagner!!!!!")
                            for i in range(1000000):#pour pas que la fenetre se referme directement
                                pass
                            exit(0)
                        else:
                            self.annonceur.affiche_nouveau_message("Vous avez pas trouver tout les objets!!!!!")

        elif mouvement == "haut":

            x = self.coordoner_tableau[0]
            y = self.coordoner_tableau[1]

            if y>=0:
                if self.plan_ch[y - 1][x].__class__ in [Couloir.__mro__[0], Objet.__mro__[0], Porte.__mro__[0], Porte_sortie.__mro__[0]]:
                    if self.plan_ch[y - 1][x].__class__ == Couloir.__mro__[0]:
                        self.coordoner_tableau[1] -= 1
                        self.d_up()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()

                    elif self.plan_ch[y - 1][x].__class__ == Objet.__mro__[0]:
                        self.coordoner_tableau[1] -= 1
                        self.d_up()
                        self.inventaire.set_objet(self.plan_ch[y - 1][x].get_message())
                        self.annonceur.affiche_nouveau_message(
                            "Vous avez trouvez un nouvelle Objet " + self.plan_ch[y - 1][x].get_message())
                        self.plan_ch[y - 1][x] = Couloir(self.plan_ch[y - 1][x].position, self.plan_ch[y][x].coter,1, 1)
                        self.plan_ch[y - 1][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y - 1][x].update()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()

                    elif self.plan_ch[y - 1][x].__class__ == Porte.__mro__[0]:
                        self.annonceur.affiche_nouveau_message("Porte est fermer !!!!")
                        if self.plan_ch[y - 1][x].poser_question():
                            self.coordoner_tableau[1] -= 1
                            self.d_up()
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.plan_ch[y - 1][x] = Couloir(self.plan_ch[y - 1][x].position, self.plan_ch[y - 1][x].coter, 1, 1)
                            self.plan_ch[y - 1][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y - 1][x].update()
                            self.update()

                        else:
                            self.annonceur.affiche_nouveau_message("Porte est fermer !!!!")
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.update()

                    elif self.plan_ch[y - 1][x].__class__ == Porte_sortie.__mro__[0]:

                        if self.inventaire.get_nombre_objet() == self.nombre_objet_a_trouver:
                            self.coordoner_tableau[1] -= 1
                            self.d_up()
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y - 1][x] = Couloir(self.plan_ch[y - 1][x].position,self.plan_ch[y - 1][x].coter, 1, 1)
                            self.plan_ch[y - 1][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y - 1][x].update()
                            self.update()
                            self.annonceur.affiche_nouveau_message("Bravo, Vous avez gagner!!!!!")
                            for i in range(1000000):#pour pas que la fenetre se referme directement
                                pass
                            exit(0)
                        else:
                            self.annonceur.affiche_nouveau_message("Vous avez pas trouver tout les objets!!!!!")

        elif mouvement == "bas":

            x = self.coordoner_tableau[0]
            y = self.coordoner_tableau[1]


            if y<=len(self.plan_ch)+1:
                if self.plan_ch[y+1][x].__class__ in [ Couloir.__mro__[0],Objet.__mro__[0],Porte.__mro__[0],Porte_sortie.__mro__[0]]:
                    if self.plan_ch[y+1][x].__class__==Couloir.__mro__[0]:
                        self.coordoner_tableau[1]+=1
                        self.d_down()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()

                    elif self.plan_ch[y + 1][x].__class__==Objet.__mro__[0]:
                        self.coordoner_tableau[1] += 1
                        self.d_down()
                        self.inventaire.set_objet(self.plan_ch[y + 1][x].get_message())
                        self.annonceur.affiche_nouveau_message("Vous avez trouvez un nouvelle Objet "+self.plan_ch[y + 1][x].get_message())
                        self.plan_ch[y + 1][x] = Couloir(self.plan_ch[y + 1][x].position, self.plan_ch[y + 1][x].coter,1, 1)
                        self.plan_ch[y + 1][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y + 1][x].update()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()

                    elif self.plan_ch[y + 1][x].__class__==Porte.__mro__[0]:
                        self.annonceur.affiche_nouveau_message("Porte est fermer !!!!")
                        if self.plan_ch[y + 1][x].poser_question():
                            self.coordoner_tableau[1] += 1
                            self.d_down()
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.plan_ch[y][x].update()
                            self.plan_ch[y + 1][x] = Couloir(self.plan_ch[y + 1][x].position, self.plan_ch[y + 1][x].coter,1, 1)
                            self.plan_ch[y + 1][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y + 1][x].update()
                            self.update()
                        else:
                            self.annonceur.affiche_nouveau_message("Porte est fermer !!!!")
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.update()

                    elif self.plan_ch[y + 1][x].__class__ == Porte_sortie.__mro__[0]:

                        if self.inventaire.get_nombre_objet() == self.nombre_objet_a_trouver:
                            self.coordoner_tableau[1] += 1
                            self.d_down()
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.plan_ch[y][x].update()
                            self.plan_ch[y + 1][x] = Couloir(self.plan_ch[y + 1][x].position, self.plan_ch[y + 1][x].coter, 1, 1)
                            self.plan_ch[y + 1][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y + 1][x].update()
                            self.update()
                            self.update()
                            self.annonceur.affiche_nouveau_message("Bravo, Vous avez gagner!!!!!")
                            for i in range(1000000):#pour pas que la fenetre se referme directement
                                pass
                            exit(0)
                        else:
                            self.annonceur.affiche_nouveau_message("Vous avez pas trouver tout les objets!!!!!")

    def deplacer_right(self):
        """
        :methods deplacer_right:va faire la demande de direction a droite

        """
        self.ecoute.onkeypress(None, "Right")
        self.deplacer(self.plan_ch, self.position, "droite")
        self.ecoute.onkeypress(self.deplacer_right, "Right")

    def deplacer_left(self):
        """
        :methods deplacer_left:va faire la demande de direction a gauche

        """
        self.ecoute.onkeypress(None, "Left")
        self.deplacer(self.plan_ch, self.position, "gauche")
        self.ecoute.onkeypress(self.deplacer_left, "Left")

    def deplacer_up(self):
        """
        :methods deplacer_up:va faire la demande de direction en haut

        """
        self.ecoute.onkeypress(None, "Up")
        self.deplacer(self.plan_ch, self.position, "haut")
        self.ecoute.onkeypress(self.deplacer_up, "Up")

    def deplacer_down(self):
        """
        :methods deplacer_down:va faire la demande de direction en bas
        """
        self.ecoute.onkeypress(None, "Down")
        self.deplacer(self.plan_ch, self.position, "bas")
        self.ecoute.onkeypress(self.deplacer_down, "Down")

chateau = Chateau(fichier_plan, COULEURS, ZONE_PLAN_MINI, ZONE_PLAN_MAXI)
hauteur, largeur = ZONE_PLAN_MINI
p = turtle

p.Screen()
p.setup((hauteur * -2)+20, (largeur * -2+20))
chateau.afficher_plan()
p1 = Joueur((chateau.get_chateau()[0][1].position[0]+(chateau.get_coter()//2),chateau.get_chateau()[0][1].position[1]-(chateau.get_coter()//2)),chateau.get_coter())
p1.set_plan_chateau(chateau.get_chateau())
p1.nombre_objet_a_trouvers(len(chateau.dico_objet))
p1.ecoute.mainloop()
p.listen()
