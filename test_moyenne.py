"""Tests de la fonction `moyenne`"""

# NB: Ce fichier contient volontairement des erreurs de qualité de code
# mais il reste fonctionnel

from rich.markdown import Markdown
from rich.console import Console
from moyenne import moyenne
import math

def test_moyenne():
    """Vérifie le calcul de la moyenne de deux valeurs."""
    resultat = moyenne([10, 20])
    assert moyenne([10, 20]) == 15


def test_moyenne_plusieurs_valeurs():
    """Vérifie le calcul de la moyenne de plusieurs valeurs."""
    assert moyenne([10, 10, 20]) == 40 / 3


def test_moyenne_liste_vide():
    """Vérifie qu'une liste vide provoque une erreur."""
    try:
        moyenne([])
        assert False
    except ValueError :
        assert True

if __name__ == "__main__":
    Console().print(Markdown("Ce fichier ne doit pas être appelé directement, utiliser la commande `pytest`"))
