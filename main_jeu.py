from epreuves_pere_fouras import *
from epreuves_logiques import *
from epreuve_finaleV2 import *
from epreuves_hasard import *
from epreuves_mathematiques import *
from fonctions import *

def jeu():
    """Lance le jeu principal."""
    introduction()
    equipe = composer_equipe()
    nombre_cles = 0

    # Boucle principale : obtenir 3 clés
    while nombre_cles < 3:
        choix_epreuve = menu_epreuves()
        joueur_participant = choisir_joueur(equipe)

        resultat_epreuve = False

        # Lancer l'épreuve choisie
        if choix_epreuve == 1:
            resultat_epreuve = epreuve_math()
        elif choix_epreuve == 2:
            resultat_epreuve = lancer_jeu_bataille_navale()
        elif choix_epreuve == 3:
            resultat_epreuve = epreuve_hasard()
        elif choix_epreuve == 4:
            resultat_epreuve = enigme_pere_fouras()
        else:
            print("Choix invalide. Veuillez sélectionner une épreuve valide.")
            continue

        # Gérer les résultats de l'épreuve
        if resultat_epreuve:
            joueur_participant['cles_gagnees'] += 1
            nombre_cles += 1
            print(f"{joueur_participant['nom']} a remporté une clé !")
        else:
            print(f"{joueur_participant['nom']} a échoué à l'épreuve.")

    # Début de l'épreuve finale
    print("\nL'épreuve de la Salle au trésor commence !")
    resultat_final = salle_de_tresor()

    if resultat_final:
        print("L'équipe a remporté le trésor ! Félicitations !")
    else:
        print("L'équipe a perdu. Mieux vaut essayer encore une fois !")

# Lancer le jeu
jeu()
