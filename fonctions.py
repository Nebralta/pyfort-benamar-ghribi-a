def introduction():
    """Affiche un message d'introduction au jeu."""
    print("Bienvenue")
    print("Accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor.")
    print("L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")

def composer_equipe():
    """Permet de composer une équipe de joueurs (maximum 3)."""
    nombre_joueurs = 4
    liste_joueurs = []

    # Limiter le nombre de joueurs à 3 maximum
    while nombre_joueurs > 3:
        nombre_joueurs = int(input("Combien voulez-vous inscrire de joueurs (max 3) : "))
        if nombre_joueurs > 3 or nombre_joueurs <= 0:
            print("Erreur")

    # Création des joueurs avec leurs caractéristiques
    for i in range(nombre_joueurs):
        nouveau_joueur = {
            'nom': input("Nom du joueur : "),
            'profession': input('Sa profession : '),
            'leader': input('Leader ? (o/n) : '),
            'cles_gagnees': 0
        }
        liste_joueurs.append(nouveau_joueur)

    # Vérification et assignation du leader
    nombre_leaders = sum(1 for joueur in liste_joueurs if joueur['leader'] == 'o')

    if nombre_leaders == 0:
        liste_joueurs[0]['leader'] = 'o'  # Premier joueur devient leader par défaut
    elif nombre_leaders > 1:
        for joueur in liste_joueurs:
            joueur['leader'] = 'n'
        liste_joueurs[0]['leader'] = 'o'  # Réassigner le premier joueur comme leader

    return liste_joueurs

def menu_epreuves():
    """Affiche le menu des épreuves et retourne le choix de l'utilisateur."""
    print("\n1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du Hasard")
    print("4. Énigme du Père Fouras")
    choix_epreuve = int(input("Choix : "))
    return choix_epreuve

def choisir_joueur(equipe):
    """Permet de choisir un joueur parmi l'équipe."""
    print('\n')
    for index, joueur in enumerate(equipe):
        role = 'Leader' if joueur['leader'] == 'o' else 'Membre'
        print("{}. {} ({}) - {}".format(index + 1, joueur['nom'], joueur['profession'], role))
    choix_joueur = int(input("Choix : "))
    return equipe[choix_joueur - 1]
