# Othello-IA

Intelligence Artificielle qui participe au tournoi PI2CChampionshipRunner et joue à OTHELLO de manière refléchie et sans bad move. 
Lien du serveur qui permet de jouer au tournoi : https://github.com/qlurkin/PI2CChampionshipRunner

## Lancement

Exemple de commande pour lancer l'IA avec le port 1100:

    - python main.py 1100
## Fichiers

 - main.py : Fichier principal de lancement.
 - connexion.py : Permet de 
    - s'inscrire sur le serveur du championnat PI2CChampionshipRunner.
    - lancer le serveur d'écoute
    - dialoguer avec le serveur du championnat
 - jsonStream.py : Permet de 
    - encoder les messages à envoyer
    - décoder les messages reçus.
 - play.py : Permet de retourner le message à envoyer au serveur avec le move à jouer et le message à afficher.
 - strategies.py : Contient les stratégies de calcul du move.
    - random_strategy : retourner un move d'une façon aléatoire.
    - weight_strategy : retourner un move avec le meilleur poids dans la matrice des poids.
    - minimax_strategy : retourner un move calculé avec l'algorithme minimax.
 - utils.py : Contient plusieurs fonctions utiles pour le projet

## Stratégie jouée au championnat
L'IA va jouer au championnat avec : minimax_strategy.
On commence par donner un poids à chaque case dans le plateau :
- Matrice des poids : Weight = 

        [100,    -50,    10,     5,     5,    10,    -50,      100],
        [-50,    -75,     0,     0,     0,     0,    -75,      -50],
        [ 10,     0,     10,     0,     0,    10,      0,       10],
        [  2,     0,      0,     0,     0,     0,      0,        2],
        [  2,     0,      0,     0,     0,     0,      0,        2],
        [ 10,     0,     10,     0,     0,    10,      0,       10],
        [-50,    -75,     0,     0,     0,     0,    -75,      -50],
        [100,    -50,    10,     5,     5,    10,    -50,      100]
   

Grâce à la matrice weight et à l'évaluation du plateau, l'IA :

    - joue en priorité les 4 coins
    - favorise les coups sur les boards
    - évite de prendre les cases adjacentes aux coins sauf quand ces derniers sont pris,ceci est fait grâce à la mise à jour des poids dans la matrice weight.

Afin de répondre dans les temps et éviter des recherches minimax inutiles :

    - Jouer None directement si la liste legal_move est vide.
    - Jouer le seul élement de la liste legal_move si celle-ci n'a qu'un seul élement.
    - jouer un coin si la liste legal_move contient un coin dans les possibilités.

En cas de recherche Minimax en profondeur, privilégier d'abords la recherche pour les cases ayant un grand poids, ainsi au bout de 4.5 secondes, si la recherche n'est pas terminée, on enverrait le meilleur score entre ces cases.

## Librairies utilisées dans le projet
- asyncio
- json
- random
- json
- pytest
- dataclass
- time
- stopit : pour interrompre la recherche minimax après un certain temps (4.7 sec).

## Author
- [@MehdiAtigui](https://github.com/mehdiatigui/othello-IA)
- matricule : 20081



