"""
Projet : château du Python des Neiges
Auteur: Raphaël COQUEREL
Date : 13 Novembre 2020
Niveau 1 : Construction et affichage du plan du château -> fonctionnel
Niveau 2 : Gestion des déplacements -> débuté mais non fonctionnel
"""

import turtle

#Déclaration de la variable globale définisant la position du joueur
position = []
matrice = []

def lire_matrice (fichier) :
    res = []
    with open(fichier, encoding="utf-8") as dat:
        m = dat.read()
        m = m.split("\n")
        for i in m :
            i = i.split(" ")
            res.append(i)

    return res



def calculer_pas (matrice) :
    hauteur = len(matrice)
    largeur = len(matrice[0])

    aff_large = 290
    aff_haut = 440

    div_large = aff_large // largeur
    div_haut = aff_haut // hauteur

    if div_haut > div_large :
        return  div_large
    else :
        return div_haut


def coordonnees (case, pas) :
    # case est composé de la valeur de la ligne et de la colone
    # position départ -240/200

    ligne = 200 - (case[0] * pas)
    colone = -(240 - (case[1] * pas))
    return(colone, ligne)


def tracer_carre(dimension) :
    turtle.down()
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(dimension)
    turtle.right(90)
    turtle.forward(dimension)
    turtle.right(90)
    turtle.forward(dimension)
    turtle.right(90)
    turtle.forward(dimension)
    turtle.end_fill()


def tracer_case (case, couleur, pas) :
    turtle.color(couleur)
    turtle.fillcolor(couleur)
    turtle.penup()
    turtle.goto(coordonnees(case, pas))
    tracer_carre(pas)


def afficher_plan (matrice) :
    i = 0
    dictcol = {0 : "white", 1 : "grey", 2 : "yellow", 3 : "orange", 4 : "green"}
    pas = calculer_pas(matrice)

    while i < len(matrice) :
        j = 0

        while j < len(matrice[i]) :
            temp = int(matrice[i][j])
            case = [i, j]
            col = dictcol[temp]
            tracer_case(case, col, pas)

            j += 1

        i += 1


def afficher_plateau () :
    #Zone de dialogue : largeur = -240/300    hauteur : 210/270
    turtle.color("black")
    turtle.penup()
    turtle.goto(-240, 270)
    turtle.down()
    turtle.forward(540)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(540)
    turtle.right(90)
    turtle.forward(60)
    turtle.penup()
    turtle.goto(-220, 250)
    turtle.write("Dialogue :", font=("Arial", 12, "bold"))


    #Zone d'inventaire : largeur = 60/300      hauteur : 200/-240
    turtle.color("black")
    turtle.penup()
    turtle.goto(60, 200)
    turtle.down()
    turtle.right(90)
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(440)
    turtle.right(90)
    turtle.forward(240)
    turtle.right(90)
    turtle.forward(440)
    turtle.penup()
    turtle.goto(80, 180)
    turtle.write("Inventaire :", font=("Arial", 12, "bold"))



def position_base (matrice) :
    i = 0
    global position

    while i < len(matrice[0]) :
        if matrice[0][i] == 0 :
            coor = coordonnees([0, i], calculer_pas(matrice))
            position = coor
            turtle.penup()
            turtle.goto(coor)
            turtle.pendown()
            turtle.dot(5, "red")
            return(0, i)


def deplacer_gauche ():
    turtle.onkeypress(None, "Left")
    global position
    global matrice

    if matrice[position[1]][position[0]-1] == 0 :
        tracer_case(position, "light grey", calculer_pas(matrice))
        position = [position[0]-1, position[1]]
        turtle.penup()
        turtle.goto(position)
        turtle.pendown()
        turtle.dot(5, "red")

    turtle.onkeypress(deplacer_gauche, "Left")


def deplacer_droite ():
    turtle.onkeypress(None, "Right")
    global position
    global matrice

    if matrice[position[1]][position[0]+1] == 0 :
        tracer_case(position, "light grey", calculer_pas(matrice))
        position = [position[0]+1, position[1]]
        turtle.penup()
        turtle.goto(position)
        turtle.pendown()
        turtle.dot(5, "red")

    turtle.onkeypress(deplacer_droite, "Right")


def deplacer_haut ():
    turtle.onkeypress(None, "Up")
    global position
    global matrice

    if matrice[position[1]-1][position[0]] == 0 :
        tracer_case(position, "light grey", calculer_pas(matrice))
        position = [position[0], position[1]-1]
        turtle.penup()
        turtle.goto(position)
        turtle.pendown()
        turtle.dot(5, "red")

    turtle.onkeypress(deplacer_haut, "Up")


def deplacer_bas ():
    turtle.onkeypress(None, "Down")
    global position
    global matrice

    if matrice[position[1]][position[0]+1] == 0 :
        tracer_case(position, "light grey", calculer_pas(matrice))
        position = [position[0]+1, position[1]]
        turtle.penup()
        turtle.goto(position)
        turtle.pendown()
        turtle.dot(5, "red")

    turtle.onkeypress(deplacer_bas, "Down")








mat = (lire_matrice("plan_chateau2.txt"))
matrice = mat

turtle.speed(0)
afficher_plateau()
afficher_plan(mat)
pos = position_base(matrice)

while True :
    turtle.listen()
    turtle.onkeypress(deplacer_gauche, "Left")
    turtle.onkeypress(deplacer_droite, "Right")
    turtle.onkeypress(deplacer_haut, "Up")
    turtle.onkeypress(deplacer_bas, "Down")