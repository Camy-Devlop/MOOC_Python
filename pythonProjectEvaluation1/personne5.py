""" Projet mooc INFO-H-100
    Auteurs : Husson Leopold, Usciuc Nicolas
    Matricules : 502703, 512886
    Escape game où nous contrôlons un personnage dans un labyrinthe. Pour atteindre la sortie, le héros devra résoudre
    des énigmes et pourra trouver des indices pour répondre à celles-ci.
    """

from CONFIGS import *
import turtle

""" Les différentes turtle utilisées"""
crayon  = turtle.Turtle() #Turtle traçant le chateau
crayon.hideturtle()
personnage = turtle.Turtle() # Turtle déplaçant le personnage
personnage.hideturtle()
affichage = turtle.Turtle() # Turtle affichant l'objet ramassé
affichage.hideturtle()
inventaire = turtle.Turtle() #Turtle affichant les objets ramassés dans l'inventaire
inventaire.hideturtle()
turtle.tracer(0)


def lire_matrice(fichier):
    """
    Lis un fichier en argument et le transforme en une matrice
    """
    with open(fichier) as infile:
        return [[int(colonne) for colonne in ligne.split()] for ligne in infile]


def calculer_pas(matrice):
    """
    Calcule la longueur du coté des cases qui composeront le chateau à partir d'une matrice
    """
    longueur_mat = len(matrice)
    largeur_mat = len(matrice[0])
    largeur_chateau = abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])
    longueur_chateau = abs(ZONE_PLAN_MAXI[1])+ abs(ZONE_PLAN_MINI[1])
    return min(longueur_chateau/longueur_mat, largeur_chateau/largeur_mat)

def coordonnees(case, pas):
    """
    Trouve les coordonnées du coin inférieur gauche de la case mise en argument
    """
    x = ZONE_PLAN_MINI[0] + case[1] * pas
    y = ZONE_PLAN_MAXI[1] - (case[0] + 1) * pas
    return (x,y)

def tracer_carre(dimension):
    """
    Trace un carré dans la dimension donnée en argument
    """
    for i in range(4):
        crayon.forward(dimension)
        crayon.left(90)

def tracer_case(case, couleur, pas):
    """
    Trace une case au bon endroit dans chateau dont le pas est sa dimension et dans la couleur donnée en argument
    """
    x, y = coordonnees(case, pas)
    crayon.up()
    crayon.goto(x,y)
    crayon.down()
    crayon.begin_fill()
    crayon.color('White', couleur)
    tracer_carre(pas)
    crayon.end_fill()


def afficher_plan(matrice):
    """
    Affiche le plan du chateau à partir de la matrice donnée en argument
    """
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            case = (i,j)
            if matrice[i][j] == 0 :
                couleur = COULEUR_CASES
            elif matrice[i][j] == 1 :
                couleur = COULEUR_MUR
            elif matrice[i][j] == 2 :
                couleur = COULEUR_OBJECTIF
            elif matrice[i][j] == 3 :
                couleur = COULEUR_PORTE
            else :
                couleur = COULEUR_OBJET
            tracer_case(case,couleur, pas)


def creer_dictionnaire_des_objets(fichier_des_objets):
    """
    Créé un dictionnaire à partir du fichier donné en argument
    """
    dictionnaire_objets = {}
    with open(fichier_des_objets, encoding= 'UTF-8') as f :
        for i in f :
            a,b = eval(i)
            dictionnaire_objets.setdefault(a,b)
    return dictionnaire_objets


def creer_dictionnaire_des_portes(fichier_des_portes):
    """
    Créé un dictionnaire à partir du fichier donné en argument
    """
    dictionnaire_portes = {}
    with open(fichier_des_portes, encoding= 'UTF-8') as f :
        for i in f :
            a,b = eval(i)
            dictionnaire_portes.setdefault(a,b)
    return dictionnaire_portes


def ramasser_objets(matrice, dico_objet,coord):
    """
    Affiche l'objet ramassé et l'ajoute à l'inventaire lorsque les coordonnées du personnage en argument sont les mêmes que
     les coordonnées de la case objet
    """
    affichage.goto(-240, 290)
    affichage.clear()
    ensemble = set()
    if matrice[coord[0]][coord[1]] == 4:
        for i in dico_objet :
            if coord == i:
                affichage.write("Vous avez trouvé : " + dico_objet[i], False, align="left", font=("Arial", 16, "normal"))
                ensemble |= {dico_objet[i]}
                tracer_case(coord, COULEUR_CASES, pas)
        for j in ensemble :
            inventaire.setheading(270)
            inventaire.up()
            inventaire.forward(30)
            inventaire.down
            inventaire.write(j, False, align="left", font=("Arial", 12, "normal"))
        matrice[coord[0]][coord[1]] = 0


def poser_question(matrice,case,mouvement):
    """
    Affiche la question située sur une case de type porte si le personnage essaie de la traverser et permet au personnage
    de passer si la réponse à l'énigme est correct
    """
    global position
    affichage.goto(-240, 290)
    affichage.clear()
    nouvelle_case = (position[0] + mouvement[0], position[1] + mouvement[1])
    if matrice[case[0]][case[1]] == 3 :
        affichage.write("Cette porte est fermée", False, align="left", font=("Arial", 20, "normal"))
        for i in dico_portes :
            if case == i :
                if dico_portes[i][1] == turtle.textinput('énigme', dico_portes[i][0]) :
                    turtle.listen()
                    matrice[case[0]][case[1]] = 0
                    affichage.clear()
                    affichage.write("La porte s'ouvre", False, align="left", font=("Arial", 20, "normal"))
                    tracer_case(case, COULEUR_CASES, pas)
                else :
                    turtle.listen()
                    affichage.clear()
                    affichage.write('Mauvaise réponse', False, align="left", font=("Arial", 20, "normal"))
                    nouvelle_case = position
    return nouvelle_case


def deplacer(matrice, position, mouvement):
    """
    Calcule et renvoie la nouvelle position du personnage par rapport à sa position en argument à laquelle on ajoute le tuple mouvement et analyse
    les éléments de la matrice du plan pour comprendre les différentes cases du chateau
    """
    nouvelle_position = (position[0] + mouvement[0], position[1] + mouvement[1])
    if nouvelle_position[0] < ZONE_PLAN_MINI[0] or nouvelle_position[0] >= ZONE_PLAN_MAXI[0] :
        nouvelle_position = position
    elif nouvelle_position[1] < ZONE_PLAN_MINI[1] or nouvelle_position[1] >= ZONE_PLAN_MAXI[1] :
        nouvelle_position = position
    else :
        coord_mat_perso = (int(((nouvelle_position[1]-ZONE_PLAN_MAXI[1])/-pas) - 1),int((nouvelle_position[0] - ZONE_PLAN_MINI[0])/pas))
        if matrice[coord_mat_perso[0]][coord_mat_perso[1]] == 1 :
            nouvelle_position = position
        elif matrice[coord_mat_perso[0]][coord_mat_perso[1]] == 2 :
            affichage.clear()
            affichage.write(' Bravo ! Vous avez gagné !', False, align="left", font=("Arial", 20, "normal"))
        elif matrice[coord_mat_perso[0]][coord_mat_perso[1]] == 4 :
            ramasser_objets(matrice, dico_objet, coord_mat_perso)
        elif matrice[coord_mat_perso[0]][coord_mat_perso[1]] == 3 :
            nouvelle_position = poser_question(matrice, coord_mat_perso, mouvement)
    return nouvelle_position


def deplacer_droite():
    """
    Fonction faisant se déplacer le personnage vers la droite
    """
    global position
    turtle.onkeypress(None, "Right")
    personnage.setheading(0)
    mouvement = (pas,0)
    position = deplacer(matrice, position, mouvement)
    personnage.goto((position[0] + pas/2),(position[1]+ pas/2))
    personnage.clear()
    personnage.dot(pas*RATIO_PERSONNAGE, COULEUR_PERSONNAGE)
    turtle.onkeypress(deplacer_droite, "Right")


def deplacer_gauche() :
    """
    Fonction faisant se déplacer le personnage vers la gauche
    """
    global position
    turtle.onkeypress(None, "Left")
    personnage.setheading(180)
    mouvement = (-pas,0)
    position = deplacer(matrice, position, mouvement)
    personnage.goto((position[0] + pas/2),(position[1]+ pas/2))
    personnage.clear()
    personnage.dot(pas*RATIO_PERSONNAGE, COULEUR_PERSONNAGE)
    turtle.onkeypress(deplacer_gauche, "Left")


def deplacer_haut() :
    """
    Fonction faisant se déplacer le personnage vers le haut
    """
    global position
    turtle.onkeypress(None, "Up")
    personnage.setheading(90)
    mouvement = (0,pas)
    position = deplacer(matrice, position, mouvement)
    personnage.goto((position[0] + pas/2),(position[1]+ pas/2))
    personnage.clear()
    personnage.dot(pas*RATIO_PERSONNAGE, COULEUR_PERSONNAGE)
    turtle.onkeypress(deplacer_haut, "Up")


def deplacer_bas():
    """
    Fonction faisant se déplacer le personnage vers le bas
    """
    global position
    turtle.onkeypress(None, "Down")
    personnage.setheading(270)
    mouvement = (0,-pas)
    position = deplacer(matrice, position, mouvement)
    personnage.goto((position[0] + pas/2),(position[1]+ pas/2))
    personnage.clear()
    personnage.dot(pas*RATIO_PERSONNAGE, COULEUR_PERSONNAGE)
    turtle.onkeypress(deplacer_bas, "Down")


""" Informations pour tracer le chateau et afficher le chateau """
matrice = lire_matrice(fichier_plan)
pas = calculer_pas(matrice)
print(afficher_plan(matrice))

"""Informations pour tracer le personnage et le mettre sur la case départ"""
position = (1,0)#(ZONE_PLAN_MINI[0] + POSITION_DEPART[1] * pas, ZONE_PLAN_MAXI[1] - (POSITION_DEPART[0] + 1) * pas)
personnage.goto(position[0] + pas/2,position[1]+ pas/2)
personnage.clear()
personnage.dot(pas*RATIO_PERSONNAGE, COULEUR_PERSONNAGE)


"""Les différents dictionnaires utilisés"""
dico_objet = creer_dictionnaire_des_objets(fichier_objets)
dico_portes = creer_dictionnaire_des_portes(fichier_questions)


""""Espace dédié à l'inventaire"""
inventaire.goto(80, 200)
inventaire.clear()
inventaire.write('Inventaire :', False, align="left", font=("Arial", 16, "normal"))


""" Fonctions pour déplacer le personnage avec les flèches du clavier"""
turtle.listen()
turtle.onkeypress(deplacer_droite, 'Right')
turtle.onkeypress(deplacer_gauche, 'Left')
turtle.onkeypress(deplacer_haut, 'Up')
turtle.onkeypress(deplacer_bas, 'Down')
turtle.mainloop()