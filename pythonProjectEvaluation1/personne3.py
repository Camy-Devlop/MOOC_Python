#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:50:46 2020

@author: Grari Mohammed Achraf
project : escape game
"""

import turtle as t #importation du module turtle comme t 
from CONFIGS import *#importation du fichier CONFIGS

"""transforme le fichier plan_chateau en une liste de liste(matrice)  """
def lire_matrice(fichier):
    res=[]
    for ligne in open(fichier):
        ligne=ligne.strip().split(" ")
        res.append(ligne)
    return res



M=lire_matrice(fichier_plan)#affectation a M la matrice qui contient le plan du chateau

"""calcule la dimension a donner aux cases par apport au plan donner"""
def calculer_pas(matrice):
    largeur = abs(ZONE_PLAN_MINI[0])+abs(ZONE_PLAN_MAXI[0])
    hauteur = abs(ZONE_PLAN_MINI[1])+abs(ZONE_PLAN_MAXI[1])
    case_largeur = len(matrice[0])
    case_hauteur = len(matrice)
    return min((largeur/case_largeur),(hauteur/case_hauteur))



pas=calculer_pas(M)#affectation a pas la dimenssion des cases 

"""calcule les coordonnées en pixels turtle du coin inférieur gauche d’une case définie par ses coordonnées"""
def coordonnees(case,pas):
    res=list(ZONE_PLAN_MINI)
    matrice=lire_matrice(fichier_plan)
    for i in range(len(matrice)-1,-1,-1):
        for j in range(len(matrice[0])):
            if(case==(i,j)):
                return tuple(res)
            else:
                res[0]+=pas
        res[0]=ZONE_PLAN_MINI[0]
        res[1]+=pas
                 
    


""" trace un carré avec une dimension donner"""
def tracer_carre(dimension):
    for _ in range(4):
        a.forward(dimension)
        a.left(90)
        
 
    
""" trace un caré dans un emplacement precis avec une couleur donner"""
def tracer_case(case,couleur,pas):
    coordonnee = coordonnees(case,pas)
    a.up()
    a.goto(coordonnee)
    a.down()
    a.color(COULEUR_CASES)
    a.fillcolor(couleur)
    a.begin_fill()
    tracer_carre(pas)
    a.end_fill() 

"""affiche le plan du chateau"""
def afficher_plan(matrice):
    global a # c'est la turtle utiliser pour la fonction tracer_case
    wn = t.Screen()
    wn.title("escape game")#mettre escape game comme titre de la page turtle 
    a=t.Turtle()
    a.hideturtle()
    a.speed(0)
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if(int(matrice[i][j])==0):#si la valeur de la case est 0 on trace un caré blanc(couloir)
                tracer_case((i,j),COULEUR_COULOIR,pas)
            elif(int(matrice[i][j])==1):#si la valeur de la case est 1 on trace un caré gris(mur)
                tracer_case((i,j),COULEUR_MUR,pas)
            elif(int(matrice[i][j])==2):#si la valeur de la case est 2 on trace un caré jaune(objectif) 
                tracer_case((i,j),COULEUR_OBJECTIF,pas)
            elif(int(matrice[i][j])==3):#si la valeur de la case est 3 on trace un caré orange(porte)
                tracer_case((i,j),COULEUR_PORTE,pas)
            else:# sinon la valeur est 4 et on trace un caré vert(objet)
                 tracer_case((i,j),COULEUR_OBJET,pas)


""" permet au mouvement d'etre effectuer ou pas (True permet d'effectuer le mouvement False sinon) """               
def deplacer(matrice, position, mouvement):
    global p# p va contenir la position du personnage elle va etre changer a chaque fois que le personnage bouge
    res0=position[0]+mouvement[0]#va contenir la position du personnage + le mouvement souhaiter en abscisse 
    res1=position[1]+mouvement[1]#va contenir la position du personnage + le mouvement souhaiter en ordonneé
    if(res0 < 0 or res1 < 0 or res0 >= len(matrice) or res1 >= len(matrice[0])):# retourne False si le joueur veut sortir du plan 
        return False 
    elif(int(matrice[res0][res1])==1):#retourne False si le joueur veut aller dans un mur 
        return False 
    elif(int(matrice[res0][res1])==3):#reourne soit True ou False si la reponse a la question est juste voir la fonction poser_question en ligne 210
        res=poser_question(matrice, (res0,res1), mouvement)
        return res 
    elif(int(matrice[res0][res1])==4):#retourne True quand le joueur veut rammaser un object 
        ramasser_objet(matrice,position,mouvement)
        return True
    elif(int(matrice[res0][res1])==2):#retourne True si le joueur veut aller a l'objectif
        tracer_case(p,"wheat",pas)
        p=(res0,res1)
        ganger()
        return True 
    else:# retourne True si le joueur veut aller dans une case vide 
        tracer_case(p,"wheat",pas)
        p=(res0,res1)
        return True 
"""permet de tracer le plan instantanner"""      
t.tracer(0.0)
afficher_plan(M)
t.update()
"""permet de creé le joueur et le mettre dans la possition de depart"""
b = t.Turtle()
b.speed(0)
b.up()
x=list(coordonnees((1,0),pas))
x[0]+=pas/2
x[1]+=pas/2
b.goto(tuple(x))
b.dot(RATIO_PERSONNAGE*pas,COULEUR_PERSONNAGE)
b.hideturtle()
p = (1,0)

"""fonction qui gere le deplacement du joueur si il veut monter"""
def up():
    global M,position
    t.onkeypress(None,'Up')
    if(deplacer(M, p, (-1,0))):
        b.setheading(90)
        b.forward(pas)
        b.dot(RATIO_PERSONNAGE*pas,"red")
    t.onkeypress(up,'Up')
    
"""fonction qui gere le deplacement du joueur si il veut descendre"""
def down():
    global M,position
    t.onkeypress(None,'Down')
    if(deplacer(M,p, (1,0))):
        b.setheading(270)
        b.forward(pas)
        b.dot(RATIO_PERSONNAGE*pas,"red")
    t.onkeypress(down,'Down')

"""fonction qui gere le deplacement du joueur si il veut aller a droite"""
def right():
    global M,position
    t.onkeypress(None,'Right')
    if(deplacer(M,p, (0,1))):
        b.setheading(0)
        b.forward(pas)
        b.dot(RATIO_PERSONNAGE*pas,"red")
    t.onkeypress(right,'Right')
    
    
"""fonction qui gere le deplacement du joueur si il veut aller a gauche"""
def left():
    global M,position
    t.onkeypress(None,'Left')
    if(deplacer(M,p, (0,-1))):
        b.setheading(180)
        b.forward(pas)
        b.dot(RATIO_PERSONNAGE*pas,"red")
    t.onkeypress(left,'Left')


"""renvoie le fichier dico_objets/dico_portes en a dictionnaire  """
def creer_dictionnaire_des_objets(fichier_des_objets):
    d={}
    for text in open(fichier_des_objets):
        a,b=eval(text)
        d[a]=b
    return d


cordone_object=list(POINT_AFFICHAGE_INVENTAIRE)#contien les cordonneé ou on doit afficher l'inventaire
t.up();t.goto(POINT_AFFICHAGE_INVENTAIRE);t.down()#on positionne la tortue au cordonneé POINT_AFFICHAGE_INVENTAIRE
t.write("inventaire:",font=("Arial",15,"normal"))#on ecrit inventaire 
"""permet de ramasser l'objet"""
c=t.Turtle()# on creé une tortue qui s'appelle c 
def ramasser_objet(matrice,position,mouvement):
    global p,cordone_object,c#p=position du personnage ;cordone_object=cordonneé ou ecrire;c=la tortue
    dict_objet=creer_dictionnaire_des_objets(fichier_objets)
    tracer_case(p,COULEUR_VUE,pas)
    position=list(position)
    position[0]+=mouvement[0]#mettre a jour l'ascisse des cordonneé de la position du joueur 
    position[1]+=mouvement[1]#mettre a jour l'ordonneé des cordonneé de la position du  joueur 
    p=tuple(position)#transformer la position de tuple a list pour pouvoir la modifier 
    matrice[p[0]][p[1]]=0#modifier la case qui etait considerer comme objet a une case vide (4-->0)
    cordone_object[1]-=25#soustraire 25 pixel de l'ordonneé pour que les texts ne s'affiche pas un sur l'autre(inventaire des objet)
    tracer_case(p,COULEUR_VUE,pas)#tracer la case ou il y'a l'objet par une case d couleur  COULEUR_VUE
    c.clear()#effacer du text si il y'en a dans la partie des annonce 
    c.up();c.goto(POINT_AFFICHAGE_ANNONCES);c.down()#on positionne la tortue au cordonneé POINT_AFFICHAGE_ANNONCES
    c.write("vous avez trouvé un objet : "+dict_objet[p],font=("Arial",15,"bold"))
    t.up();t.goto(cordone_object);t.down()#on positionne la tortue au cordonneé cordone_object
    t.write(dict_objet[p],font=("Arial",15,"normal"))#afficher l'objet trouver


"""permet de poser une question et permettre au joueur de repondre """
def poser_question(matrice, case, mouvement):
    global p,c
    c.clear()#effacer du text si il y'en a dans la partie des annonce  
    c.up();c.goto(POINT_AFFICHAGE_ANNONCES);c.down()#on positionne la tortue au cordonneé POINT_AFFICHAGE_ANNONCES
    c.write("cette porte est fermée.",font=("Arial",15,"bold"))#afficher cette porte est fermée
    dict_question=creer_dictionnaire_des_objets(fichier_questions)#affecter a dict_question le fichier dico_portes sous forme de dictionnaire 
    reponse=t.textinput("Question",dict_question[case][0])#afficher la question qui se trouve dans la porte 
    t.listen()#recommencer à surveiller le clavier car textinput le desactive 
    if(reponse==dict_question[case][1]):#si la reponse du joueur est correcte 
        p=case#la position du joueur devien celle de la porte 
        c.clear()#effacer du text si il y'en a dans la partie des annonce 
        c.up();c.goto(POINT_AFFICHAGE_ANNONCES);c.down()#on positionne la tortue au cordonneé POINT_AFFICHAGE_ANNONCES
        c.write("la porte s'ouvre !",font=("Arial",15,"bold"))
        matrice[case[0]][case[1]]=0#modifier la case qui etait considerer comme porte a une case vide (3-->0)
        tracer_case(case,COULEUR_VUE,pas)
        case=list(case)
        case[0]-=mouvement[0]
        case[1]-=mouvement[1]
        case=tuple(case)
        tracer_case(case,COULEUR_VUE,pas)#tracé un caré de couleur COULEUR_VUE la ou le personnage se trouver 
        return True 
    else:#si la reponse est fausse 
        c.clear()
        c.up();c.goto(POINT_AFFICHAGE_ANNONCES);c.down()
        c.write("mauvaise reponse",font=("Arial",15,"bold"))
        return False
"""effacer du text si il y'en a dans la partie des annonce et affiche vous aves ganger !"""       
def ganger():
    global c
    c.clear()
    c.up();c.goto(POINT_AFFICHAGE_ANNONCES);c.down()
    c.write("vous aves ganger !",font=("Arial",15,"bold"))
    
    
 
t.listen()#mettre le clavier sous ecoute 
t.onkeypress(up,'Up')#permettre d'appeller la fonction up si le joueur appuis sur la fleche du haut 
t.onkeypress(down,'Down')#permettre d'appeller la fonction down si le joueur appuis sur la fleche du bas
t.onkeypress(left,'Left')#permettre d'appeller la fonction left si le joueur appuis sur la fleche du gauche
t.onkeypress(right,'Right')#permettre d'appeller la fonction right si le joueur appuis sur la fleche de droite
t.mainloop()