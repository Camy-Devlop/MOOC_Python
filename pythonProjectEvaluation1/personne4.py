"""
Python des neiges
Auteur: Tran Bao   Matricule : 000516401
Date: 12 novembre 2020
Petit jeu du type jeu d’évasion (escape game) dans lequel le joueur commande au clavier les déplacements
d’un personnage au sein d’un « château » représenté en plan. Le château est constitué de cases vides
(pièces, couloirs), de murs, de portes, que le personnage ne pourra franchir qu’en répondant à des questions,
d’objets à ramasser, qui l’aideront à trouver les réponses à ces questions et de la case de sortie / quête du château.
Le but du jeu est d’atteindre cette dernière.
"""
import turtle   # module pour dessiner le plan, pour afficher des messages et des objets et pour poser des questions
from CONFIGS import *  #valeurs préinitialisées


def couleur(x):
    """
    Associer une case à une couleur
    Entrée : La valeur de la case
    Résultat : La couleur de la case
    """
    couleur_case = 0
    if x == 0:
        couleur_case = COULEUR_COULOIR
    elif x == 1:
        couleur_case = COULEUR_MUR
    elif x == 2:
        couleur_case = COULEUR_OBJECTIF
    elif x == 3:
        couleur_case = COULEUR_PORTE
    elif x == 4:
        couleur_case = COULEUR_OBJET
    return couleur_case


def lire_matrice(fichier):
    """
    Transformer un fichier (le plan du château )en matrice
    Entrée : Le fichier du plan
    Résultat : La matrice
    """
    with open(fichier) as file:
        return [[int(i) for i in ligne.split()] for ligne in file]  #Transformer en liste le fichier et chaque ligne du plan dans le fichier


def tracer_carre(dimension):
    """
    Dessiner un carré
    Entrée : La longueur d'un côté du carré
    Résultat : Un carré
    """
    for i in range(4):    #Trace une ligne pour chaque côté du carré
        turtle.forward(dimension)
        turtle.right(90)


def tracer_case(case, couleur, pas):
    """
    Tracer une case d'une couleur donnée à des coordonnées données
    Entrée case: Les coordonnées sous forme de tuple
    Entrée couleur: La couleur
    Entrée pas: La longueur d'un côté de la case
    Résultat : La case est tracée
    """
    turtle.tracer(False)
    turtle.up()
    turtle.goto(case)
    turtle.down()
    turtle.color(couleur)
    turtle.begin_fill()
    tracer_carre(pas)   #Appelle la fonction tracer_carre pour tracer un carré
    turtle.end_fill()
    turtle.ht()

def coordonnees(case, pas):
    """
    Changer une case de la matrice en des coordonnées
    Entrée case: Case de la matrice
    Entrée pas: Dimension d'une case
    Résultat : Des coordonnées sous forme de tuple
    """
    coy = 50
    cox = -240
    for i in range(case[0]):
        coy -= pas
    for y in range(case[1]):
        cox += pas
    return (cox, coy)


def coordonnees_point(case, pas):
    """
    Changer la case où se trouve le point du jouer en coordonnées
    Entrée case: La case où se trouve le point du jouer
    Entrée pas: Dimension d'une case
    Résultat :  Des coordonnées sous forme de tuple
    """
    pts = list(coordonnees(case, pas))
    return (pts[0] + (pas // 2), pts[1] - (pas // 2))    #diviser le pas par 2 pour que le point soit au milieux de la case


def calculer_pas(matrice):
    """
    Calculer la dimension d'une case à partir de la matrice par rapport à la zone destinée à l'affichage
    Entrée matrice: La matrice du plan de chateau
    Résultat : Le pas c'est à dire la dimension d'une case
    """
    return (min(290 / len(matrice), 440 / len(matrice[1])))


def afficher_plan(matrice):
    """
    Afficher le plan du château + afficher le titre de l'inventaire
    Entrée matrice: La matrice du plan de chateau
    Résultat : Le plan est dessiné
    """
    pas = calculer_pas(matrice)
    for ligne in range(len(matrice)):
        for colonne in range(len(matrice[ligne])):
            tracer_case(coordonnees((ligne, colonne), pas), couleur(matrice[ligne][colonne]), pas) #Appelle la fonction tracer_case pour chaque case
    inventaire.ht()
    inventaire.up()
    inventaire.goto(50,50)
    inventaire.write("Inventaire : ")


def creer_dictionnnaire_des_objets(fichier):
    """
    Tranformer les fichiers restants (dico_objet et dico_portes) en dictionnaire
    Entrée fichier: Le fichier demandé
    Résultat : Le dictionnaire du fichier
    """
    objet = {}       #initialisation d'un dictionnaire vide
    with open(fichier, encoding=" UTF -8 ") as file:
        for chaine in file:
            a, b = eval(chaine)
            objet[a] = b   #Chaque a est la clé de chaque b
    return (objet)


def ramasser_objets(x, y):
    """
    Ramasser un objet + le rajouter dans l'inventaire + afficher un message
    Entrée x: La ligne où se trouve l'objet
    Entrée y: La colonne où se trouve l'objet
    Résultat : L'objet est ramassé et tranféré dans l'inventaire et un message est affiché
    """
    global compteur
    liste_objet = creer_dictionnnaire_des_objets(fichier_objets)
    objets.up()
    objets.goto(-220, 220)
    objets.clear()            #faire disparaitre l'ancien message
    objets.write(" Vous avez trouvé :" + liste_objet[x, y])
    inventaire.up()
    inventaire.goto(50, 50 - compteur)
    inventaire.write("N°" + str(compteur // 10) + ": " + liste_objet[x, y])
    compteur += 10                #valeur permettant de changer la place de chaque objet dans l'inventaire
    matrice[x][y] = 0      #chaque objet trouvé rend vide la case où se trouve l'objet
    tracer_case(coordonnees((x, y), pas), couleur(matrice[x][y]), pas)  #retracer la case vide pour changer la couleur de la case


def poser_question(matrice,case,mouvement):
    """
    Poser une la question et si la réponse est correct, la porte s'ouvre. Un message est affiché indiquant l'état de la porte.
    Entrée matrice : La matrice du château
    Entrée case : La case où il y a une porte
    Entrée mouvement : Le pas
    Résultat : Si la réponse est correct, la porte s'ouvre
               Sinon la porte reste fermé
    """
    objets.up()
    objets.goto(-220, 220)
    objets.down()
    objets.clear()         #faire disparaitre l'ancien message
    objets.write("Cette porte est fermée.")
    x,y = case
    question = creer_dictionnnaire_des_objets(fichier_questions)
    reponse = turtle.textinput("question" , question[case][0])        #utilisation de la fonction turtle.textinput pour poser la question
    turtle.listen()
    if reponse == question[case][1]:           #si la reponse donnée par le joueur correspond à la réponse attendue ( se trouvant dans question[case][1])
        objets.clear()     #faire disparaitre l'ancien message
        objets.write("Brooum, la porte s'ouvre")
        matrice[x][y] = 0        #la porte s'ouvre donc la case devient vide pour laisser passer le joueur
        tracer_case(coordonnees((x, y), mouvement), couleur(matrice[x][y]), mouvement)   #retracer la case vide pour changer la couleur de la case
    else:
        objets.clear()
        objets.write(" Rien ne se passe ")


def deplacer( position):
    """

    :param position:
    :return:
    """

    """
    Déplacer le pion du joueur en fonction de la touche appuyée par le joueur
    Entrée position: Case où le joueur se trouve
    Résultat : Le joueur  aller à droite, à gauche, en haut ou en bas en fonction de la commande effectuée
    """
    point.up()
    point.goto(coordonnees_point(position, pas))
    point.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)        #faire apparaitre le point du joueur
    turtle.listen()            #attendre une action du joueur
    turtle.onkeypress(deplacer_gauche, "Left")
    turtle.onkeypress(deplacer_droite, "Right")
    turtle.onkeypress(deplacer_haut, "Up")
    turtle.onkeypress(deplacer_bas, "Down")
    turtle.mainloop()  #recommencer la fonction


def deplacer_gauche():
    """
    Le point se déplace à gauche
    """
    global matrice, position, pas, point   #appeler matrice, position, pas, point
    turtle.onkeypress(None, "Left") # Désactive la touche Left
    point.clear()
    position = list(position)
    if matrice[position[0]][position[1] - 1] == 3:  #Quand il y a une porte, appeler la fonction poser_question
        poser_question(matrice,((position[0]),(position[1]- 1)),pas)
    if position[1] > 0 and matrice[position[0]][position[1] - 1] != 1 and matrice[position[0]][position[1]-1] != 3 :  # traitement associé à la flèche gauche appuyée par le joueur
        if matrice[position[0]][position[1] - 1] == 4:    #Quand il y a un objet, appeler la fonction ramasser_objet
            ramasser_objets((position[0]), (position[1] - 1))
        if matrice[position[0]][position[1] - 1] == 2:    #Quand le joueur arrive à la fin, envoyer un message
            objets.clear()
            objets.write("C'est gagné")
        position[1] -= 1
    point.goto(coordonnees_point(tuple(position), pas))
    point.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)    #faire apparaitre le point du joueur
    turtle.onkeypress(deplacer_gauche, "Left")


def deplacer_droite():
    """
    Le point se déplace à droite
    """
    global matrice, position, pas, point
    turtle.onkeypress(None, "Right") # Désactive la touche Right
    point.clear()
    position = list(position)
    if matrice[position[0]][position[1] + 1] == 3:      #Quand il y a une porte, appeler la fonction poser_question
        poser_question(matrice,((position[0]), (position[1] + 1)) , pas)
    if position[1] < len(matrice[0]) and matrice[position[0]][position[1] + 1] != 1 and matrice[position[0]][position[1]+ 1] != 3 : # traitement associé à la flèche doite appuyée par le joueur
        if matrice[position[0]][position[1] + 1] == 4:     #Quand il y a un objet, appeler la fonction ramasser_objet
            ramasser_objets((position[0]), (position[1] + 1))
        if matrice[position[0]][position[1] + 1] == 2:     #Quand le joueur arrive à la fin, envoyer un message
            objets.clear()
            objets.write("C'est gagné")
        position[1] += 1
    point.goto(coordonnees_point(tuple(position), pas))
    point.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)      #faire apparaitre le point du joueur
    turtle.onkeypress(deplacer_droite, "Right")


def deplacer_haut():
    """
    Le point se déplace en haut
    """
    global matrice, position, pas, point
    turtle.onkeypress(None, "Up")    # Désactive la touche Up
    point.clear()
    position = list(position)
    if matrice[position[0] - 1][position[1]] == 3:        #Quand il y a une porte, appeler la fonction poser_question
        poser_question(matrice,((position[0] - 1), (position[1])) , pas)
    if position[0] > 0 and matrice[position[0] - 1][position[1]] != 1 and matrice[position[0] - 1][position[1]] != 3: # traitement associé à la flèche haut appuyée par le joueur
        if matrice[position[0] - 1][position[1]] == 4:        #Quand il y a un objet, appeler la fonction ramasser_objet
            ramasser_objets((position[0] - 1), (position[1]))
        if  matrice[position[0] - 1][position[1]] == 2:     #Quand le joueur arrive à la fin, envoyer un message
            objets.clear()
            objets.write("C'est gagné")
        position[0] -= 1
    point.goto(coordonnees_point(tuple(position), pas))
    point.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)   #faire apparaitre le point du joueur
    turtle.onkeypress(deplacer_haut, "Up")


def deplacer_bas():
    """
    Le point se déplace en bas
    """
    global matrice, position, pas, point
    turtle.onkeypress(None, "Down")   # Désactive la touche Down
    point.clear()
    position = list(position)
    if matrice[position[0] + 1][position[1]] == 3 :       #Quand il y a une porte, appeler la fonction poser_question
        poser_question(matrice,((position[0] + 1), (position[1])),pas)
    if position[0] < len(matrice) and matrice[position[0] + 1][position[1]] != 1 and matrice[position[0] + 1][position[1]] != 3: # traitement associé à la flèche bas appuyée par le joueur
        if matrice[position[0] + 1][position[1]] == 4:     #Quand il y a un objet, appeler la fonction ramasser_objet
            ramasser_objets((position[0] + 1), (position[1]))
        if matrice[position[0] + 1][position[1]] == 2:     #Quand le joueur arrive à la fin, envoyer un message
            objets.clear()
            objets.write("C'est gagné")
        position[0] += 1
    point.goto(coordonnees_point(tuple(position), pas))
    point.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)    #faire apparaitre le point du joueur
    turtle.onkeypress(deplacer_bas, "Down")


compteur = 10                 #valeur permettant de décaller chaque objet affiché dans l'inventaire
objets = turtle.Turtle()       #définir un turtle
objets.ht()
inventaire = turtle.Turtle() #définir un turtle
inventaire.ht()
point = turtle.Turtle()            #définir un turtle
point.ht()
matrice = lire_matrice(fichier_plan)
position = (0,1)
pas = calculer_pas(matrice)
print(afficher_plan(matrice))
print(deplacer(position))


