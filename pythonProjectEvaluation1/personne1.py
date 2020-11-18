"""
Projet réalisé dans le cadre du MOOC : Apprendre à coder avec Python
Date : 11 nov 2020
Affiche le plan d'un château et permet de se déplacer dans le plan jusqu'à que le joueur soit sur la case sortie
Remarque : ce programme correspond au Niveau 1 du MOOC (avec un ajout : le déplacement du joueur)
"""

import turtle
from CONFIGS import *

# Création d'un dictionnaire qui fait le lien entre les valeurs dans la matrice plan et les couleurs
# NOus ajoutons une valeur 5 qui signifie que la case déjà a été vue (COULEUR_VUE)
couleurs = {}
couleurs[0] = COULEUR_COULOIR
couleurs[1] = COULEUR_MUR
couleurs[2] = COULEUR_OBJECTIF
couleurs[3] = COULEUR_PORTE
couleurs[4] = COULEUR_OBJET
couleurs[5] = COULEUR_VUE

def calculer_pas(matrice):
    """
    La matrice du plan permet de retourner la taille d'une case (la case est carrée)
    """
    return int(min((ZONE_PLAN_MAXI[0] - ZONE_PLAN_MINI[0]) / len(matrice[0]),
                      (ZONE_PLAN_MAXI[1] - ZONE_PLAN_MINI[1]) / len(matrice)))

def coordonnees(case, pas):
    """
    Traduit la position d'une case dans le plan en ses coordonnées en pixels Turtle
    """
    return ZONE_PLAN_MINI[0] + case[1] * pas, ZONE_PLAN_MAXI[1] - (case[0] + 1) * pas

def tracer_carre(dimension):
    """
    Affiche un carré de taille 'dimension' depuis la position actuelle de Turtle
    """
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(dimension)
        turtle.left(90)
    turtle.end_fill()

def tracer_case(case, couleur, pas):
    """
    Prépare la couleur de la case et lance l'affichage de la case
    """
    turtle.color(couleur)
    turtle.up()
    turtle.goto(coordonnees(case, pas))
    tracer_carre(pas)

def afficher_plan(matrice):
    """
    Affiche le plan du château fourni dans la matrice en parcourant toutes ses lignes et colonnes
    """
    for y in range(len(plan)):
        for x in range(len(plan[y])):
            tracer_case(tuple([y, x]), couleurs[int(plan[y][x])], calculer_pas(plan))

def tracer_joueur(case, couleur, pas):
    """
    Affiche le joueur à sa position dans le plan (rond plein et centré dans sa case)
    """
    turtle.color(couleur)
    turtle.up()
    x0, y0 = coordonnees(case, pas)[0] + int(pas / 2), coordonnees(case, pas)[1] + int(pas / 4)
    turtle.goto(x0, y0)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(int(pas * RATIO_PERSONNAGE / 2))
    turtle.end_fill()

def lire_matrice(fichier):
    """
    Chargement du plan du château retourné par la matrice map
    """
    map = []
    f = open(fichier, 'r', encoding='utf-8')
    for line in f:
        map.append(line.strip().split(' '))
    f.close()
    return map

def avancer(x, y):
    """
    Incrémente la position du joueur si le déplacement vers x, y est possible. Puis trace
    le joueur à la nouvelle position et colorie l'ancienne position dans la couleur des
    cases déjà visitées.
    """
    global pos_joueur
    global plan
    if not(pos_joueur[0] + y < 0 or pos_joueur[0] + y >= len(plan) or pos_joueur[1] + x < 0 or pos_joueur[1] + x >= len(plan[0])):
        if int(plan[pos_joueur[0] + y][pos_joueur[1] + x]) != 1:
            tracer_case(pos_joueur, COULEUR_VUE, calculer_pas(plan))
            pos_joueur = pos_joueur[0] + y, pos_joueur[1] + x
            tracer_joueur(pos_joueur, COULEUR_PERSONNAGE, calculer_pas(plan))

def haut():
    """
    Effectue un déplacement vers le haut si la flèche haut est pressée
    """
    x, y = 0, -1
    avancer(x, y)

def bas():
    """
    Effectue un déplacement vers le bas si la flèche bas est pressée
    """
    x, y = 0, 1
    avancer(x, y)

def droite():
    """
    Effectue un déplacement vers la droite si la flèche droite est pressée
    """
    x, y = 1, 0
    avancer(x, y)

def gauche():
    """
    Effectue un déplacement vers la gauche si la flèche gauche est pressée
    """
    x, y = -1, 0
    avancer(x, y)

# Chargement du dictionnaire des objets avec position en clé (tuple de int) et description en valeur (str)
# La structure des données proposées des .csv des objets du jeu, qui est rédigée comme du code Python, est exploitée grâce à la commande exec()
f = open(fichier_objets, 'r', encoding='utf-8')
dico_objets = {}
import io
d:str
with open(fichier_questions, "r", encoding="utf-8") as lec:
    d = lec.read()
f = d.strip('\n')

f = f.split("\n")

f_dico = dict()
for v in f:
    d1, d2 = v.split("),")
    d1 = d1[1:]
    d1 = d1.split(",")
    d1 = (int(d1[0]), int(d1[1]))

    d2=d2.strip(" ")
    if len(d2.split("',")) == 2:
        d2 = d2.split("',")
    else:
        d2 = d2.split("\",")

    d2[0] = d2[0].strip(" ('\"")
    d2[1] = d2[1].strip(" \'")
    d2[1] = d2[1].strip(")")
    d2[1] = d2[1].strip(" '")
    f_dico[d1] = (d2[0], d2[1])
dico_objets=f_dico
memoire_qr = ""
"""for line in f:
    exec('position = '+line[:line.index(',',line.index(',') + 1)]) # le format du tuple de la position est récupéré avant la seconde virgule de chaque ligne
    exec('objet = '+line[line.index(',',line.index(',')+1) + 1:].strip()) # la description de l'objet est récupérée après la seconde virgule de chaque ligne, puis exec pour supprimer les " ou '
    dico_objets[position] = objet
"""
memoire_qr = ""
import io
d:str
with open(fichier_objets, "r", encoding="utf-8") as lec:
    d = lec.read()
f = d.strip('\n')

f = f.split("\n")

f_dico = dict()
for v in f:
    d1, d2 = v.split("),")
    d1 = d1[1:]
    d1 = d1.split(",")
    d1 = (int(d1[0]), int(d1[1]))
    d2=d2.strip(" ")
    d2 = d2[1:len(d2)-1]
    f_dico[d1] = d2
dico_objets=f_dico


# Chargement du dictionnaire des portes avec position en clé (tuple de int) et question/réponse (tuple de str) en valeur
# La structure des données des .csv des portes du jeu, qui est rédigée comme du code Python, est exploitée grâce à la commande exec()
f = open(fichier_questions, 'r', encoding='utf-8')
dico_portes = {}
"""for line in f:
    exec('position = '+line[:line.index(',',line.index(',') + 1)]) # le format du tuple de la position est récupéré avant la seconde virgule de chaque ligne
    exec('q_et_r = '+line[line.index(',',line.index(',') + 1) + 1:].strip()) # la question et la réponse est récupérée après la seconde virgule de chaque ligne, puis exec pour supprimer les deux " ou ' englobants
    dico_portes[position] = q_et_r
"""
f.close()

# prépare le jeu en affichant le plab du château et le joueur à sa position de départ
plan = lire_matrice(fichier_plan)
turtle.hideturtle()
turtle.speed(0)
afficher_plan(plan)
pos_joueur = (0,1)
tracer_joueur(pos_joueur, COULEUR_PERSONNAGE, calculer_pas(plan))

# défini les qautre touches attendues pour les déplacements
turtle.onkeypress(haut, 'Up')
turtle.onkeypress(bas, 'Down')
turtle.onkeypress(droite, 'Right')
turtle.onkeypress(gauche, 'Left')
turtle.listen()

# Effectue des déplacements jusqu'à que le joueur soit sur la case objectif = fin du jeu
while int(plan[pos_joueur[0]][pos_joueur[1]]) != 2:
    turtle.update()