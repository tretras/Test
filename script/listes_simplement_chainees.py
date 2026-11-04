#! /usr/bin/env python3

"""Listes simplement chaînées

TODO : 
Produire une version récursive de la fonction d’affichage 
Produire des fonctions calculant la taille de la liste en versions itératives et récursives
Tester pour des listes de taille vide, réduite à un élément ou plus longues
[BONUS] Permettre de pouvoir donner un nom à une liste
[BONUS] Ajouter un compteur permettant de savoir le nombre total de cellules produites pour gérer toutes les listes construites
"""

class Cellule:

    @classmethod
    def afficher_nombre_cellules_creees(cls):
        print("Nb de cellules créees : " + str(cls.nombre_cellules_creees))

    def __init__(self, val, suiv=None):
        self.valeur = val   
        self.suivant = suiv

class ListeChainee:
    def __init__(self, n=None):
        self.tete = None

    def est_vide(self):
        return self.tete is None

    def cellule_tete(self):
        return self.tete

    def inserer_tete(self, val):
        nouvelle = Cellule(val, self.tete) 
        self.tete = nouvelle

    def supprimer_tete(self):      
        if self.tete is not None:
            renvoie = self.tete.valeur 
            seconde = self.tete.suivant
            self.tete = seconde
            return renvoie

    def afficher(self):
        courant = self.tete
        while courant is not None:
            print(courant.valeur, end=" -> ")
            courant = courant.suivant
        print("None")

    def afficher_recursif(self):
        def aux_recursif(chainon):
            if chainon is None:
                print("None")
            else:
                print(f"{chainon.valeur} -> ", end="")
                aux_recursif(chainon.suivant)
        aux_recursif(self.tete)

    def longueur(self):
        courant = self.tete
        compteur = 0
        while courant is not None:
            compteur += 1
            courant = courant.suivant
        return compteur


    def longueur_recursif(self):   
        def aux_recursif(chainon):
            if chainon is None:
                return 0
            else:
                return 1 + aux_recursif(chainon.suivant)
        return aux_recursif(self.tete) 


    def inserer_queue(self, val):
        
        if self.tete is None:
            self.tete = Cellule(val, None)
        else:
            courant = self.tete
            while courant.suivant is not None:
                courant = courant.suivant
            courant.suivant = Cellule(val,None)

    def inserer_queue_recursif(self, val):
        def aux_recursif(chainon,val):
            if chainon is None:
                return Cellule(val)
            else:
                chainon.suivant = aux_recursif(chainon.suivant, val)
                return chainon
        self.tete = aux_recursif(self.tete, val)


    def supprimer_queue(self):      
        courant = self.tete
        if self.tete is None:
            print("Liste vide")
        elif courant.suivant is None:
            self.tete = None
        else:
            while courant.suivant.suivant is not None:
                courant = courant.suivant
            courant.suivant = None
    
    def supprimer_queue_recursif(self):
        def aux_recursif(chainon):
            if chainon.suivant is None:
                return None
            else:
                chainon.suivant = aux_recursif(chainon.suivant)
                return chainon
        if self.tete is None:
            print("Liste vide")
        else:
            self.tete = aux_recursif(self.tete)



def tests():
    """"""
    L = ListeChainee()
    L.inserer_tete(10)
    L.inserer_tete(20)
    L.inserer_tete(30)

    L1 = ListeChainee()
    L1.inserer_tete(1)
    
    L2 = ListeChainee()

    L.afficher()
    L1.afficher()
    L2.afficher()

    L.afficher_recursif()
    L1.afficher_recursif()
    L2.afficher_recursif()

    print(L.longueur())
    print(L1.longueur())
    print(L2.longueur())

    print(L.longueur_recursif())
    print(L1.longueur_recursif())
    print(L2.longueur_recursif())

    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()

    L.inserer_tete(1); L.afficher()
    L.inserer_tete(2); L.afficher()
    L.inserer_tete(3); L.afficher()
    
    # BONUS
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()

    L.inserer_queue(1); L.afficher()
    L.inserer_queue(2); L.afficher()
    L.inserer_queue(3); L.afficher()

    L.supprimer_queue_recursif(); L.afficher()
    L.supprimer_queue_recursif(); L.afficher()
    L.supprimer_queue_recursif(); L.afficher()
    L.supprimer_queue_recursif(); L.afficher()

    L.inserer_queue_recursif(1); L.afficher()
    L.inserer_queue_recursif(2); L.afficher()
    L.inserer_queue_recursif(3); L.afficher()


if __name__ == "__main__":
    tests()
