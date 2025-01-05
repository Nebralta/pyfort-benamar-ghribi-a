import random
import time

def prochain_joueur(joueur_actuel):
    return 1 if joueur_actuel == 0 else 0

def creer_grille_vide():
    return [[" " for _ in range(3)] for _ in range(3)]

def afficher_grille(grille, message):
    print(message)
    for ligne in grille:
        print("| " + " | ".join(ligne) + " |")
    print("-" * 15)

def demander_position():
    while True:
        position = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) : ")
        if "," in position:
            ligne, colonne = position.split(',')
            ligne, colonne = int(ligne), int(colonne)
            if 1 <= ligne <= 3 and 1 <= colonne <= 3:
                return ligne - 1, colonne - 1
        print("Position invalide !")

def initialiser_grille():
    grille_joueur = creer_grille_vide()

    position_bateau_1 = demander_position()
    grille_joueur[position_bateau_1[0]][position_bateau_1[1]] = 'B'

    while True:
        position_bateau_2 = demander_position()
        if position_bateau_2 != position_bateau_1:
            grille_joueur[position_bateau_2[0]][position_bateau_2[1]] = 'B'
            break

    afficher_grille(grille_joueur, "Découvrez votre grille de jeu avec vos bateaux :")

def effectuer_tour(joueur_actuel, grille_tirs_joueur, grille_adversaire):
    if joueur_actuel == 0:
        ligne_tir, colonne_tir = demander_position()
        if grille_adversaire[ligne_tir][colonne_tir] == 'B':
            grille_tirs_joueur[ligne_tir][colonne_tir] = 'x'
        elif grille_adversaire[ligne_tir][colonne_tir] == ' ':
            grille_tirs_joueur[ligne_tir][colonne_tir] = '.'
    elif joueur_actuel == 1:
        ligne_tir, colonne_tir = random.randint(0, 2), random.randint(0, 2)
        if grille_adversaire[ligne_tir][colonne_tir] == 'B':
            grille_tirs_joueur[ligne_tir][colonne_tir] = 'x'
        elif grille_adversaire[ligne_tir][colonne_tir] == ' ':
            grille_tirs_joueur[ligne_tir][colonne_tir] = '.'

def verifier_victoire(grille_tirs_joueur):
    nombre_touches = sum(ligne.count('x') for ligne in grille_tirs_joueur)
    return nombre_touches >= 2

def lancer_jeu_bataille_navale():
    grille_joueur = creer_grille_vide()
    grille_maitre_du_jeu = creer_grille_vide()
    grille_tirs_joueur = creer_grille_vide()
    grille_tirs_maitre_du_jeu = creer_grille_vide()

    while True:
        position_bateau_1 = (random.randint(0, 2), random.randint(0, 2))
        position_bateau_2 = (random.randint(0, 2), random.randint(0, 2))
        if position_bateau_1 != position_bateau_2:
            break
    grille_maitre_du_jeu[position_bateau_1[0]][position_bateau_1[1]] = 'B'
    grille_maitre_du_jeu[position_bateau_2[0]][position_bateau_2[1]] = 'B'

    joueur_actuel = 0
    while True:
        if joueur_actuel == 0:
            effectuer_tour(joueur_actuel, grille_tirs_joueur, grille_maitre_du_jeu)
        elif joueur_actuel == 1:
            effectuer_tour(joueur_actuel, grille_tirs_maitre_du_jeu, grille_joueur)
        time.sleep(1)
        if verifier_victoire(grille_tirs_joueur):
            return True
        joueur_actuel = prochain_joueur(joueur_actuel)
