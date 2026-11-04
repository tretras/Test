#! /usr/bin/env python3

"""Implémentation des piles à l'aide de listes simplement chainées """

from listes_simplement_chainees import ListeChainee


class Pile:
    
    def __init__(self):
        self.tete = ListeChainee()

    def est_vide(self): 
        return self.tete.est_vide()
    
    def sommet(self):
        seft.tete.sommet()

    def empiler(self, x): 
        self.tete.inserer_tete(x)
    
    def depiler(self):
        return self.tete.supprimer_tete()
    
    def longueur(self): 
        self.tete.longueur()
    
    def afficher(self):
        self.tete.afficher()

if __name__ == "__main__":
    p1 = Pile()
    p1.empiler(1)
    p1.empiler(2)
    p1.empiler(3)
    p1. afficher()
    
    v = p1.depiler(); print("Extrait : " + str(v))
    v = p1.depiler(); print("Extrait : " + str(v))
    v = p1.depiler(); print("Extrait : " + str(v))
    p1. afficher()

