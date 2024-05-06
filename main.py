from soustraction import soustraction

def calculatrice(choix, a, b):
    if choix == "addition":
        return addition(a, b)
    elif choix == "soustraction":
        return soustraction(a, b)
    else:
        return "Opération non valide"
