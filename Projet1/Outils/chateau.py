import io
from Outils.CONFIGS import fichier_plan,ZONE_PLAN_MINI,ZONE_PLAN_MAXI
class Chateau():

    def __init__(self):
        self.chateau: str = None
        self.nom_fichier=fichier_plan
        self.recuperation_fichier()
        self.dessiner()
        #TODO

    def recuperation_fichier(self):#TODO: "lecture du fichier pour desinne le chateau"
        with open(self.nom_fichier,"r") as lecture:
            self.chateau=lecture.read()

    def dessiner(self):
        print(self.chateau)

d=Chateau()