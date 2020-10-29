from Outils.CONFIGS import *
from Outils.chateau import Chateau
from Outils.carrer import Carrer
from Outils.point import Point
import turtle

#ch=Chateau(fichier_plan,COULEURS)
hauteur,largeur=ZONE_PLAN_MINI
"""
p=turtle.Screen()
p.setup(hauteur*-2,largeur*-2)
pe=turtle.Turtle()
pe.speed(0)
pe.ht()
#ch.dessiner()
"""
p=turtle.Screen()
p.setup((hauteur*-2)+8,(hauteur*-2)+24)

pe=turtle.Turtle()
pe.speed(0)
from Outils.polygone import Polygone
l=[290,440,290,440]
r=[90,90,90,90]
poly=Polygone("red",(-240,-240),l,r)
poly.dessiner()
c1=Carrer(Point(50, 200),10,1,1,"","red")
c1.dessiner(pe)
c2=Carrer(Point(-240, -240),10,1,1,"","red")
c2.dessiner(pe)
#--------------------------------------------
c3=Carrer(Point(-240, 240),10,1,1,"","blue")
c3.dessiner(pe)
c2=Carrer(Point(70, 210),10,1,1,"","green")
c2.dessiner(pe)

p.mainloop()
