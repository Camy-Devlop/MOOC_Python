"""" Auteurs du projet: Mathieu Massart (matricule: 521670) et Maxime Martin (matricule: 512885)
    Date de Remise: 15 Novembre 2020
    But de ce projet:
    le programme suivant permet de créer un 'escape game' ou l' on déplace un personnage dans un Labyrinthe, le joueur
    pourra récupérer des indices sur certaines cases du plateau qui lui permettront de répondre correctement aux
    questions posées aux différentes portes du labyrinthe.Son but est d' en sortir.
"""

from CONFIGS import *
import turtle
# coordonées minimales et maximales dans le plan (turtle)
X_min = ZONE_PLAN_MINI[0]
Y_min = ZONE_PLAN_MINI[1]
X_max = ZONE_PLAN_MAXI[0]
Y_max = ZONE_PLAN_MAXI[1]
#-----------------------------------------------------------------------------------------------------------------------

def lire_matrice(fichier_plan) :
    # transforme un fichier 'matrice'(en entrée) en liste de liste qui va representer notre plan du chateu
    liste_totale = []
    for ligne in open(fichier_plan) :
        liste_ligne = ligne.split(' ', -1)              # considère les espace comme séparation entre chaque valeur
        liste_ligne_int = []
        for i in range(len(liste_ligne)) :              # transforme chaque valeur en entier
            toto = int(liste_ligne[i])
            liste_ligne_int.append(toto)
        liste_totale.append(liste_ligne_int)            # remplit la liste avec les valeurs de la matrice
    return liste_totale

#-----------------------------------------------------------------------------------------------------------------------

def calculer_pas(matrice_en_liste, X_max, X_min, Y_max, Y_min) :
    """"""
    # calcule la taille des cases de notre plan à partir de la taille du plan
    longueur_horizontale_matrice = len(matrice_en_liste[1])
    longueur_verticale_matrice = len(matrice_en_liste)
    longueur_horizontale_turtle = (X_max - X_min)
    longueur_verticale_turtle = (Y_max - Y_min)
    longueur_pas_horizontale = longueur_horizontale_turtle / longueur_horizontale_matrice
    longueur_pas_verticale = longueur_verticale_turtle / longueur_verticale_matrice
    taille_case = min(longueur_pas_horizontale, longueur_pas_verticale)             # prend le minimum pour que toutes
                                                                                    # les cases rentrent dans l'espace
                                                                                    #  défini pour le plan
    return taille_case

#-----------------------------------------------------------------------------------------------------------------------

def coordonnees(case, pas, Xmin, Ymin, nombre_de_lignes) :
    # calcule la position du coin inferieur gauche de chaque case
    coordonnees_X = Xmin + ((case[1]) * pas)
    coordonnees_Y = Ymin + ((nombre_de_lignes - case[0] -1 ) * pas)
    coordonnees = (coordonnees_X, coordonnees_Y)
    return coordonnees

#-----------------------------------------------------------------------------------------------------------------------

def tracer_carre(dimensions):
    # trace le contour des carrés qui servent de cases au plan du chateau selon les dimensions
    turtle.forward(dimensions)
    turtle.left(90)
    turtle.forward(dimensions)
    turtle.left(90)
    turtle.forward(dimensions)
    turtle.left(90)
    turtle.forward(dimensions)
    turtle.left(90)

#-----------------------------------------------------------------------------------------------------------------------

def tracer_case(case,couleur,pas):
    # trace une case sur le plan et leur donne la couleur qui correspond à leur rôle
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.up()
    turtle.goto(case)
    turtle.down()
    turtle.fillcolor(couleur)
    turtle.pencolor('white')
    turtle.begin_fill()
    tracer_carre(pas)
    turtle.end_fill()

#-----------------------------------------------------------------------------------------------------------------------

def afficher_plan(matrice, X_max, X_min, Y_max, Y_min) :
    # affiche le plan final du plateau de jeu
    for i in range(len(matrice)) :
        for j in range(len(matrice[1])) :
            pas = calculer_pas(matrice , X_max, X_min, Y_max, Y_min)
            case = coordonnees((i,j), pas, X_min, Y_min, len(matrice))      # 'case' contient les coordonnées du
                                                                            # coin inférieur gauche du carré
            if matrice[i][j]==0:
                couleur = COULEUR_CASES
            elif matrice[i][j]==1:
                couleur = COULEUR_MUR
            elif matrice[i][j]==2:
                couleur = COULEUR_OBJECTIF
            elif matrice[i][j]==3:
                couleur = COULEUR_PORTE
            elif matrice[i][j]==4:
                couleur = COULEUR_OBJET
            tracer_case(case, couleur, pas)
    return(pas)
#-----------------------------------------------------------------------------------------------------------------------

def deplacer_dans_matrice(mouvement_matrice, matricef, position_actuelle_matrice, liste_objets, dico_objets):
    # détermine si le mouvement est autorisé dans la matrice (liste de listes)
    # en fonction des valeurs de chaque case (mur, case vide, porte, objet)
    position_potentielle = (position_actuelle_matrice[0]+mouvement_matrice[0], position_actuelle_matrice[1]+mouvement_matrice[1])
    if position_potentielle[0] >= 0 and position_potentielle[1] >= 0:       # n'accepte pas que les indices décrivant
                                                                            # la position dans la matrice deviennent négatifs
        valeur_case = matricef[position_potentielle[0]][position_potentielle[1]]
        if valeur_case == 1 :                           # Mur, pas de mouvement possible
            return False, position_potentielle
        if valeur_case == 0 :                           # Couloir, le mouvement est possible
            return True, position_potentielle
        if valeur_case == 2 :                           # Fin du jeu, le joueur a gagné
            ecrire_txt_annonces(POINT_AFFICHAGE_ANNONCES, 'Win !!!')
            return True, position_potentielle
        if valeur_case == 4 :                           # Objet trouvé, mouvement possible, il faut mettre l'objet
                                                        # dans la liste des objets ramassés
            ecrire_txt_annonces(POINT_AFFICHAGE_ANNONCES, "Vous avez touvé un indice")
            ramasser_objet(matricef, liste_objets, dico_objets, position_potentielle)
            return True, position_potentielle
        if valeur_case == 3 :                           # Porte, il faut poser la question et ne laisser passer
                                                        # que si la réponse est correcte par rapport au dictionnaire
            reponse_joueur, question_reponse= poser_question(matricef, position_potentielle, dico_portes)
            if reponse_joueur == question_reponse[1]:   # Réponse correcte
                ecrire_txt_annonces(POINT_AFFICHAGE_ANNONCES, "Bonne réponse")
                matricef[position_potentielle[0]][position_potentielle[1]] = 0
                return True, position_potentielle
            else:                                       # Réponse fausse, pas de mouvement autorisé
                ecrire_txt_annonces(POINT_AFFICHAGE_ANNONCES, "Mauvaise réponse")
                return False, position_potentielle
    else :                                              # empêche de sortir de la matrice par le haut et la
                                                        # gauche (empèche de sortir du plan à l' entrée,
                                                        # (dans ces cas les indices dans la matrice deviennent négatifs)
        return False, position_potentielle

#-----------------------------------------------------------------------------------------------------------------------

def deplacer_dans_turtle(mouvement_turtle, position_actuelle_turtle, pas):
    # définit le mouvement dans turtle si il est accepté dans la matrice
    nouvelle_position_turtle = (position_actuelle_turtle[0] + (mouvement_turtle[0]*pas), position_actuelle_turtle[1] + (mouvement_turtle[1]*pas))
    return nouvelle_position_turtle

#-----------------------------------------------------------------------------------------------------------------------

def deplacer_droite():
    # déplace le personnage vers la droite dans le plan
    turtle.onkeypress(None, "Right")                            # Désactive la touche Right (empêche le bug du programme
                                                                # lorsqu'on appuie trop vite sur la touche)
    # pas de passage par paramètres (imposé par onkeypress)
    global matricef, position_actuelle_matrice, position_actuelle_turtle, pas, liste_objets, dico_objets
    mouvement_matrice = (0,1)
    mouvement_turtle = (1,0)                    # correspond à la direction du mouvement (encore à multiplier par
                                                # le pas pour obtenir le mouvement "réel" dans turtle)
    ancienne_position_turtle = (position_actuelle_turtle[0]-0.5*pas, position_actuelle_turtle[1]-0.5*pas)
    decision, position_potentielle_matrice = deplacer_dans_matrice(mouvement_matrice, matricef, position_actuelle_matrice, liste_objets, dico_objets)
    if decision == True:
        position_actuelle_matrice = position_potentielle_matrice
        position_actuelle_turtle = deplacer_dans_turtle(mouvement_turtle,position_actuelle_turtle, pas)
        tracer_case(ancienne_position_turtle, COULEUR_VUE, pas)
        point_du_personnage = personnage(pas, position_actuelle_turtle)
    turtle.onkeypress(deplacer_droite, "Right")                 # Réactive la touche Right (empêche le bug du
                                                                # programme lorsqu' on appui trop vite sur la touche)

#---------------------------------------

def deplacer_gauche():
    # déplace le personnage vers la gauche dans le plan
    turtle.onkeypress(None, "Left")                             # Désactive la touche Left (empêche le bug du programme
                                                                # lorsqu'on appui etrop vite sur la touche)
    # pas de passage par paramètres (imposé par onkeypress)
    global matricef, position_actuelle_matrice, position_actuelle_turtle, pas, liste_objets, dico_objets
    mouvement_matrice = (0,-1)
    mouvement_turtle = (-1,0)                   # correspond à la direction du mouvement (encore à multiplier par
                                                # le pas pour obtenir le mouvement "réel" dans turtle)
    ancienne_position_turtle = (position_actuelle_turtle[0]-0.5*pas, position_actuelle_turtle[1]-0.5*pas)
    decision, position_potentielle_matrice = deplacer_dans_matrice(mouvement_matrice, matricef, position_actuelle_matrice, liste_objets, dico_objets)
    if decision == True:
        position_actuelle_matrice = position_potentielle_matrice
        position_actuelle_turtle = deplacer_dans_turtle(mouvement_turtle,position_actuelle_turtle, pas)
        tracer_case(ancienne_position_turtle, COULEUR_VUE, pas)
        point_du_personnage = personnage(pas, position_actuelle_turtle)
    turtle.onkeypress(deplacer_gauche, "Left")                  # Réactive la touche Left (empêche le bug du programme
                                                                # lorsqu'on appuie trop vite sur la touche)

#---------------------------------------

def deplacer_haut():
    # déplace le personnage vers le haut dans le plan
    turtle.onkeypress(None, "Up")                               # Désactive la touche Up (empêche le bug du programme
                                                                # lorsqu'on appuie trop vite sur la touche)
    # pas de passage par paramètres (imposé par onkeypress)
    global matricef, position_actuelle_matrice, position_actuelle_turtle, pas, liste_objets, dico_objets
    mouvement_matrice = (-1,0)
    mouvement_turtle = (0,1)                    # correspond à la direction du mouvement (encore à multiplier par
                                                # le pas pour obtenir le mouvement "réel" dans turtle)
    ancienne_position_turtle = (position_actuelle_turtle[0]-0.5*pas, position_actuelle_turtle[1]-0.5*pas)
    decision, position_potentielle_matrice = deplacer_dans_matrice(mouvement_matrice, matricef, position_actuelle_matrice, liste_objets, dico_objets)
    if decision == True:
        position_actuelle_matrice = position_potentielle_matrice
        position_actuelle_turtle = deplacer_dans_turtle(mouvement_turtle,position_actuelle_turtle, pas)
        tracer_case(ancienne_position_turtle, COULEUR_VUE, pas)
        point_du_personnage = personnage(pas, position_actuelle_turtle)
    turtle.onkeypress(deplacer_haut, "Up")                      # Réactive la touche Up (empêche le bug du programme
                                                                # lorsqu'on appuie trop vite sur la touche)


#---------------------------------------

def deplacer_bas():
    # déplace le personnage vers le bas dans le plan
    turtle.onkeypress(None, "Down")                             # Désactive la touche Down (empêche le bug du programme
                                                                # lorsqu' on appui trop vite sur la touche)
    # pas de passage par paramètres (imposé par onkeypress)
    global matricef, position_actuelle_matrice, position_actuelle_turtle, pas, liste_objets, dico_objets
    mouvement_matrice = (1, 0)
    mouvement_turtle = (0,-1)                   # correspond à la direction du mouvement (encore à multiplier par
                                                # le pas pour obtenir le mouvement "réel" dans turtle)
    ancienne_position_turtle = (position_actuelle_turtle[0]-0.5*pas, position_actuelle_turtle[1]-0.5*pas)
    decision, position_potentielle_matrice = deplacer_dans_matrice(mouvement_matrice, matricef, position_actuelle_matrice, liste_objets, dico_objets)
    if decision == True:
        position_actuelle_matrice = position_potentielle_matrice
        position_actuelle_turtle = deplacer_dans_turtle(mouvement_turtle,position_actuelle_turtle, pas)
        tracer_case(ancienne_position_turtle, COULEUR_VUE, pas)
        point_du_personnage = personnage(pas, position_actuelle_turtle)
    turtle.onkeypress(deplacer_bas, "Down")                     # Réactive la touche Down (empêche le bug du programme
                                                                # lorsqu'on appuie trop vite sur la touche)


#-----------------------------------------------------------------------------------------------------------------------
def personnage(pas, position_actuelle_tur):
    # trace le personnage sur le plan proportionnellement à la taille de la case (pas)
    rayon= RATIO_PERSONNAGE*pas
    turtle.speed('fastest')
    turtle.up()
    turtle.goto(position_actuelle_tur)
    turtle.down()
    turtle.dot(rayon,COULEUR_PERSONNAGE)
    turtle.end_fill()

#-----------------------------------------------------------------------------------------------------------------------

def creer_dictonnaire_des_objets(fichier):
    dico ={}
    for i in open(fichier):
        t, u = eval(i)
        dico[t] = u
    return dico

#-----------------------------------------------------------------------------------------------------------------------
def ramasser_objet(matricef, liste_objets, dico_objets, position_matrice) :
    # prend l'objet et l'ajoute à la liste d'objets ramassés
    matricef[position_matrice[0]][position_matrice[1]] = 0      # Transforme la case en couloir (objet ramassé qu'une fois)
    objets = dico_objets.get(position_matrice)                  # Récupère l'objet dans le dictionnaire sur base de la
                                                                # clé qui est la position dans la matrice
    liste_objets.append(objets)
    ecrire_txt_inventaire((POINT_AFFICHAGE_INVENTAIRE[0], POINT_AFFICHAGE_INVENTAIRE[1]-(len(liste_objets)-1)*15), liste_objets[-1])

#-----------------------------------------------------------------------------------------------------------------------
def poser_question(matricef,position_matrice, dico_portes):
    # pose une question et attend une réponse
    if matricef[position_matrice[0]][position_matrice[1]] == 3 :
        ecrire_txt_annonces(POINT_AFFICHAGE_ANNONCES, "Cette porte est fermée.")
        question_reponse = dico_portes.get(position_matrice)
        reponse_joueur = turtle.textinput("Qestion", question_reponse[0])
        turtle.listen()
        return reponse_joueur, question_reponse
#-----------------------------------------------------------------------------------------------------------------------
def ecrire_txt_annonces(coordonnees, message) :
    # écrit les messages dans la barre d' annonce
    tracer_contour((coordonnees[0]-15, coordonnees[1]-15), 480, 40)
    turtle.up()
    turtle.setpos(coordonnees)
    turtle.down()
    turtle.color("Black")
    turtle.write(message)
#------------------------------------------------------------------
def ecrire_txt_inventaire(coordonnees, message) :
    # écrit les messages (indices) dans l' inventaire
    turtle.up()
    turtle.setpos(coordonnees)
    turtle.down()
    turtle.color("Black")
    turtle.write(message)

#-----------------------------------------------------------------------------------------------------------------------
def tracer_contour(position_initial, longueur, hauteur):
    # trace la zone d'annonce et permet la réinitialisation de la zone par retraçage d'une case blanche
    # au cas où un message y était déjà présent
    turtle.up()
    turtle.goto(position_initial)
    turtle.down()
    turtle.fillcolor('White')
    turtle.pencolor('Black')
    turtle.begin_fill()
    turtle.forward(longueur)
    turtle.left(90)
    turtle.forward(hauteur)
    turtle.left(90)
    turtle.forward(longueur)
    turtle.left(90)
    turtle.forward(hauteur)
    turtle.left(90)
    turtle.end_fill()
#-----------------------------------------------------------------------------------------------------------------------
# Script principal
matricef = lire_matrice(fichier_plan)
liste_objets = []
pas = afficher_plan(matricef, X_max, X_min, Y_max, Y_min)
position_actuelle_matrice = (0,1)#POSITION_DEPART
position_actuelle_turtle = (X_min + (1.5*pas), Y_min + (len(matricef)-0.5)*pas)
point_du_personnage = personnage(pas, position_actuelle_turtle)
dico_objets = creer_dictonnaire_des_objets(fichier_objets)
dico_portes = creer_dictonnaire_des_objets(fichier_questions)
matrice = matricef
turtle.listen()
turtle.onkeypress(deplacer_gauche, "Left")
turtle.onkeypress(deplacer_droite, "Right")
turtle.onkeypress(deplacer_haut, "Up")
turtle.onkeypress(deplacer_bas, "Down")
turtle.mainloop()