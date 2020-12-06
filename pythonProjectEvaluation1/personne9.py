# Marco La Gioia (000515093) & Ulysse Dehousse (000514144)
"""Jeu d'escape game en rapport avec python. Le but est de s'échapper
 du labyrinthe en récupérant des indices et en résolvant des énigmes.
 Auteurs : Marco La Gioia & Ulysse Dehousse
 Date : 12/11/2020
 Entrées : un fichier plan,
           un fichier contenant les énigmes liés aux portes
           et un fichier contenant les indices
 Résultat : Une fenêtre turtle permettant de se déplacer dans le
            labyrinthe, de récupérer des indices et d'ouvrir des portes"""

import turtle  # importation du module


def creer_dico_portes():  # crée un dictionnaire avec les coordonées de la case comme clés et la question liée comme valeur
    liste_cases = []
    liste_questions = []
    dico_portes = {}
    fichier = open('dico_portes.txt', encoding='utf-8')  # ouvre le fichier dico portes
    for i in fichier:
        a, b = eval(i)  # sépare la ligne en deux parties, la case et la question
        liste_cases.append(a)
        liste_questions.append(b)
    for i in range(len(liste_cases)):
        dico_portes[liste_cases[i]] = liste_questions[i]  # ajoute les couples case-question au dictionnaire
    return dico_portes


def creer_dico_objets():  # crée un dictionnaire avec les coordonées de la case comme clés et l'indice lié comme valeur
    liste_cases = []
    liste_indices = []
    dico_objets = {}
    fichier = open('dico_objets.txt', encoding='utf-8')  # ouvre le fichier dico objets
    for i in fichier:
        a, b = eval(i)  # sépare la ligne en deux parties, la case et l'indice
        liste_cases.append(a)
        liste_indices.append(b)
    for i in range(len(liste_cases)):
        dico_objets[liste_cases[i]] = liste_indices[i]  # ajoute les couples case-indice au dictionnaire
    return dico_objets


def tracer_carre(taille):  # trace un carré, l'argument est la longueur de coté
    for i in range(4):  # répète les instructions 4 fois
        turtle.forward(taille)  # trace un coté
        turtle.left(90)  # fais un angle de 90° vers la gauche


def calculer_pas(
        matrice):  # calcule la taille du coté d'une case sur base d'une matrice. Chaque élément de la matrice"""
    # correspond à une ligne du plan et est une liste
    nbr_lignes = 0  # crée une variable pour le nombre de lignes
    nbr_colonnes = 0  # crée une variable pour le nombre de colonnes
    for i in matrice:  # itère sur chaque élément de la liste 'matrice'
        nbr_lignes += 1  # rajoute 1 au nombre de lignes
    ligne = matrice[0]  # prend la première sous-liste de la liste matrice
    for j in ligne:  # itère sur chaque élément de ligne
        nbr_colonnes += 1  # ajoute 1 au nommbre de colonnes
    longueur = 290 / nbr_colonnes  # calcules la longueur d'une case en fonction du nombre de colonnes
    hauteur = 440 / nbr_lignes  # calcules la hauteur d'une case en fonction du nombre de lignes
    pas = min(longueur, hauteur)  # donnes la plus petite valeur entre la longueur et la hauteur
    return pas  # renvoie la longueur d'un coté de case


def coinIG(nl, nc, pas):  # calcule les coordonnées du coin inférieur gauche d'une case
    x = -240 + nc * pas  # définis l'abcisse du coin en fonction du nombre de colonnes
    y = 200 - (nl + 1) * pas  # définis l'ordonée du coin en fonction du nombre de lignes
    return (x, y)  # renvoie les coordonnées du coin


def tracer_case(nl, nc, couleur, pas):  # trace une case
    coordonnees = coinIG(nl, nc, pas)  # calcules les coordonnées du coin de la case
    turtle.up()
    turtle.goto(coordonnees[0], coordonnees[1])  # déplace turtle au coin inférieur gauche de la case
    turtle.down()
    turtle.begin_fill()  # commence à remplir la figure
    turtle.color(couleur)
    tracer_carre(pas)  # trace un carré en partant du point donné
    turtle.end_fill()  # arretes le remplissage de la figure


def afficher_plan(matrice):
    """affiches le plan sur base de la matrice. Utilise un double for
           pour itérer sur chaque case du plan"""
    pas = calculer_pas(matrice)  # donne la longueur de coté d'une case
    nl = -1  # assigne la valeur -1 à la variable numéro de lignes
    for i in matrice:  # itère sur chaque élément de la liste 'matrice'
        nc = -1  # crée la variable numéro de colonnes et lui assigne la valeur -1
        nl += 1  # ajoute 1 au numéro de ligne
        for j in i:
            nc += 1  # ajoute 1 au numéro de colonne
            couleur = liste_couleurs[j]  # donne la couleur en fonction du numéro donné dans la matrice
            tracer_case(nl, nc, couleur, pas)  # trace la case donnée


def rectangle(x, y, long, haut, couleur):  # dessine un rectangle
    """
    :methods:que fais la fonction
    :param x: c'est quoi la variable etc
    :param y:
    :param long:
    :param haut:
    :param couleur:
    :return: si elle donne un retour ....
    """
    turtle.penup()
    turtle.pencolor(couleur)
    turtle.goto(x, y)  # envoie turtle au premier point
    turtle.pendown()
    for i in range(4):  # itère 4 fois
        if i % 2 == 0:  # définis si le coté est long ou court
            turtle.forward(long)  # dessine le coté
        else:
            turtle.forward(haut)  # dessine le coté
        turtle.right(90)  # fais un angle de 90° vers la droite


def coordonnées_centre_case(nc, nl):  # donne les coordonnées du centre d'une case
    global pas  # permet à la fonction d'utiliser la variable pas
    abcisse = -240 + nc * pas + 0.5 * pas  # détermine la valeur de l'abcisse en fonction du numéro de colonne
    ordonee = 200 - nl * pas - 0.5 * pas  # détermine la valeur de l'ordonée en fonction du numéro de ligne
    return (abcisse, ordonee)  # renvoye les valeurs d'abcisse et d'ordonée


def ecrire_inventaire():  # écris l'inventaire du joueur dans la zone prévue à cet effet
    global inventaire  # permet à la fonction d'utiliser la variable inventaire
    j = 0  # crée une variable j qui servira en cas de décalage
    for i in range(len(inventaire)):  # itère sur tout l'inventaire
        turtle.penup()
        turtle.goto(75, (190 - i * 12 - j * 12))  # envoie turtle dans la zone de l'inventaire
        turtle.pendown()
        if len(inventaire[i]) <= 25:  # vérifie que l'indice ne dépasse pas de la zone d'inventaire
            turtle.write(inventaire[i])  # écris l'indice
        elif len(inventaire[i]) > 25:  # La taille d'écriture est réduite et le texte est séparé en 2 parties
            x = inventaire[i].find(' ', 20)  # trouve un espace dans l'indice
            turtle.write(inventaire[i][:x], move=False, align="left",
                         font=("Arial", 6, "normal"))  # écris la partie précédant l'espace
            turtle.penup()
            turtle.right(90)  # fais un angle de 90 degrés a droite
            turtle.forward(12)  # descends à la ligne suivante dans l'inventaire
            turtle.left(90)  # fais un angle de 90 degrés a gauche
            turtle.pendown()
            turtle.write(inventaire[i][x:], move=False, align="left",
                         font=("Arial", 6, "normal"))  # écris la partie suivant l'espace
            j += 1  # crée un décalage d'une ligne pour les indices suivants


def timer():
    count = 0
    for i in range(2 ** (22)):
        count = count + 1  # crée un délai de quelques secondes


def centre(case):
    return (-240 + pas * (0.5 + case[0]), 200 - pas * (0.5 + case[1]))


# calcule les coordonées turtle du centre de la case désirée

def ouvrir_porte(position_2):
    global matrice
    x = position_2[0]
    y = position_2[1]
    matrice = matrice[0:y] + [matrice[y][0:x] + [0] + matrice[y][x + 1:]] + matrice[y + 1:]
    # remplace une porte par une case vide dans la matrice


def poser_question(position_2):
    global position
    x = position_2[0]
    y = position_2[1]
    reponse = turtle.textinput("Question", dico_portes[(y, x)][0])  # pose une question et saisit la réponse du joueur
    if reponse in ("0000", dico_portes[(y, x)][1]):
        ouvrir_porte(position_2)
        turtle.penup()
        turtle.goto(-230, 210)
        turtle.color("green")
        turtle.pendown()
        turtle.write("réponse correcte, la porte s'ouvre.")
        timer()
        turtle.color("white")
        turtle.begin_fill()
        rectangle(-239, 239, 478, 38, "white")
        turtle.end_fill()
        turtle.color("black")
        turtle.penup()
        turtle.goto(centre(position))
        turtle.pendown()
        return (True)
        '''Si la réponse donnée est juste (ou égale à la clef universelle 0000), la porte est remplacée
        par une case vide, un message est affiché et effacé apres un délai de temps'''
    else:
        turtle.penup()
        turtle.goto(-230, 210)
        turtle.color("red")
        turtle.pendown()
        turtle.write("réponse incorrecte, la porte reste fermée.")
        timer()
        turtle.color("white")
        turtle.begin_fill()
        rectangle(-239, 239, 478, 38, "white")
        turtle.end_fill()
        turtle.color("black")
        turtle.penup()
        turtle.goto(centre(position))
        turtle.pendown()
        '''Si la réponse donnée est fausse,un message est affiché et effacé apres un délai de temps'''


def recuperer_indice(position_2):  # récupère l'indice lorsque le joueur passe dessus
    tracer_case(position_2[1], position_2[0], 'lightgrey', pas)  # trace une case visitée sur la position de l'indice
    indice = dico_objets[
        (position_2[1], position_2[0])]  # crée une variable indice et lui assigne la chaine de caractère indice
    turtle.color('white')  # détermine la couleur du dessin
    turtle.begin_fill()
    rectangle(-239, 239, 478, 38, 'white')  # colorie la zone d'affichage de messages en blanc
    turtle.end_fill()
    turtle.color('black')  # détermine la couleur du dessin
    turtle.penup()
    turtle.goto(-220, 220)  # envoie turtle dans la zone d'affichage de messages
    turtle.pendown()
    if len(indice) > 25:  # La taille d'écriture est réduite
        turtle.write('Vous avez trouvé un indice : ' + indice, move=False, align="left",
                     font=("Arial", 6, "normal"))  # écrit l'indice
    else:
        turtle.write('Vous avez trouvé un indice : ' + indice)
    timer()
    turtle.color("white")
    turtle.begin_fill()
    rectangle(-239, 239, 478, 38, "white")
    turtle.end_fill()
    turtle.color("black")
    inventaire.append(indice)  # rajoute l'indice à l'inventaire
    ecrire_inventaire()  # écris l'inventaire
    turtle.penup()
    turtle.goto(coordonnées_centre_case(position[0], position[1]))  # renvoie turtle sur la position initiale du joueur
    matrice[position_2[1]][position_2[0]] = 0  # transforme la case de l'indice en case vide dans le plan


def victoire():  # termine le jeu lorsque le joueur atteint la sortie
    turtle.clear()  # vide la fenêtre turtle
    turtle.penup()
    turtle.goto(-50, 0)  # envoie turtle aux coordonées données
    turtle.pendown()
    turtle.color('green')  # détermine la couleur du dessin
    turtle.write('Victoire !', font=(20))  # écrit 'victoire'
    turtle.onkeypress(None, "Left")  # désactive les déplacements du joueur
    turtle.onkeypress(None, "Right")
    turtle.onkeypress(None, "Up")
    turtle.onkeypress(None, "Down")


def deplacement(mouvement):
    global pas
    global position
    x = position[0] + mouvement[0]
    y = position[1] + mouvement[1]
    position_2 = [x, y]  # calcul de la position future, cad. la position après le déplacement
    if matrice[y][x] == 0:
        tracer_case(position[1], position[0], "lightgrey", pas)
        turtle.goto(centre(position))
        position = position_2
        turtle.penup()
        turtle.goto(centre(position))
        turtle.pendown()
        turtle.dot(0.9 * pas, "red")
        '''si la prochaine case est vide, une case grise-clair est tracée à la position initiale,
        turtle prend la position future (qui est définie comme nouvelle position initiale)
        et trace un nouveau rond rouge'''
    elif matrice[y][x] == 3:
        if poser_question(position_2):
            deplacement(mouvement)
        turtle.listen()
        '''si la prochaine case est une porte, la question associée est posée.
        si la réponse donnée est juste le joueur se déplace'''
    elif matrice[y][x] == 4:  # vérifie que le joueur se déplace vers un objet
        recuperer_indice(position_2)  # récupère l'indice
        deplacement(mouvement)  # déplace le joueur sur la case
    elif matrice[y][x] == 2:  # vérifie que le joueur a atteint la sortie
        victoire()  # termine le jeu


def deplacer_gauche():
    turtle.onkeypress(None, "Left")
    deplacement([-1, 0])
    turtle.onkeypress(deplacer_gauche, "Left")


def deplacer_droite():
    turtle.onkeypress(None, "Right")
    deplacement([1, 0])
    turtle.onkeypress(deplacer_droite, "Right")


def deplacer_haut():
    turtle.onkeypress(None, "Up")
    deplacement([0, -1])
    turtle.onkeypress(deplacer_haut, "Up")


def deplacer_bas():
    turtle.onkeypress(None, "Down")
    deplacement([0, 1])
    turtle.onkeypress(deplacer_bas, "Down")


matrice = []  # crée la matrice qui servira au dessin du plan
for i in open('plan_chateau.txt'):  # ouvre le fichier et itère sur chaque ligne
    ligne = []  # crée une liste appelée ligne
    for j in range(len(i)):  # itère sur chaque élément de la ligne du fichier
        if i[j].isalnum():  # vérifie que l'élément est un nombre
            chiffre = int(i[j])  # transforme la string contenant le chiffre en un entier
            ligne.append(chiffre)  # ajoute l'élément à la liste 'ligne'
    matrice.append(ligne)  # ajoute la sous-liste 'ligne' à la matrice

turtle.tracer(0, 0)  # affiche instantanément le dessin
turtle.hideturtle()  # cache la puce turtle
liste_couleurs = ['grey', 'black', 'green', 'brown', 'gold', "lightgrey", "red"]
rectangle(-240, 200, 290, 440, "blue")  # trace la zone du plan
rectangle(70, 200, 170, 440, "red")  # trace la zone d'inventaire
rectangle(-240, 240, 480, 40, "green")  # trace la zone d'affichage
afficher_plan(matrice)  # trace le plan
dico_portes = creer_dico_portes()  # crée le dictionnaire des portes(clés) et des questions liées(valeurs)
dico_objets = creer_dico_objets()  # créé le dictionnaire des cases (clés) comportant des indices[valeurs)
inventaire = [' ']  # créé une variable inventaire et lui assigne ule liste qui sera modifiée par la suite
pas = calculer_pas(matrice)  # calcule la taille d'une case
position = [1, 0]
turtle.penup()
turtle.goto(-240 + pas * 1.5, 200 - pas * 0.5)  # envoie le joueur sur la case départ
turtle.pendown()
turtle.dot(0.9 * pas, "red")  # dessine le rond qui représente le joueur
turtle.listen()
turtle.onkeypress(deplacer_gauche, "Left")
turtle.onkeypress(deplacer_droite, "Right")
turtle.onkeypress(deplacer_haut, "Up")
turtle.onkeypress(deplacer_bas, "Down")
turtle.mainloop()  # empêches la fenêtre de se fermer