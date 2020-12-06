b=[ ['V', 'V', 'V', 'J', 'R', 'R', 'J'],
    ['V', 'V', 'V', 'R', 'J', 'R', 'R'],
    ['V', 'V', 'V', 'V', 'R', 'J', 'J'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'J'],
    ['V', 'V', 'V', 'R', 'R', 'R', 'R'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V']]
def gagnant(grille):

    nb_colonne=len(grille)+1
    Puissance=4
    cpt=[[],[]]
    COULEUR=["R","J"]
    for i in range(nb_colonne):
        if i<nb_colonne//2:
            print("droite")
        elif i==nb_colonne//2:
            print("deux coter")
        elif i > nb_colonne // 2:
            print("gauche")
    
    print(nb_colonne)
    
    for i,v in enumerate(grille):
        print(i,v)
        print(len(grille[i]))
        for j in range(len(grille[i])-1):
            if grille[i][j:j+4]==["R","R","R","R"]:
                print("puissance 4")
                print(grille[i][j:j + 4])
                i=(nb_colonne-1)
               

gagnant(b)