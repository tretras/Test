#! /usr/bin/env python3

"""Implémentation des piles à l'aide de listes python """


class Pile:
    
    def __init__(self): self.data = []
    
    def est_vide(self):
        return self.data == []
    
    def sommet(self):
        if self.est_vide():
            return None
        else:
            return self.data[-1]

    def empiler(self, x): 
        self.data.append(x)
    
    def depiler(self):
        if self.est_vide():
            print("Pile vide")
        else:
            return self.data.pop()
    
    def longueur(self): 
        return len(self.data)
    
    def afficher(self):
        for i in range(len(self.data)-1,-1,-1):
            print(self.data[i], end= " ")
        print("")

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

