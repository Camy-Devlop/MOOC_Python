
"""
Ingrédients (pour 4 personnes)

3 oeufs
100 g chocolat (noir ou au lait)
1 sachet de sucre vanillé
Préparation de la recette

Séparer les blancs des jaunes d’oeufs
Faire ramollir le chocolat dans une casserole au bain-marie
Hors du feu, incorporer les jaunes et le sucre
Battre les blancs en neige ferme et les ajouter délicatement au mélange à l’aide d’une spatule
Verser dans une terrine ou des verrines et mettre au frais 1 heure ou 2 minimum
"""
class Mousse_chocolat:

    def __init__(self,personne=4):
        self.personne=personne
        self.oeufs=((3/4)*personne)
        self.chocolat=(100/4)*personne
        self.vanille=(1/4)*personne

    def calcule_par_Personne(self,personne=4)->(object,object,object):
        if self.personne==4:
            return (self.oeufs/self.personne)*personne,(self.chocolat / self.personne) * personne,(self.vanille / self.personne) * personne
        else:
            return self.oeufs,self.chocolat,self.vanille


    def affiche_ingrediant(self,personne=4):
        pass