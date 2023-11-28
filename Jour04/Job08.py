#Écrire un programme qui calcule la somme de toutes les valeurs paires de la liste
#L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def somme_valeurs_paires(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:  # Le nombre est-il pair?
            somme += nombre
    return somme

resultat = somme_valeurs_paires(L)
print(f"La somme des valeurs paires de la liste est : {resultat}")