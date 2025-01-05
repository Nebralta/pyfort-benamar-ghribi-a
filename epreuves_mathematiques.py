import random
def factorielle(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

def  epreuve_math_factorielle():
    k = random.randint(1, 10)
    attemps = int(input("Épreuve de Mathématiques: Calculer la factorielle de " + str(k) +" : "))
    print("Votre réponse:",attemps)
    if attemps == factorielle(k):
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Mauvaise réponse ! La réponse correcte était :", factorielle(k), ".")
        return False

def resoudre_equation_lineaire(a, b):
    x = -b/a
    return x

def epreuve_math_equation():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = resoudre_equation_lineaire(a, b)
    solution = float(input(f"Épreuve de Mathématiques: Résoudre l'équation {a}x + {b} = 0."))
    if solution == x:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Mauvaise réponse ! La réponse correcte était :",x, ".")
        return False

def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def premier_plus_proche(n):
    while not est_premier(n):
        n += 1
    return n

def epreuve_math_premier():

    n = random.randint(10, 20)
    solution = premier_plus_proche(n)

    print(f"Epreuve de Mathématiques: Trouver le nombre premier le plus proche de {n}.")

    reponse = int(input("Votre réponse: "))

    if reponse == solution:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print(f"Incorrect. La bonne réponse était {solution}.")
        return False


def epreuve_roulette_mathematiques():
    nombre = []
    for i in range(5):
        nombre.append(random.randint(1,20))
    operation = random.choice(["addition", "soustraction", "multiplication"])
    if operation == 'multiplication':
        resultat = nombre[0]
        for n in nombre[1:]:
            resultat = resultat * n

    if operation == 'addition':
        resultat = nombre[0]
        for n in nombre[1:]:
            resultat = resultat + n

    if operation == 'soustraction':
        resultat = nombre[0]
        for n in nombre[1:]:
            resultat = resultat - n
    print(f"Nombres sur la roulette : {nombre}")
    print(f"Calculez le résultat en combinant ces nombres avec une {operation}")
    tentative = int(input("Votre réponse: "))
    if tentative == resultat:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print(f"Incorrect. La bonne réponse était {resultat}.")
        return False
def epreuve_math():

    epreuves = [epreuve_math_premier, epreuve_roulette_mathematiques,epreuve_math_equation,epreuve_math_factorielle()]
    epreuve = random.choice(epreuves)
    return epreuve()

