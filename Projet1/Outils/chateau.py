from Outils.mur import Mur
from Outils.vue import Vue
from Outils.porte import Porte
from Outils.couloir import Couloir
from Outils.objet import Objet


class Chateau():
    """
      Auteur: ISMAIL ADBAIBI 
      date : 15/10/2020
      But du programme :
      :class Chateau: la classe Chateau permet cree et de dessiner le 
                      chateau  
    """

    def __init__(self, fichier: str, couleur: list):
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
            """
        self.chateau_str: str = None
        self.couleur = couleur

        self.matrice = self.lire_matrice(fichier)

    def lire_matrice(self, fichier) -> list:
        """
          :methode : 
        """
        chateau_str: str = ""
        matrice: list
        with open("Outils/" + fichier, "r", encoding="utf-8") as lecture:
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
        tb_ch = []
        tb_tmp = []
        tmp_x = -240
        tmp_y = 90
        for l, i in enumerate(self.matrice):
            for ll, j in enumerate(i):
                if j == 0:
                    tb_tmp.append(Couloir((tmp_x, tmp_y), 10, 1, 1))
                elif j == 1:
                    tb_tmp.append(Mur((tmp_x, tmp_y), 10, 1, 1))
                elif j == 2:
                    tb_tmp.append(Porte((tmp_x, tmp_y), 10, 1, 1))
                elif j == 3:
                    tb_tmp.append(Porte((tmp_x, tmp_y), 10, 1, 1))
                elif j == 4:
                    tb_tmp.append(Objet((tmp_x, tmp_y), 10, 1, 1))
                tmp_x += 11
            tb_ch.append(tb_tmp)

            tmp_y -= 11
            tmp_x = -240

    def update(self):  # TODO: afaire pour le depalcement du chateau 
        pass