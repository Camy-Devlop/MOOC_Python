"""PROJET INFO 2020
Le labyrinthe du python des neiges par Noé Medaets (matricule 000520074)
et Ali Dama (matricule 000513470)"""
from CONFIGS import *
import turtle

def lire_matrice(fichier):
	"""Fonction qui reçoit le nom du fichier map et renvoie la matrice correspondante"""
	res=[]
	with open(fichier) as f:
		for ligne in f:
			res.append([int(i) for i in ligne.strip().split(" ")])
	return res

def calculer_pas(matrice):
	"""retourne la taille des cases"""
	size_x=(ZONE_PLAN_MAXI[0]-ZONE_PLAN_MINI[0])/len(matrice)
	size_y=(ZONE_PLAN_MAXI[1]-ZONE_PLAN_MINI[1])/len(matrice[0])
	if size_x<size_y:
		res=size_x
	else:
		res=size_y
	return int(res)

def coordonnees(case,pas):
	"""renvoie les coordonnées du coin inférieur gauche du carré donné par le tuple case grâce à l'entier pas (=taille des cases)"""
	res=(ZONE_PLAN_MINI[0]+case[1]*pas, ZONE_PLAN_MAXI[1]-case[0]*pas)
	return res

def tracer_rectangle(dimensionX, dimensionY):
	"""trace un rectangle d'une certaine dimension à partir du point où se trouve déjà la tortue"""
	turtle.seth(90) #tourne la tortue vers le haut
	for i in range(2):
		turtle.fd(dimensionY)
		turtle.right(90)
		turtle.fd(dimensionX)
		turtle.right(90)

def tracer_case(case,couleur,pas):
	"""Trace une case, donnée par le tuple case, de taille donnée par "pas" et d'une certaine couleur"""
	turtle_clean_goto(*coordonnees(case,pas))
	turtle.fillcolor(couleur)
	turtle.begin_fill()
	tracer_rectangle(pas,pas)
	turtle.end_fill()

def afficher_plan(matrice):
	"""affiche la carte à partir de la matrice"""

	for i in range(len(matrice)):
		for j in range(len(matrice[i])):
			tracer_case((i,j), COULEURS[matrice[i][j]], calculer_pas(matrice))

def deplacer(matrice, position, mouvement, inventaire, dico_objets, dico_portes):
	"""fonction pour les déplacements du personnage.
	Entrées :
		-matrice : la matrice de la carte
		-couple position : la position actuelle du joueur
		-couple mouvement : le mouvement que le joueur veut effectuer (0,1) ou (-1,0) par exemple
		-liste inventaire : l'inventaire (pour y ajouter un objet)
		-dictionnaire dico_objets : le dictionnaire contenant touts les objets disponibles sur la carte
		-dictionnaire dico_portes : le dictionnaire contenant toutes les questions à poser lorsque le joueur veut passer une porte
	Sortie : la nouvelle position du joueur"""
	pos=position
	pas=calculer_pas(matrice)
	case_actuelle=matrice[position[0]][position[1]]
	case_deplacement=matrice[position[0]+mouvement[0]][position[1]+mouvement[1]]
	if case_deplacement==0 or case_deplacement==3 and bonne_reponse((position[0]+mouvement[0], position[1]+mouvement[1]), dico_portes):
		pos=(position[0]+mouvement[0], position[1]+mouvement[1])


	if case_deplacement==4:
		pos=(position[0]+mouvement[0], position[1]+mouvement[1])
		ramasser_objet(pos, inventaire, dico_objets)

	if case_deplacement==2:
		annonce("VICTOIRE")
		turtle.title("VOUS ETES TROP FORT")
		pos=(position[0]+mouvement[0], position[1]+mouvement[1])

	matrice[pos[0]][pos[1]]=0 #comme ça si le joueur a ramassé un objet ou est passé par une porte l'objet ou la porte disparait
	tracer_case(position, COULEUR_VUE, pas)
	tracer_joueur(pos,COULEUR_PERSONNAGE,pas,RATIO_PERSONNAGE)
	return pos

def deplacer_gauche():
	global matrice,position,inventaire,objets,portes
	turtle.onkeypress(None, "Left")
	position=deplacer(matrice,position,(0,-1),inventaire,objets,portes)
	turtle.onkeypress(deplacer_gauche, "Left")

def deplacer_droite():
	global matrice,position,inventaire,objets,portes
	turtle.onkeypress(None, "Right")
	position=deplacer(matrice,position,(0,1),inventaire,objets,portes)
	turtle.onkeypress(deplacer_droite, "Right")

def deplacer_haut():
	global matrice,position,inventaire,objets,portes
	turtle.onkeypress(None, "Up")
	position=deplacer(matrice,position,(-1,0),inventaire,objets,portes)
	turtle.onkeypress(deplacer_haut, "Up")

def deplacer_bas():
	global matrice,position,inventaire,objets,portes
	turtle.onkeypress(None, "Down")
	position=deplacer(matrice,position,(1,0),inventaire,objets,portes)
	turtle.onkeypress(deplacer_bas, "Down")

def tracer_joueur(position,couleur,pas,taille):
	"""Trace la position du joueur sur la carte
		Entrées : -position : la position du personnage sur la matrice
				  -couleur : la couleur du personnage
				  -pas : la taille des cases
				  -taille : la taille du personnage relative au pas"""
	coordonnees_joueur=tuple([i+pas/2 for i in coordonnees(position,pas)])
	turtle_clean_goto(*coordonnees_joueur)
	turtle.dot(pas/taille,couleur)

def creer_dictionnaire_des_objets(fichier):
	"""Renvoie un dictionnaire construit à partir d'un fichier"""
	res={}
	with open(fichier,encoding='utf-8') as f:
		for ligne in f:
			a,b=eval(ligne)
			res[a]=b
	return res

def ramasser_objet(position, inventaire, dico_objets):
	"""fonction appelée lorsque le joueur passe sur un objet. Cet objet est alors retiré de la carte et ajouté dans l'inventaire
		Entrées : -matrice : la matrice de la carte
				  -couple position : la position du joueur sur la carte
				  -liste inventaire : l'inventaire du joueur
				  -dictionnaire dico_objets : le dictionnaire contenant touts les objets disponibles sur la carte"""
	inventaire.append(dico_objets[position])
	afficher_inventaire(inventaire)
	annonce("Vous avez trouvé un objet : " + dico_objets[position])

def annonce(texte):
	"""Affiche un texte dans le bandeau 'annonces' en haut de l'écran"""
	turtle_clean_goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1]-20)
	turtle.fillcolor('white')
	turtle.begin_fill()
	tracer_rectangle(480, 20)
	turtle.end_fill()
	turtle.penup()
	turtle.goto(0, POINT_AFFICHAGE_ANNONCES[1]-15)
	turtle.write(texte, font=("Arial", 8, "normal"), align="center")

def afficher_inventaire(inventaire):
    
	"""Affiche l'inventaire du joueur dans le champs de gauche
		-Entrée : l'inventaire du joueur"""
	turtle_clean_goto(POINT_AFFICHAGE_INVENTAIRE[0], POINT_AFFICHAGE_INVENTAIRE[1]-440)
	turtle.fillcolor('white')
	turtle.begin_fill()
	tracer_rectangle(170,440)
	turtle.end_fill()
	turtle_clean_goto(POINT_AFFICHAGE_INVENTAIRE[0]+85, POINT_AFFICHAGE_INVENTAIRE[1]-15)
	turtle.write("INVENTAIRE :", font=("Arial", 10, "underline"), align="center")
	ligne=0
	for i in range(len(inventaire)):
		objet="--> "+inventaire[i]
		for j in range(0,len(objet),30):
			turtle_clean_goto(POINT_AFFICHAGE_INVENTAIRE[0]+85, POINT_AFFICHAGE_INVENTAIRE[1]-15*(ligne+3))
			turtle.write(objet[j:j+30], font=("Arial", 8, "normal"), align="center")#cela permet d'afficher max 25 caractères par ligne (comme ça on dépasse pas)
			ligne+=1



def turtle_clean_goto(pos_x, pos_y):
	"""Déplace la tortue vers une certaine position sans laisser de trainée derrière elle
		-Entrées : les coordonnées en x et y vers lesquelles la tortues doit se rendre"""
	turtle.penup()
	turtle.goto(pos_x, pos_y)
	turtle.pendown()

def bonne_reponse(coordonnee, questions):
	"""Pose la question correspondante à la porte donnée par coordonnee
		Renvoie True si le joueur donne une bonne réponse
		Renvoie False si le joueur donne une mauvaise réponse
		-Entrees : -coordonnee : les coordonnées (dans la matrice) de la porte
				   -questions : le dictionnaire contenant les questions"""
	reponse_joueur = turtle.textinput("QUESTION", questions[coordonnee][0])
	turtle.listen()
	ok=questions[coordonnee][1]==reponse_joueur
	if ok:
		annonce("Bien joué !")
	else:
		annonce("Aîe, on dirait que vous êtes nul :(")
	return ok


#main code
position = (0,1)
inventaire=[]
ecran=turtle.setup()
turtle.speed(0)
turtle.tracer(0,0)
turtle.ht()
turtle.title("Le labyrinthe de la peur")
annonce("Chargement...")
matrice=lire_matrice(fichier_plan)
afficher_plan(matrice)
portes=creer_dictionnaire_des_objets(fichier_questions)
objets=creer_dictionnaire_des_objets(fichier_objets)
tracer_joueur(position,COULEUR_PERSONNAGE,calculer_pas(matrice),RATIO_PERSONNAGE)
afficher_inventaire(inventaire)
annonce("Bienvenue dans le jeu")
turtle.update()

turtle.listen()
turtle.onkeypress(deplacer_gauche, "Left")
turtle.onkeypress(deplacer_droite, "Right")
turtle.onkeypress(deplacer_haut, "Up")
turtle.onkeypress(deplacer_bas, "Down")
turtle.mainloop()
