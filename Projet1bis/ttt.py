from turtle import textinput as demander
import turtle
from turtle import Turtle
from CONFIGS import *


class Point():
    def __init__(self, x=None, y=None, coord=None):
        if x != None and y != None:  # verifier si la valeur a ete donne doit etre diffier de null
            self.x = x
            self.y = y
        elif coord != None:  # verifier si l'argument n'es pas null
            if not isinstance(coord, tuple):
                self.x, self.y = coord.point
            else:
                self.x, self.y = coord
        else:  # si les deux argument sont null x et y et l'argument coord aussi alors il # donne x, y vaut 0,0
            self.x = 0
            self.y = 0
    @property
    def point(self):
        return (self.x, self.y)
    @point.setter
    def point(self, coord: tuple):
        self.x, self.y = coord
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
class Carrer(Point):
    def __init__(self, point: Point, coter, dx, dy, couleur):
        self.forme = "square"
        super().__init__(coord=point)
        self.couleur = couleur
        self.coter = coter
        self.dx = dx
        self.dy = dy
    def trace_case(self, crayon: Turtle):
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
        return super().point
    @position.setter
    def position(self, new_point):
        self.point = new_point
    def new_couleur(self, nouvealle_couleur):
        self.couleur = nouvealle_couleur
class Cercle(Point):
    def __init__(self, point: Point, coter, dx, dy, couleur):
        self.forme = "square"
        super().__init__(coord=point)
        self.couleur = couleur
        self.coter = coter
        self.dx = dx
        self.dy = dy
    def trace_case(self, crayon: Turtle):
        crayon.penup()
        crayon.goto(super().point)
        crayon.pendown()
        crayon.dot(self.coter, self.couleur)
        crayon.penup()
    @property
    def position(self):
        return super().point
    @position.setter
    def position(self, new_point):
        self.point = new_point
    def new_couleur(self, nouvealle_couleur):

        self.couleur = nouvealle_couleur
class Crayon():
    def __init__(self):
        self.crayon = tortue
        self.crayon.speed(0)
        self.update()
    def update(self):
        self.crayon.penup()
        super().dessiner(self.crayon)
        self.crayon.penup()
class Couloir(Carrer):
    def __init__(self, point, coter, dx, dy):
        super().__init__(point, coter, dx, dy, COULEUR_COULOIR)
        self.crayon = tortue

        self.crayon.speed(0)
        self.update()
    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()
class Mur(Carrer):
    def __init__(self, point, coter, dx, dy):
        super().__init__(point, coter, dx, dy, COULEUR_MUR)
        self.crayon =tortue

        self.crayon.speed(0)
        self.update()
    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()
class Objet(Carrer):
    def __init__(self, point, coter, dx, dy, message: str):
        super().__init__(point, coter, dx, dy, COULEUR_OBJET)
        self.message = message
        self.crayon =tortue
        self.crayon.speed(0)
        self.update()
    def get_message(self) -> str:
        return self.message
    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()
class Question():
    def __init__(self, sujet: tuple):
        self.question = sujet[0]
        self.reponce = sujet[1]
    def poser_question(self):
        if demander("Question", self.question) == self.reponce:
            turtle.listen()
            return True
        else:
            turtle.listen()
            return False
    def __str__(self):
        return "Question ?"
class Porte(Carrer, Question):
    def __init__(self, point, coter, dx, dy, ques: tuple):
        Carrer.__init__(self, point, coter, dx, dy, COULEUR_PORTE)
        Question.__init__(self, ques)
        self.crayon = tortue
        self.crayon.speed(0)
        self.update()
    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()
class Porte_sortie(Carrer):
    def __init__(self, point, coter, dx, dy):
        super().__init__(point, coter, dx, dy, COULEUR_PORTE)

        self.crayon.speed(0)
        self.update()
    def update(self):
        self.crayon.penup()
        super().trace_case(self.crayon)
        self.crayon.penup()
class Chateau():
    def __init__(self, fichier: str, couleur: list, zone_plan1, zone_plan2):
        self.chateau_str: str = None
        self.couleur = couleur
        self.ZONE_PLAN1: tuple = zone_plan1
        self.ZONE_PLAN2: tuple = zone_plan2
        self.dico_question = self.lire_dico_portes()
        self.dico_objet = self.creer_dictionnaire_des_objets()
        self.matrice = self.lire_matrice(fichier)
        self.COTER = (min(abs(self.ZONE_PLAN1[0]) + abs(self.ZONE_PLAN2[0]),abs(self.ZONE_PLAN1[1]) + abs(self.ZONE_PLAN2[1]))) // max(len(self.matrice),len(self.matrice[0]))
        self.plan_matrice: list = []
        self.nombre_case_y: int = None
        self.nombre_case_x: int = None
    def lire_matrice(self, fichier) -> list:
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
        self.nombre_case_x = len(matrice[0])
        self.nombre_case_y = len(matrice)
        return matrice
    def afficher_plan(self, matrice=[]):
        tb_tmp = []
        tmp_x = self.ZONE_PLAN1[0]
        tmp_y = self.ZONE_PLAN2[1]
        for ey, i in enumerate(self.matrice):
            for ex, j in enumerate(i):
                if j == 0:
                    tb_tmp.append(Couloir((tmp_x, tmp_y), self.COTER, 1, 1))
                elif j == 1:
                    tb_tmp.append(Mur((tmp_x, tmp_y), self.COTER, 1, 1))
                elif j == 2:
                    tb_tmp.append(Porte_sortie((tmp_x, tmp_y), self.COTER, 1, 1))
                elif j == 3:
                    tb_tmp.append(Porte((tmp_x, tmp_y), self.COTER, 1, 1, self.dico_question[(ey, ex)]))
                elif j == 4:
                    tb_tmp.append(Objet((tmp_x, tmp_y), self.COTER, 1, 1, self.dico_objet[(ey, ex)]))
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
        d: str
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
            d2 = d2.strip(" ")
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
        d: str
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
            d2 = d2.strip(" ")
            d2 = d2[1:len(d2) - 1]
            f_dico[d1] = d2
        return f_dico
class Annonceur(Point):
    def __init__(self):
        super().__init__(coord=(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1] - 15))
        self.font_police: str = "arial"
        self.taille_police: int = 12
        self.type_police: str = "normal"
        self.COULEUR_POLICE: str = "black"
        self.message_debut = "bonjour bienvenue dans mon jeux amusez vous bien !!!!! "
        self.crayon = tortue
        self.crayon.speed(0)
        self.crayon.penup()
        self.crayon.goto(super().point)
        self.crayon.pendown()
        self.crayon.write(self.message_debut, font=(self.font_police, self.taille_police, self.type_police))

    def affiche_nouveau_message(self, message: str):
        self.efface_annonce()  # il va effacer le texte avant d'afficher le texte voulue
        self.crayon.penup()
        self.crayon.goto(super().point[0] - 4, super().point[1])
        self.crayon.pendown()
        self.crayon.color(self.COULEUR_POLICE)
        self.crayon.write(message, font=(self.font_police, self.taille_police, self.type_police))
    def efface_annonce(self):
        self.crayon.penup()
        self.crayon.goto(super().point[0] - 4, super().point[1])
        self.crayon.pendown()
        self.crayon.color(COULEUR_EXTERIEUR)
        self.crayon.begin_fill()
        test = False
        for i in range(4):
            if test == False:
                self.crayon.forward(ZONE_PLAN_MINI[0] * -2)
                test = True
            else:
                self.crayon.forward(30)
                test = False
            self.crayon.left(90)
        self.crayon.end_fill()
        self.crayon.penup()
class Inventaire(Point):
    def __init__(self):
        super().__init__(coord=POINT_AFFICHAGE_INVENTAIRE)
        self.font_police: str = "arial"
        self.taille_police: int = 12
        self.type_police: str = "normal"
        self.COULEUR_POLICE: str = "black"
        self.message_debut = "Invantaire"
        self.crayon = tortue

        self.crayon.speed(0)
        self.crayon.penup()
        self.crayon.goto(super().point)
        self.crayon.pendown()
        self.crayon.write(self.message_debut, font=(self.font_police, self.taille_police, self.type_police))
        self.cpt: int = 0
        self.objet: list = list()
    def affichage_inventaire(self):
        self.crayon.penup()
        x, y = super().point
        print(x, y)
        y -= 10
        self.point = (x, y)
        print(super().point)
        self.crayon.goto(super().point)
        self.crayon.pendown()
        self.cpt += 1
        self.crayon.write("N°{0}: {1}".format(self.cpt, self.objet[self.cpt - 1]))
    def get_nombre_objet(self) -> int:
        return len(self.objet)
    def set_objet(self, objet):
        self.objet.append(objet)
        self.affichage_inventaire()
class Joueur(Cercle):
    def __init__(self, coord: tuple, coter: int):
        super().__init__(coord, coter, 1, 1, COULEUR_PERSONNAGE)
        self.inventaire = Inventaire()
        self.annonceur = Annonceur()
        self.coordoner_tableau: tuple = [1, 0]
        self.plan_ch: list
        self.ecoute = turtle.Screen()
        self.crayon = tortue

        self.crayon.speed(0)
        self.dx = coter  # permet de faire un placement de 10 pixelle en x
        self.dy = coter
        self.ecoute.listen()
        self.ecoute.onkeypress(self.deplacer_left, "Left")
        self.ecoute.onkeypress(self.deplacer_right, "Right")
        self.ecoute.onkeypress(self.deplacer_up, "Up")
        self.ecoute.onkeypress(self.deplacer_down, "Down")
        self.nombre_objet_a_trouver: int = None
        self.update()
    def update(self):
        self.trace_case(self.crayon)
    def nombre_objet_a_trouvers(self, n: int):
        self.nombre_objet_a_trouver = n
    def set_plan_chateau(self, p):
        self.plan_ch = p
    def d_left(self):
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x - self.dx - 1, y)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()
    def d_right(self):
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x + self.dx + 1, y)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()
    def d_up(self):
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x, y + self.dy + 1)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()
    def d_down(self):
        x, y = self.position
        self.new_couleur(COULEUR_VUE)
        self.update()
        self.position = (x, y - self.dx - 1)
        self.new_couleur(COULEUR_PERSONNAGE)
        self.update()
    def new_couleur(self, nouvelle_couleur):
        super().new_couleur(nouvelle_couleur)
    def deplacer(self, matrice: list, position: tuple, mouvement):
        if mouvement == "droite":
            x = self.coordoner_tableau[0]
            y = self.coordoner_tableau[1]
            if x < len(self.plan_ch[0]):
                if self.plan_ch[y][x + 1].__class__ in [Couloir.__mro__[0], Objet.__mro__[0], Porte.__mro__[0],Porte_sortie.__mro__[0]]:
                    if self.plan_ch[y][x + 1].__class__ == Couloir.__mro__[0]:
                        self.coordoner_tableau[0] += 1
                        self.d_right()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()
                    elif self.plan_ch[y][x + 1].__class__ == Objet.__mro__[0]:
                        self.coordoner_tableau[0] += 1
                        self.d_right()
                        self.inventaire.set_objet(self.plan_ch[y][x + 1].get_message())
                        self.annonceur.affiche_nouveau_message("Vous avez trouvez un nouvelle Objet " + self.plan_ch[y][x + 1].get_message())
                        self.plan_ch[y][x + 1] = Couloir(self.plan_ch[y][x + 1].position, self.plan_ch[y][x + 1].coter,1, 1)
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
                        if self.inventaire.get_nombre_objet() == self.nombre_objet_a_trouver:
                            self.coordoner_tableau[0] += 1
                            self.d_right()
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.plan_ch[y][x].update()
                            self.update()
                            self.annonceur.affiche_nouveau_message("Bravo, Vous avez gagner!!!!!")
                            for i in range(1000000):  # pour pas que la fenetre se referme directement
                                pass
                            exit(0)
                        else:
                            self.annonceur.affiche_nouveau_message("Vous avez pas trouver tout les objets!!!!!")
        elif mouvement == "gauche":
            x = self.coordoner_tableau[0]
            y = self.coordoner_tableau[1]
            if x >= 1:
                if self.plan_ch[y][x - 1].__class__ in [Couloir.__mro__[0], Objet.__mro__[0], Porte.__mro__[0],Porte_sortie.__mro__[0]]:
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
                            self.plan_ch[y][x - 1] = Couloir(self.plan_ch[y][x - 1].position,self.plan_ch[y][x - 1].coter, 1, 1)
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
                            for i in range(1000000):  # pour pas que la fenetre se referme directement
                                pass
                            exit(0)
                        else:
                            self.annonceur.affiche_nouveau_message("Vous avez pas trouver tout les objets!!!!!")
        elif mouvement == "haut":
            x = self.coordoner_tableau[0]
            y = self.coordoner_tableau[1]
            if y >= 0:
                if self.plan_ch[y - 1][x].__class__ in [Couloir.__mro__[0], Objet.__mro__[0], Porte.__mro__[0],Porte_sortie.__mro__[0]]:
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
                        self.annonceur.affiche_nouveau_message("Vous avez trouvez un nouvelle Objet " + self.plan_ch[y - 1][x].get_message())
                        self.plan_ch[y - 1][x] = Couloir(self.plan_ch[y - 1][x].position, self.plan_ch[y][x].coter, 1,1)
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
                            self.plan_ch[y - 1][x] = Couloir(self.plan_ch[y - 1][x].position,self.plan_ch[y - 1][x].coter, 1, 1)
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
                            self.plan_ch[y - 1][x] = Couloir(self.plan_ch[y - 1][x].position,
                                                             self.plan_ch[y - 1][x].coter, 1, 1)
                            self.plan_ch[y - 1][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y - 1][x].update()
                            self.update()
                            self.annonceur.affiche_nouveau_message("Bravo, Vous avez gagner!!!!!")
                            for i in range(1000000):  # pour pas que la fenetre se referme directement
                                pass
                            exit(0)
                        else:
                            self.annonceur.affiche_nouveau_message("Vous avez pas trouver tout les objets!!!!!")
        elif mouvement == "bas":
            x = self.coordoner_tableau[0]
            y = self.coordoner_tableau[1]
            if y <= len(self.plan_ch) + 1:
                if self.plan_ch[y + 1][x].__class__ in [Couloir.__mro__[0], Objet.__mro__[0], Porte.__mro__[0],Porte_sortie.__mro__[0]]:
                    if self.plan_ch[y + 1][x].__class__ == Couloir.__mro__[0]:
                        self.coordoner_tableau[1] += 1
                        self.d_down()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()
                    elif self.plan_ch[y + 1][x].__class__ == Objet.__mro__[0]:
                        self.coordoner_tableau[1] += 1
                        self.d_down()
                        self.inventaire.set_objet(self.plan_ch[y + 1][x].get_message())
                        self.annonceur.affiche_nouveau_message(
                            "Vous avez trouvez un nouvelle Objet " + self.plan_ch[y + 1][x].get_message())
                        self.plan_ch[y + 1][x] = Couloir(self.plan_ch[y + 1][x].position, self.plan_ch[y + 1][x].coter,1, 1)
                        self.plan_ch[y + 1][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y + 1][x].update()
                        self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                        self.plan_ch[y][x].update()
                        self.plan_ch[y][x].update()
                        self.update()
                    elif self.plan_ch[y + 1][x].__class__ == Porte.__mro__[0]:
                        self.annonceur.affiche_nouveau_message("Porte est fermer !!!!")
                        if self.plan_ch[y + 1][x].poser_question():
                            self.coordoner_tableau[1] += 1
                            self.d_down()
                            self.plan_ch[y][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y][x].update()
                            self.plan_ch[y][x].update()
                            self.plan_ch[y + 1][x] = Couloir(self.plan_ch[y + 1][x].position,
                                                             self.plan_ch[y + 1][x].coter, 1, 1)
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
                            self.plan_ch[y + 1][x] = Couloir(self.plan_ch[y + 1][x].position,
                                                             self.plan_ch[y + 1][x].coter, 1, 1)
                            self.plan_ch[y + 1][x].new_couleur(COULEUR_VUE)
                            self.plan_ch[y + 1][x].update()
                            self.update()
                            self.update()
                            self.annonceur.affiche_nouveau_message("Bravo, Vous avez gagner!!!!!")
                            for i in range(10000000):  # pour pas que la fenetre se referme directement
                                pass
                            exit(0)
                        else:
                            self.annonceur.affiche_nouveau_message("Vous avez pas trouver tout les objets!!!!!")
    def deplacer_right(self):
        self.ecoute.onkeypress(None, "Right")
        self.deplacer(self.plan_ch, self.position, "droite")
        self.ecoute.onkeypress(self.deplacer_right, "Right")
    def deplacer_left(self):
        self.ecoute.onkeypress(None, "Left")
        self.deplacer(self.plan_ch, self.position, "gauche")
        self.ecoute.onkeypress(self.deplacer_left, "Left")
    def deplacer_up(self):
        self.ecoute.onkeypress(None, "Up")
        self.deplacer(self.plan_ch, self.position, "haut")
        self.ecoute.onkeypress(self.deplacer_up, "Up")
    def deplacer_down(self):
        self.ecoute.onkeypress(None, "Down")
        self.deplacer(self.plan_ch, self.position, "bas")
        self.ecoute.onkeypress(self.deplacer_down, "Down")
global tortue
tortue=turtle.Turtle()
tortue.hideturtle()
chateau = Chateau(fichier_plan, COULEURS, ZONE_PLAN_MINI, ZONE_PLAN_MAXI)
hauteur, largeur = ZONE_PLAN_MINI
p = turtle
p.Screen()
p.setup((hauteur * -2) + 20, (largeur * -2 + 20))
chateau.afficher_plan()
p1 = Joueur((chateau.get_chateau()[0][1].position[0] + (chateau.get_coter() // 2),
             chateau.get_chateau()[0][1].position[1] - (chateau.get_coter() // 2)), chateau.get_coter())
p1.set_plan_chateau(chateau.get_chateau())
p1.nombre_objet_a_trouvers(len(chateau.dico_objet))
p1.ecoute.mainloop()
p.listen()
