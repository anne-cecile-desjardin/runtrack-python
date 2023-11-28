#Écrire un programme qui récupère la valeur, maximum et le minimum des éléments de
#la liste.

#L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def valeurs_extremes(liste):
    if not liste:  # Lla liste est-elle vide?
        return None, None, None

    valeur = liste[0]
    maximum = minimum = liste[0]

    for nombre in liste:
        valeur += nombre
        maximum = max(maximum, nombre)
        minimum = min(minimum, nombre)

    return valeur, maximum, minimum

resultat_valeur, resultat_maximum, resultat_minimum = valeurs_extremes(L)

print(f"La valeur des éléments de la liste est : {resultat_valeur}")
print(f"Le maximum des éléments de la liste est : {resultat_maximum}")
print(f"Le minimum des éléments de la liste est : {resultat_minimum}")

