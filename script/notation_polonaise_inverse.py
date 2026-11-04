#! /usr/bin/env python3

"""Évaluation d’une expression NPI fournie dans une liste python ou comme une file d'opérateurs"""

from piles_listes_python import Pile
from files_listes_python import File
#from piles_listes_simplement_chainees import Pile
#from files_listes_doublement_chainees import File

def eval_NPI_file(fileExpression):
    # Cette fonction renvoie un tuple(BoolExpressionValide, ValeurOuNone)
    # à partir d'une file d'opérateurs et d'opérandes
    # renvoyer (False,None) signifie que l'expression n'est pas valide 
    # renvoyer (True,None) signifie que l'expression est valide, 
    # mais qu'elle ne correspond pas à un résultat calculable car elle est incomplète
    # renvoyer (True, Entier) signifie que l'expression est valide, 
    # et que son évaluation donne Entier comme résultat
    p = Pile()
    while not fileExpression.est_vide():
        e = fileExpression.defiler()
        if e == "+":
            try:
                e1 = p.depiler()
                e2= p.depiler()
                p.empiler(e2+e1)
            except:
                return (False, None)
        elif e == "-":
            try:
                e1 = p.depiler()
                e2= p.depiler()
                p.empiler(e2+e1)
            except:
                return (False, None)
        elif e == "*":
            try:
                e1 = p.depiler()
                e2= p.depiler()
                p.empiler(e2*e1)
            except:
                return (False, None)
        elif e == "/":
            try:
                e1 = p.depiler()
                e2= p.depiler()
                if e1 != 0 and e2%e1 == 0:
                    p.empiler(e2+e1)
                else:
                    raise "Error"
            except:
                return (False, None)
        elif type(e) is int:
            p.empiler(e)
        else:
            return (False, None)
    if p.longueur() == 1:
        return (True, p.depiler())
    else:
        return (True, None)
   

def eval_NPI_liste(listeExpression):
    # Cette fonction renvoie un tuple(BoolExpressionValide, ValeurOuNone)
    # à partir d'une liste d'opérateurs et d'opérandes
    # renvoyer (False,None) signifie que l'expression n'est pas valide 
    # renvoyer (True,None) signifie que l'expression est valide, 
    # mais qu'elle ne correspond pas à un résultat calculable car elle est incomplète
    # renvoyer (True, Entier) signifie que l'expression est valide, 
    # et que son évaluation donne Entier comme résultat
    p = Pile()
    for e in listeExpression:
        if e == "+":
            try:
                e1 = p.depiler()
                e2= p.depiler()
                p.empiler(e2+e1)
            except:
                return (False, None)
        elif e == "-":
            try:
                e1 = p.depiler()
                e2= p.depiler()
                p.empiler(e2+e1)
            except:
                return (False, None)
        elif e == "*":
            try:
                e1 = p.depiler()
                e2= p.depiler()
                p.empiler(e2*e1)
            except:
                return (False, None)
        elif e == "/":
            try:
                e1 = p.depiler()
                e2= p.depiler()
                if e1 != 0 and e2%e1 == 0:
                    p.empiler(e2+e1)
                else:
                    raise "Error"
            except:
                return (False, None)
        elif type(e) is int:
            p.empiler(e)
        else:
            return (False, None)
    if p.longueur() == 1:
        return (True, p.depiler())
    else:
        return (True, None)



if __name__ == "__main__":
    e1 = File() 
    e1.enfiler(1);
    e1.enfiler(3);
    e1.enfiler('+');
    print(eval_NPI_file(e1));

    e2 = [1,2,'+',4,'*',5,'+']
    print(eval_NPI_liste(e2))