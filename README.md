# demo-template

## Objectifs

À l'issue de ce tutoriel, vous devez savoir :

- écrire une fonction Python ;
- utiliser des listes ;
- gérer une erreur avec une exception ;
- obtenir de l'aide sur le projet ;
- vérifier la qualité du code avec `ruff` et l'améliorer ;
- produire la documentation de votre code avec `pdoc` et l'afficher ;
- exécuter des tests avec `pytest` ;
- mettre en place des jeux de tests produisant des courbes ;
- automatiser ces traitements à l'aide de la commande `make`.

---

## Exercice 1 — Calculer une moyenne

On souhaite écrire une fonction permettant de calculer la moyenne des valeurs contenues dans une liste.

- La fonction doit avoir la forme :

```python
def moyenne(valeurs):
    ...
```

- La fonction doit retourner la moyenne des valeurs de la liste qui lui est passée en paramètres.  

- Testez votre fonction en utilisant le *main guard* du fichier moyenne.py, en exécutant directement le fichier python depuis le terminal : 

```bash
python3 moyenne.py
```

---

## Exercice 2 — Obtenir de l'aide sur le projet

Le projet est fourni avec un fichier *Makefile* permettant d'automatiser certaines actions. La règle `man` permet d'afficher une aide présentant quelques commandes utiles et leurs options.

Dans le terminal, utilisez la commande suivante pour afficher cette aide :

```bash
make man
```

---

## Exercice 3 — Vérifier et améliorer le code

On souhaite maintenant vérifier automatiquement la qualité du code. La règle `check` du fichier *Makefile* invoque successivement deux outils pour cela : 

- La commande `ruff`
- La commande `pycodestyle`

Dans le terminal, exécutez :

```bash
make check
```

- Cette commande affiche les problèmes détectés concernant la qualité du code.

- Corrigez les problèmes signalés jusqu'à obtenir des affichages qui vous conviennent. L'objectif est d'obtenir un code respectant les conventions de qualité attendues, ou d'assumer la responsabilité des suggestions que vous choisissez de ne pas traiter.

La commande `ruff` propose diverses options pour vous aider à résoudre les problèmes rencontrés :

- Observer les modifications proposées par Ruff avant de les appliquer :

```bash
ruff check --diff .
```

- Appliquer les modifications automatiquement : 

```bash
ruff check --fix .
```

- Formater le code :

```bash
ruff format .
```

---

## Exercice 4 — Tester la fonction `moyenne`

On souhaite maintenant vérifier automatiquement que `moyenne` fonctionne correctement. Pour cela, nous utilisons la commande `pytest`, qui exploite le fichier *test_moyenne.py*. 

- Les tests peuvent être exécutés avec : 

```bash
pytest
```

- Ou, de manière équivalente, avec la règle `test` du fichier *Makefile* : 

```bash
make test
```

- Un test vérifie notamment qu'une erreur `ValueError` est bien levée lorsque la liste est vide.
Corrigez la fonction `moyenne` si nécessaire afin que tous les tests passent.

---

## Exercice 5 — Mesurer les performances

On souhaite maintenant étudier les performances de la `moyenne` en fonction de la taille de la liste à traiter. Pour cela, nous utilisons le fichier *benchmark.py*, qui réalise plusieurs exécutions de la fonction `moyenne` pour des listes de tailles croissantes, mesure leur temps d'exécution à l'aide du module  `timeit`, affiche les résultats sur le terminal et produit une courbe avec `matplotlib`.


Dans le terminal, exécutez :

```bash
make benchmark
```

Vérifiez qu'un fichier nommé *benchmark.png* a bien été produit et affichez-le. 


## Exercice 6 — Produire la documentation du projet

On souhaite produire une documentation lisible à partir du code du projet. La règle `doc` du fichier *Makefile* utilise `pdoc` pour cela. 

Dans le terminal, exécutez :

```bash
make doc
```

- Un répertoire `docs` est créé, contenant des fichiers HTML de documentation, à l'aide des annotations docstrings présentes dans les fichiers de code python. 

- Vérifiez la présence de ce répertoire dans l'aborescence du projet. 

- Pour afficher le contenu des fichiers HTML générés, il vous faut un navigateur, ce que Codespaces ne fournit pas... 

- Un moyen simple d'afficher ces fichiers est de commiter votre travail et de le pousser sur votre dépôt. Vous pourrez ainsi observer les fichiers depuis le navigateur de votre PC en affichant la version actuelle de votre dépôt. C'est l'objet du dernier exercice. 

## Exercice 7 — Enregistrer la version actuelle de votre projet sur GitHub

On souhaite maintenant enregistrer sur GitHub la version actuelle du projet, afin de pouvoir remettre le travail pour évaluation ou simplement en garder une trace.

Dans le terminal, exécutez successivement les commandes suivantes : 

- Vérifiez l'état du dépôt :

```bash
git status
```

- Ajoutez les modifications :

```bash
git add .
```

- Créez un commit :

```bash
git commit -m "Message de Commit"
```

Envoyez le commit sur GitHub :

```bash
git push
```

- Une manière plus simple (mais magique) de réaliser ces opérations est d'utiliser le menu *Source Control* de Visual Studio, et de réaliser l'opération *Commit & Push*, après avoir sélectionné les nouveaux fichiers à versionner en cliquant sur le `+` situé à droite de chaque fichier.


- Ouvrez ensuite votre dépôt GitHub dans le navigateur de votre PC et vérifiez que tous les fichiers de votre projet dans Codespaces ont bien été ajoutés à votre dépôt distant. 

