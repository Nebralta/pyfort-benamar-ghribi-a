import json
import random

def salle_de_tresor():
    # Initialisation des variables
    jeu_indices, details_emission = {}, {}
    annee_selectionnee, mot_de_passe = "", ""
    essais_restants = 0
    reponse_correcte = False

    # Chargement des indices à partir du fichier JSON
    with open("data/indicesSalle.json", "r") as fichier:
        jeu_indices = json.load(fichier)

    # Sélection aléatoire d'une année et d'une émission
    fort_boyard = jeu_indices["Fort Boyard"]
    liste_annees = list(fort_boyard.keys())
    annee_selectionnee = random.choice(liste_annees)
    emissions_par_annee = fort_boyard[annee_selectionnee]
    nom_emission = random.choice(list(emissions_par_annee.keys()))
    details_emission = emissions_par_annee[nom_emission]
    liste_indices = details_emission["Indices"]
    mot_de_passe = details_emission["MOT-CODE"]

    print("Les indices sont :", liste_indices[0], liste_indices[1], liste_indices[2])

    index_indice_suivant = 2
    essais_restants = 3

    while essais_restants > 0:
        reponse_joueur = input("Saisir la réponse : ")
        mot_de_passe_lower = mot_de_passe.lower()
        reponse_joueur_lower = reponse_joueur.lower()
        if mot_de_passe_lower == reponse_joueur_lower:
            reponse_correcte = True
            break
        else:
            essais_restants -= 1
            if essais_restants > 0:
                index_indice_suivant += 1
                print("Il vous reste", essais_restants, "essais")
                print("Le prochain indice est", liste_indices[index_indice_suivant])
            else:
                print("La réponse était :", mot_de_passe)

    if reponse_correcte:
        print("Vous avez gagné !")
    else:
        print("Vous avez perdu !")
