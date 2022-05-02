
# Othello-IA

Intelligence Artificielle qui joue de manière refléchie et sans bad move
 au jeu de société "Othello".

## Dossiers
### main
dossier principale qui donne les infos de l'utilisateur.
### connexion
permet de s'inscrire et de dialoguer avec le serveur de M.Lurkin. 
### jsonStream
permet de lire et d'écrire les fichiers json.
### play
permet de jouer un coup choisi qui n'est pas un bad move.
## Stratégie

- Prendre en priorité les 4 coins
- favoriser les coups sur les bords
    - priorité aux "3ème" coins
    - éviter de prendre les "2ème" coins sauf si le coin est pris
- Contrôler le centre du plateau
- Au début du jeu, posséder moins de pions que l'adversaire pour avoir l'avantage.
- éviter de donner les 4 coins
    - ne pas mettre de pions sur les "2ème" coins
    - ne pas mettre de pions sur les (1, 1)
    
![othello](https://tronche.com/cours/assignment/position-initiale.gif)

## Lessons Learned

Lors de ce projet, j'ai appris à faire du code propre d'une part.
C'est à dire, à mettre des commentaires pour chaque fonction,
à faire régulièrement des tests tout au long du projet, à 
utiliser des noms de variables et des noms de fonctions cohérents.

Et d'autre part, comment l'Intelligence Artificielle fonctionne.
La manière de l'utiliser et aussi de la rendre plus performante.



## Documentation

[asyncio](https://docs.python.org/3/library/asyncio-stream.html)
[Itération](https://realpython.com/introduction-to-python-generators/)



## Modules importer

```python
from dataclasses import dataclass
import asyncio
import json
import unittest
import sys

```
## Authors

- [@MehdiAtigui](https://github.com/mehdiatigui/othello-IA)
--> matricule : 20081



