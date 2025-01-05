import random



def jeu_lance_des():
    essais_max = 3



    for essai in range(1, essais_max + 1):



        input("Appuyer sur Entrée pour lancer les dés :")

        print(f"Essai {essai}/{essais_max}")




        des_joueur = (random.randint(1, 6), random.randint(1, 6))
        print(f"Résultats du joueur : {des_joueur}")
        if 6 in des_joueur:
            print( "Félicitations ! Vous avez obtenu un 6 et gagné la partie.")
            return True


        des_maitre = (random.randint(1, 6), random.randint(1, 6))
        print(f"Résultats du maître du jeu : {des_maitre}")
        if 6 in des_maitre:
            print("Le maître du jeu a obtenu un 6. Vous avez perdu la partie.")
            return False

        print("Aucun 6 obtenu. On passe au prochain essai.", 50, 50)

    print("Aucun joueur n'a obtenu un 6 après trois essais. Match nul.")
    return False
def bonneteau():
    bonneteaux = ['A', 'B', 'C']
    essais_max = 2

    print("Bienvenue dans le jeu du bonneteau !")
    print("Trouvez sous quel bonneteau (A, B ou C) se cache la clé. Vous avez deux essais.")

    for essai in range(1, essais_max + 1):
        print(f"Essai {essai}/{essais_max}")
        bonneteau_cle = random.choice(bonneteaux)
        choix_joueur = input("Choisissez un bonneteau (A, B ou C) : ").upper()
        if choix_joueur not in bonneteaux:
            print("Choix invalide. Veuillez choisir entre A, B et C.")
            continue
        if choix_joueur == bonneteau_cle:
            print(f"Bravo ! Vous avez trouvé la clé sous le bonneteau {bonneteau_cle}.")
            return True
        else:
            print(f"Dommage, la clé n'était pas sous {choix_joueur}.")

    print(f"Vous avez perdu. La clé était sous le bonneteau {bonneteau_cle}.")
    return False

def epreuve_hasard():

    epreuves = [jeu_lance_des,bonneteau]
    epreuve = random.choice(epreuves)
    return epreuve()




