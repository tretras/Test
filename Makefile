.PHONY: all test check format benchmark  info doc clean readme

SEP="------------------------------------------------------------------------------------------------------------------------------"
define cartouche
	@echo "\n$(SEP)\n\t$(1)\n$(SEP)"
endef

 
#commencer une ligne par @ permet de spécifier un commentaire
info: 
	@echo "Choisir une cible parmi readme, man, format, check, doc, test, benchmark, all"

readme: 
	lowdown -tterm README.md | more

all: format check doc test benchmark

man: 
	$(call cartouche, Analyse Ruff)
	@echo "ruff --help : Afficher l'aide de ruff"
	@echo "ruff check <fichier> : Afficher les erreurs de qualité de code"
	@echo "ruff rule <règle> : Explication d'une règle particulière (e.g. ruff rule E722)"
	@echo "ruff check --diff <fichier> : Suggérer des correctifs"
	@echo "ruff check --fix <fichier> : Appliquer les correctifs"
	@echo "ruff format --diff <fichier> : Suggérer un reformatage"
	@echo "ruff format <fichier> : Appliquer un reformatage"
	$(call cartouche, Analyse Pycodestyle)	
	@echo "pycodestyle --help : Afficher l'aide de pycodestyle"

format:
	$(call cartouche, Formatage Ruff de tous les fichiers)
	ruff format .
	
# commencer une commande par - permet de poursuivre en cas d'erreur 
# || true permet de ne pas afficher de message de make en cas d'erreur (même 'ignored')
# comme celui-ci : make: [makefile:28: check] Error 1 (ignored)  
check:
	$(call cartouche, Analyse Ruff)
	-@ruff check . || true
	$(call cartouche, Analyse Pycodestyle)
	-@pycodestyle . || true

doc: 
	pdoc moyenne.py test_moyenne.py benchmark.py -o docs

test:
	$(call cartouche, Tests)
	pytest

benchmark:
	python benchmark.py

clean: 
	rm -rf docs benchmark.png .ruff_cache .pytest_cache __pycache__



























































































































































egg: 
	@echo  "Vous avez trouvé un easteregg ! Envoyez un message à votre enseignant référent pour le signaler !"
