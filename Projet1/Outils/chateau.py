from Outils.mur import Mur
from Outils.vue import Vue
from Outils.porte import Porte
from Outils.couloir import Couloir
from Outils.objet import Objet


class Chateau():

    def __init__(self, fichier: str, couleur: list):
        self.chateau_str: str = None
        self.couleur = couleur
        with open("Outils/" + fichier, "r", encoding="utf-8") as lecture:
            self.chateau_str = lecture.read()
        self.tb_chateau = self.chateau_str.split('\n')
        for v, i in enumerate(self.tb_chateau):
            self.tb_chateau[v] = i.split(" ")

    # TODO: le reste du tableau pour le Chateau entre dans un tableau
    def dessiner(self):
        tb_ch = []
        tb_tmp = []
        tmp_x = -240
        tmp_y = 90
        for l, i in enumerate(self.tb_chateau):
            for ll, j in enumerate(i):
                if j == '0':
                    tb_tmp.append(Couloir((tmp_x, tmp_y), 10, 1, 1, ""))
                elif j == '1':
                    tb_tmp.append(Mur((tmp_x, tmp_y), 10, 1, 1, ""))
                elif j == '2':
                    tb_tmp.append(Porte((tmp_x, tmp_y), 10, 1, 1, ""))
                elif j == '3':
                    tb_tmp.append(Porte((tmp_x, tmp_y), 10, 1, 1, ""))
                elif j == '4':
                    tb_tmp.append(Objet((tmp_x, tmp_y), 10, 1, 1, ""))
                tmp_x += 12
            tb_ch.append(tb_tmp)

            tmp_y -= 12
            tmp_x = -240

    def update(self):  # TODO: afaire pour le depalcement du chateau
        pass