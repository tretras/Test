#! /usr/bin/env python3

"""Implémentation des files à l'aide de listes doublement chainées """

from listes_doublement_chainees import ListeDoublementChainee

class File:

    def __init__(self): 
        self.file = ListeDoublementChainee()

    def est_vide(self): 
        return self.file.est_vide()
    
    def premier(self) : 
        if self.file is not None:
            return self.file.valeur
    
    def enfiler(self, x): 
        self.file.inserer_tete(x)
    
    def defiler(self):
        return self.file.supprimer_queue()
    
    def longueur(self): 
        return self.file.longueur_recursif()
    
    def afficher(self):
        self.file.afficher_recursif()


if __name__ == "__main__":
    p1 = File() 
    p1.enfiler(1)
    p1.enfiler(2)
    p1.enfiler(3)
    p1.afficher()
    
    v = p1.defiler(); print("Extrait : " + str(v))
    v = p1.defiler(); print("Extrait : " + str(v))
    v = p1.defiler(); print("Extrait : " + str(v))
    p1.afficher()
    
