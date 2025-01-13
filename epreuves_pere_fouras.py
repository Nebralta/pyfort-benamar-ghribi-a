import json
import random

def charger_enigmes(fichier):
    """Charge les énigmes depuis un fichier JSON."""
    with open(fichier, 'r') as fichier_enigmes:
        liste_enigmes = json.load(fichier_enigmes)
    return liste_enigmes

def enigme_pere_fouras():
    """Gère une énigme du Père Fouras."""
    liste_enigmes = []
    enigme_choisie = {}
    essais_restants = 3

    # Charger les énigmes depuis le fichier JSON
    liste_enigmes = charger_enigmes("enigmesPF.json")

    # Choisir une énigme aléatoire
    enigme_choisie = random.choice(liste_enigmes)
    print(enigme_choisie["question"])

    # Boucle pour les essais
    while essais_restants > 0:
        reponse_joueur = input("Saisir la réponse : ")
        reponse_joueur_lower = reponse_joueur.lower()

        if reponse_joueur_lower == enigme_choisie["reponse"].lower():
            print("La réponse est correcte, vous avez gagné une clé.")
            return True
        else:
            print("La réponse n'est pas correcte.")
            essais_restants -= 1

        if essais_restants == 0:
            print("Le joueur a échoué à résoudre l'énigme.")
            return False
