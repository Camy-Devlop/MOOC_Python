"""
CHATEAU DES NEIGES
Auteur : Ben David MALYANE
Date : 12 novembre 2020

Lancelot entre dans le château au sommet du Python des Neiges, muni de son précieux sac de rangement
et de sa torche fraîchement allumée aux feux de Beltane. Il doit trouver la statue de sainte Axerror,
le chef-d’oeuvre de Gide de Rome, dit le « tyran malfaisant éternel ».

Heureusement, pour l’aider dans sa quête, Merlin, son maître, lui a fourni un plan minutieux des salles
et des couloirs du château. Ce plan lui sera fort utile, vu l’énormité du bâtiment, tant par sa taille que
par le nombre de ses pièces !

Avant de partir, Merlin lui a donné la clef de la porte d’entrée du château et lui a prodigué moults conseils,
dont celui de bien garder tous les objets qu’il trouvera lors de sa quête : ceux-ci lui permettront de répondre
aux diverses énigmes que ne manqueront pas de poser les gardes postés devant les portes à l’intérieur du château.

Merlin a affirmé à son disciple que, s’il procède avec intelligence, sa quête sera satisfaite.

Résultat : Lancelot trouve la statue de sainte Axerror ou pas.

"""

import turtle
from CONFIGS import *


                                # Niveau 1 : Construction et affichage du plan du château
def lire_matrice(fichier):
    """Cette fonction reçois le fichier plan lit le fichier plan et renvois la matrice correspondante"""

    matrice = []

    for ligne in open(fichier):
        matrice.append(list(ligne.split()))

    return matrice


def calculer_pas(matrice):
    """Cette fonction reçois la matrice calcule la dimension des cases du plan et la renvois"""

    nb_de_case_largeur = len(matrice[0])
    nb_de_case_hauteur = len(matrice)

    largeur_zone = ZONE_PLAN_MAXI[0] - ZONE_PLAN_MINI[0]
    hauteur_zone = ZONE_PLAN_MAXI[1] - ZONE_PLAN_MINI[1]

    largeur_case = largeur_zone // nb_de_case_largeur
    hauteur_case = hauteur_zone // nb_de_case_hauteur

    if largeur_case < hauteur_case:
        pas = largeur_case
    else:
        pas = hauteur_case

    return pas


def coordonnees(matrice, pas):
    """Cette fonction reçois la matrice plan ainsi que la dimension des côtés des cases
    Retourne le dictionnnaire des positions(des coordonnées turtle) des cases du plan
    et la valeur de chacune des cases représentant la couleur"""

    pos_case = {}

    line = -240
    for i in range(len(matrice) - 1, -1, -1):
        col = -240
        for j in range(len(matrice[0])):
            pos_case[(j, i)] = [(col, line), int(matrice[i][j])]
            col += pas
        line += pas

    return pos_case


def tracer_carre(dimension):
    """Cette fonction reçois la mesure des côtés des cases du plan et
    Trace un carré représentant une case"""
    turtle.speed(0)
    for side in range(4):
        turtle.forward(dimension)
        turtle.left(90)


def tracer_case(case, couleur, pas):


    """Cette fonction reçois les positions des cases ainsi
    que la mesure des côtés des cases (reçois aussi un paramètre couleur en string vide)
    Trace les cases du plan en fonction de leur couleur(leur nature)"""

    # Gestion des couleurs (des natures) des cases
    for elem in case:
        if case[elem][1] == 0:
            couleur = COULEUR_COULOIR
        elif case[elem][1] == 1:
            couleur = COULEUR_MUR
        elif case[elem][1] == 2:
            couleur = COULEUR_OBJECTIF
        elif case[elem][1] == 3:
            couleur = COULEUR_PORTE
        elif case[elem][1] == 4:
            couleur = COULEUR_OBJET

        turtle.hideturtle()
        turtle.up()
        turtle.goto(case[elem][0][0], case[elem][0][1])
        turtle.down()
        turtle.color(COULEUR_EXTERIEUR, couleur)
        turtle.begin_fill()
        tracer_carre(pas)
        turtle.end_fill()


def afficher_plan(matrice):
    """Affichage du plan"""
    global pos_case, PAS

    tracer_case(case=pos_case, couleur='', pas=PAS) #La gestion des couleurs se fait dans la fonction tracer case d'où couleur = ''
#Fin Niveau 1


                                #Niveau 2: gestion des déplacements
def deplacer(matrice, position, mouvement):
    """Déplace le personnage en fonction du mouvement demandé par le joueur"""
    global PAS, inventaire

    turtle.color(COULEUR_EXTERIEUR, COULEUR_VUE)
    turtle.goto(position[0] - PAS/2, position[1] - PAS/2)
    turtle.begin_fill()
    tracer_carre(PAS)
    turtle.end_fill()
    personnage.goto(mouvement)
    personnage.dot(RATIO_PERSONNAGE * PAS, COULEUR_PERSONNAGE)
    position[:] = list(personnage.position())



def deplacer_gauche():
    """Demande le déplacement du personnage vers la gauche si le mouvement est possible"""
    global MATRICE, position, pos_case, pos_matrice

    personnage.onkeypress(None, "Left")   # Désactive la touche Left
    new_pos = (personnage.position()[0] - PAS, personnage.position()[1])
    pos_matrice[:] = [pos_matrice[0] - 1, pos_matrice[1]]
    if -1 < pos_matrice[0] < len(MATRICE[0]) and -1 < pos_matrice[1] < len(MATRICE) :
        if pos_case[tuple(pos_matrice)][1] == 0:
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 1:
            pos_matrice[:] = [pos_matrice[0] + 1, pos_matrice[1]]
            mouvement = personnage.position()
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 4:
            inventaire.add(DICO_OBJETS[(pos_matrice[1], pos_matrice[0])])
            ramasser_objet()
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 3:
            mouvement = new_pos
            if poser_question(MATRICE, mouvement) is True:
                deplacer(MATRICE, position, mouvement)
            else:
                pos_matrice[:] = [pos_matrice[0] + 1, pos_matrice[1]]
                mouvement = personnage.position()
                deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 2:
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
            effaceur()
            aff_annonce = turtle.Turtle()
            aff_annonce.hideturtle()
            aff_annonce.up()
            aff_annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
            aff_annonce.write('Félicitaion Lancelo, tu a trouvé la statue de sainte Axerror !',
                              font=("Roman", 16, "normal"))
            pos_case[tuple(pos_matrice)][1] = 0
    else:
        pos_matrice[:] = [pos_matrice[0] + 1, pos_matrice[1]]
        effaceur()
        aff_annonce = turtle.Turtle()
        aff_annonce.color('red')
        aff_annonce.hideturtle()
        aff_annonce.up()
        aff_annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
        aff_annonce.write('Mouvement pas possible', font=("Arial", 10, "normal"))
    personnage.onkeypress(deplacer_gauche, "Left")   # Réassocie la touche Left à la fonction deplacer_gauche

def deplacer_droite():
    """Demande le déplacement du personnage vers la droite si le mouvement est possible"""
    global MATRICE, position, pos_case, pos_matrice

    personnage.onkeypress(None, "Right")   # Désactive la touche Right
    new_pos = (personnage.position()[0] + PAS, personnage.position()[1])
    pos_matrice[:] = [pos_matrice[0] + 1, pos_matrice[1]]
    if -1 < pos_matrice[0] < len(MATRICE[0]) and -1 < pos_matrice[1] < len(MATRICE):
        if pos_case[tuple(pos_matrice)][1] == 0:
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 1:
            pos_matrice[:] = [pos_matrice[0] - 1, pos_matrice[1]]
            mouvement = personnage.position()
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 4:
            inventaire.add(DICO_OBJETS[(pos_matrice[1], pos_matrice[0])])
            ramasser_objet()
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 3:
            mouvement = new_pos
            if poser_question(MATRICE, mouvement) is True:
                deplacer(MATRICE, position, mouvement)
            else:
                pos_matrice[:] = [pos_matrice[0] - 1, pos_matrice[1]]
                mouvement = personnage.position()
                deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 2:
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
            effaceur()
            aff_annonce = turtle.Turtle()
            aff_annonce.hideturtle()
            aff_annonce.up()
            aff_annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
            aff_annonce.write('Félicitaion Lancelo, tu a trouvé la statue de sainte Axerror !',
                              font=("Roman", 16, "normal"))
            pos_case[tuple(pos_matrice)][1] = 0
    else:
        pos_matrice[:] = [pos_matrice[0] - 1, pos_matrice[1]]
        effaceur()
        aff_annonce = turtle.Turtle()
        aff_annonce.color('red')
        aff_annonce.hideturtle()
        aff_annonce.up()
        aff_annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
        aff_annonce.write('Mouvement pas possible', font=("Arial", 10, "normal"))
    personnage.onkeypress(deplacer_droite, "Right")   # Réassocie la touche Left à la fonction deplacer_droite

def deplacer_haut():
    """Demande le déplacement du personnage vers le haut si le mouvement est possible"""
    global MATRICE, position, pos_case, pos_matrice

    personnage.onkeypress(None, "Up")   # Désactive la touche Up
    new_pos = (personnage.position()[0], personnage.position()[1] + PAS)
    pos_matrice[:] = [pos_matrice[0], pos_matrice[1] - 1]
    if -1 < pos_matrice[0] < len(MATRICE[0]) and -1 < pos_matrice[1] < len(MATRICE):
        if pos_case[tuple(pos_matrice)][1] == 0:
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 1:
            pos_matrice[:] = [pos_matrice[0], pos_matrice[1] + 1]
            mouvement = personnage.position()
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 4:
            inventaire.add(DICO_OBJETS[(pos_matrice[1], pos_matrice[0])])
            ramasser_objet()
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 3:
            mouvement = new_pos
            if poser_question(MATRICE, mouvement) is True:
                deplacer(MATRICE, position, mouvement)
            else:
                pos_matrice[:] = [pos_matrice[0], pos_matrice[1] + 1]
                mouvement = personnage.position()
                deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 2:
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
            effaceur()
            aff_annonce = turtle.Turtle()
            aff_annonce.hideturtle()
            aff_annonce.up()
            aff_annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
            aff_annonce.write('Félicitaion Lancelo, tu a trouvé la statue de sainte Axerror !',
                              font=("Roman", 16, "normal"))
            pos_case[tuple(pos_matrice)][1] = 0
    else:
        pos_matrice[:] = [pos_matrice[0], pos_matrice[1] + 1]
        effaceur()
        aff_annonce = turtle.Turtle()
        aff_annonce.color('red')
        aff_annonce.hideturtle()
        aff_annonce.up()
        aff_annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
        aff_annonce.write('Mouvement pas possible', font=("Arial", 10, "normal"))

    personnage.onkeypress(deplacer_haut, "Up")   # Réassocie la touche Left à la fonction deplacer_haut

def deplacer_bas():
    """Demande le déplacement du personnage vers le bas si le mouvement est possible"""
    global MATRICE, position, pos_case, pos_matrice

    personnage.onkeypress(None, "Down")   # Désactive la touche Down
    new_pos = (personnage.position()[0], personnage.position()[1] - PAS)
    pos_matrice[:] = [pos_matrice[0], pos_matrice[1] + 1]
    if -1 < pos_matrice[0] < len(MATRICE[0]) and -1 < pos_matrice[1] < len(MATRICE):
        if pos_case[tuple(pos_matrice)][1] == 0:
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 1:
            pos_matrice[:] = [pos_matrice[0], pos_matrice[1] - 1]
            mouvement = personnage.position()
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 4:
            inventaire.add(DICO_OBJETS[(pos_matrice[1], pos_matrice[0])])
            ramasser_objet()
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 3:
            mouvement = new_pos
            if poser_question(MATRICE, mouvement) is True:
                deplacer(MATRICE, position, mouvement)
            else:
                pos_matrice[:] = [pos_matrice[0], pos_matrice[1] - 1]
                mouvement = personnage.position()
                deplacer(MATRICE, position, mouvement)
        elif pos_case[tuple(pos_matrice)][1] == 2:
            mouvement = new_pos
            deplacer(MATRICE, position, mouvement)
            effaceur()
            aff_annonce = turtle.Turtle()
            aff_annonce.hideturtle()
            aff_annonce.up()
            aff_annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
            aff_annonce.write('Félicitaion Lancelo, tu a trouvé la statue de sainte Axerror !',
                              font=("Roman", 16, "normal"))
            pos_case[tuple(pos_matrice)][1] = 0
    else:
        pos_matrice[:] = [pos_matrice[0], pos_matrice[1] - 1]
        effaceur()
        aff_annonce = turtle.Turtle()
        aff_annonce.color('red')
        aff_annonce.hideturtle()
        aff_annonce.up()
        aff_annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
        aff_annonce.write('Mouvement pas possible', font=("Arial", 10, "normal"))
    personnage.onkeypress(deplacer_bas, "Down")   # Réassocie la touche Left à la fonction deplacer_bas
#Fin Niveau 2


                                                #Niveau 3 : collecte d’objets dans le labyrinthe
def creer_dictionnaire_des_objets(fichier_des_objets):
    """Renvoie un dictionnaire des objets du plan
    ayant pour clés leur coordonnée dans le plan"""
    dico_objet = {}
    for ligne in open(fichier_des_objets, encoding='utf-8'):
        a, b = eval(ligne)
        dico_objet[a] = b

    return dico_objet


def effaceur():
    """Permet d'effacer les annonces sur le panneau d'affichage des annonces
     afin de permetrre l'affichage de nouvelles annonces"""

    efface_annonce = turtle.Turtle()
    efface_annonce.speed(0)
    efface_annonce.hideturtle()
    efface_annonce.up()
    efface_annonce.goto(POINT_AFFICHAGE_ANNONCES[0] - 10, POINT_AFFICHAGE_ANNONCES[1])
    efface_annonce.begin_fill()
    efface_annonce.color(COULEUR_EXTERIEUR)
    for i in range(2):
        efface_annonce.forward(800)
        efface_annonce.left(90)
        efface_annonce.forward(50)
        efface_annonce.left(90)
    efface_annonce.end_fill()


def ramasser_objet():
    """Ramasse l'objet et modifie la case de l'objet
    en une case vide après l'avoir récupérer """
    global DICO_OBJETS ,MATRICE, pos_case, pos_matrice
    pos_case[tuple(pos_matrice)][1] = 0
    MATRICE[pos_matrice[1]][pos_matrice[0]] = 0

    effaceur()

    aff_annonce = turtle.Turtle()
    aff_annonce.hideturtle()
    aff_annonce.up()
    aff_annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
    aff_annonce.write('Vous avez trouvé un objet du type: ' + str(DICO_OBJETS[(pos_matrice[1], pos_matrice[0])]),
                      font=("Lucida Console", 10, "normal"))

    aff_inventaire = turtle.Turtle()
    aff_inventaire.speed(0)
    aff_inventaire.hideturtle()
    aff_inventaire.up()
    aff_inventaire.goto(POINT_AFFICHAGE_INVENTAIRE[0], POINT_AFFICHAGE_INVENTAIRE[1])
    aff_inventaire.color('black')
    if len(inventaire) == 1:
        aff_inventaire.write('Inventaire :', font=("Lucida Console", 10, "normal"))

    j = 15

    elem_inventaire = turtle.Turtle()
    pos_elem = (POINT_AFFICHAGE_INVENTAIRE[0], POINT_AFFICHAGE_INVENTAIRE[1] - j)
    elem_inventaire.up()
    elem_inventaire.hideturtle()
    elem_inventaire.speed(0)

    for elem in inventaire:
        elem_inventaire.goto(pos_elem[0], pos_elem[1] - j)
        j += 15

    n = len(inventaire)

    elem_inventaire.write("N°" + str(n) + ": " + str(DICO_OBJETS[(pos_matrice[1], pos_matrice[0])]), font=("Lucida Console", 8, "normal"))
#Fin Niveau 3


                                        #Niveau 4 : Le jeu escape game complet avec questions-réponses
def poser_question(matrice, mouvement):
    """Pose la question au personnage. Si la réponse est correcte la porte s'ouvre
    et change de nature(Elle devient une case vide = 0).
    Dans le cas contraire la porte reste fermée"""
    global DICO_PORTES, pos_case, pos_matrice
    res = False

    effaceur()

    aff_annonce = turtle.Turtle()
    aff_annonce.hideturtle()
    aff_annonce.up()
    aff_annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
    aff_annonce.write("Cette porte est fermée |¬(", font=("Lucida Console", 10, "normal"))

    reponse = turtle.textinput("Question", DICO_PORTES[(pos_matrice[1], pos_matrice[0])][0])
    if reponse == DICO_PORTES[(pos_matrice[1], pos_matrice[0])][1]:
        res = True

    if res is True:
        effaceur()
        aff_annonce.write("La porte s'ouvre !", font=("Lucida Console", 10, "normal"))
        pos_case[tuple(pos_matrice)][1] = 0
        matrice[pos_matrice[1]][pos_matrice[0]] = 0

    elif res is False:
        effaceur()
        aff_annonce.write("Cette porte est fermée |¬(", font=("Lucida Console", 10, "normal"))
    personnage.listen()

    return res
#Fin Niveau 4


                                                #Code principal
turtle.title('Python des Neiges')
turtle.tracer(False)

MATRICE = lire_matrice(fichier_plan) #Matrice plan
PAS = calculer_pas(MATRICE) #Dimension des cotés des cases formant le plan
pos_case = coordonnees(MATRICE, PAS) #Dictionnaire des positions des cases du plan

afficher_plan(MATRICE)


#Les objets et portes du plan
DICO_OBJETS = creer_dictionnaire_des_objets(fichier_objets)
DICO_PORTES = creer_dictionnaire_des_objets(fichier_questions)

inventaire = set() #Initialisation de l'inventaire du personnage


                                                #Création du personnage
position = [pos_case[(1, 0)][0][0] + PAS/2,
             pos_case[(1, 0)][0][1] + PAS/2] #Positionnement du personnage sur la position de départ

pos_matrice = list((1, 0)) #Position matricielle du personnage
#Choix du type liste pour permettre une meilleur gestion des mouvements du personnage

personnage = turtle #Nommage de turtle afin de permetrre une meilleur lecture du code
personnage.up()
personnage.goto(tuple(position))
personnage.dot(RATIO_PERSONNAGE * PAS, COULEUR_PERSONNAGE) #Le personnage est représenté par un point rouge
#Fin création du personnage

personnage.listen()    # Déclenche l’écoute du clavier
personnage.onkeypress(deplacer_gauche, "Left")   # Associe à la touche Left une fonction appelée deplacer_gauche
personnage.onkeypress(deplacer_droite, "Right")
personnage.onkeypress(deplacer_haut, "Up")
personnage.onkeypress(deplacer_bas, "Down")
personnage.mainloop()    # Place le programme en position d’attente d’une action du joueur