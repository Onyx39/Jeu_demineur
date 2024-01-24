"""
Fichier en charge de l'initialisation du plateau
"""

import random as rd
import sys

def lancer_le_jeu () :
    """
    Fonction qui démarre le jeu

    Auncune entrée

    Sorties :
        plateau (list<list>) : le représentation du plateau
        mines (list) : l'emplacement des mines
    """

    print("\n\nBienvenue dans le jeu du démineur\n" \
        + "Ce programme a été implémenté par Valentin Richard\n" \
        + "Entrer 'exit' à n'importe quel moment pour fermer le programme\n" \
        + "Bon jeu !")
    entree = input("\nDéfinissez la taille de plateau \n" \
               + "(Un entier non nul inférieur ou égal à 20 est demandé)\n")
    if test_entrer_utilisateur(entree) == int(entree) :
        plateau = []
        for _ in range (int(entree)) :
            ligne = []
            for _ in range (int(entree)) :
                ligne.append(["x"])
            plateau.append(ligne)

        mines = creer_liste_mines (plateau)
        return plateau, mines

    return None

def test_entrer_utilisateur (entree) :
    """
    Fonction qui vérifie l'entrée de l'utilisateur pour l'initialisation

    Entrée :
        entree (str) : la saisie de l'utilisateur

    Sortie :
        int(entree) (int) : l'entier de la saisie si valide
    """

    if entree == 'exit' :
        fin_de_partie()
    try :
        entree = int(entree)
    except ValueError:
        print("\nVous n'avez pas entré un entier\n" \
              + "Veuillez recommencer\n")
        print("*"*40)
        lancer_le_jeu()
    if entree <= 0 or entree > 20 :
        print("\nL'entier ne rentre pas dans le domaine demandé\n" \
              + "Veuillez recommencer\n")
        print("*"*40)
        lancer_le_jeu()
    return int(entree)


def creer_liste_mines (plateau) :
    """
    Fonction qui place des mines de manière aléatoire

    Entrée :
        plateau (list<list>) : la représentation du plateau

    Sorties :
        liste_mines (list) : la liste des mines
    """

    longeur = len(plateau)
    nb_mines = round(0.15625*longeur*longeur)

    liste_mines = []
    for _ in range (nb_mines) :
        abscisse = rd.randint(0, longeur - 1)
        ordonnee = rd.randint(0, longeur - 1)
        if [abscisse, ordonnee] not in liste_mines :
            liste_mines.append([abscisse, ordonnee])
        elif [ordonnee, abscisse] not in liste_mines :
            liste_mines.append([ordonnee, abscisse])
        else :
            abscisse = rd.randint(0, longeur - 1)
            if [abscisse, ordonnee] not in liste_mines :
                liste_mines.append([abscisse, ordonnee])

    if len(liste_mines) == nb_mines :
        return liste_mines

    return creer_liste_mines(plateau)

def fin_de_partie () :
    """"
    Fonction qui termine le jeu

    Aucune entrée

    Aucune sortie
    """

    print("\nMerci d'avoir joué\n" \
          + "Ce jeu vous a été proposé par Valentin Richard\n" \
          + "N'hésitez pas à faire des retours ou à rejouer\n\n" \
          + "A la prochaine fois :)\n")
    sys.exit()
