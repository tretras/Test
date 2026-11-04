"""Mesure les performances de la fonction `moyenne`"""

# NB: Ce fichier ne doit pas être modifié

from pathlib import Path
from timeit import timeit

import matplotlib.pyplot as plt

from moyenne import moyenne


def calcul(valeurs):
    """Calcule la moyenne d'une liste de valeurs \
    à l'aide de la fonction `moyenne`."""
    return moyenne(valeurs)


def benchmark():
    """Mesure les performances de la fonction `moyenne`."""
    n_values = [100, 10**3, 10**4, 10**5]
    temps = []

    for n in n_values:
        valeurs = list(range(n))

        temps_total = timeit(
            "calcul(valeurs)",
            globals={"calcul": calcul, "valeurs": valeurs},
            number=100,
        )

        temps.append(temps_total / 100)
        print(f"n = {n:>7} | temps = {temps[-1]:.8f} s")

    plt.plot(n_values, temps, marker="o")
    plt.xlabel("Taille n")
    plt.ylabel("Temps moyen (s)")
    plt.title("Temps d'exécution de moyenne")
    plt.grid()

    fichier = Path(__file__).with_name("benchmark.png")
    plt.savefig(fichier)
    print(f"Graphique enregistré dans : {fichier}")


if __name__ == "__main__":
    benchmark()
