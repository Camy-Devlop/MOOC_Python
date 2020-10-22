from fenetre import Fenetre
from carrer import Carrer
from point import Point
hauteur=500
largeur=500
fenetre=Fenetre(largeur,hauteur,"Black","lanseleau dans le ltmbirinte")


fenetre.add_objet(Carrer(Point(40,50),-1,1,"circle","blue"))
fenetre.add_objet(Carrer(Point(30,-10),1,1,"square","white"))
fenetre.dessiner()

