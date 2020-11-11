from CONFIGS import *
from Outils.chateau import Chateau
from Outils.joueur import Joueur
import turtle

chateau = Chateau(fichier_plan, COULEURS, ZONE_PLAN_MINI, ZONE_PLAN_MAXI)
hauteur, largeur = ZONE_PLAN_MINI
p = turtle
p.Screen()
p.setup(hauteur * -2, largeur * -2)

chateau.afficher_plan()
p1 = Joueur((chateau.get_chateau()[0][1].position[0]+5,chateau.get_chateau()[0][1].position[1]+5),chateau.get_coter())
print(len(chateau.get_chateau()[0]))
p1.set_plan_chateau(chateau.get_chateau())
p1.ecoute.mainloop()
p.listen()

