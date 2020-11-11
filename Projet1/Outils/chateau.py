from Outils.mur import Mur
from Outils.vue import Vue
from Outils.porte import Porte
from Outils.couloir import Couloir
from Outils.objet import Objet
from Outils.porte_sortie import Porte_sortie
import os
import sys


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
        self.matrice = self.lire_matrice(fichier)
        self.COTER = (min(abs(self.ZONE_PLAN1[0]) + abs(self.ZONE_PLAN2[0]),
                          abs(self.ZONE_PLAN1[1]) + abs(self.ZONE_PLAN2[1]))) // max(len(self.matrice),
                                                                                     len(self.matrice[0]))
        self.plan_matrice: list = []

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
        return matrice

    def afficher_plan(self, matrice=[]):
        """
        :methods afficher_plan: methode qui va se charger de constrire le cheateau garce a la matrice recu en paaramter
        :param matrice: paramtre que recoi la methode afficher_plan est un tableau
                        de matricr n x m contenant des valeur de 0 à 4

        """
        tb_ch = []
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
                    print(ex,ey)
                    tb_tmp.append(Porte((tmp_x, tmp_y), self.COTER, 1, 1, self.dico_question[(ex, ey)]))
                    # TODO: Ajouter les question dpor l'ouverture des portes
                    # tb_tmp[][]
                elif j == 4:
                    tb_tmp.append(Objet((tmp_x, tmp_y), self.COTER, 1, 1))
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
        sys.path.append("..")
        from CONFIGS import fichier_questions
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

            #d1 = d1.strip("(")
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