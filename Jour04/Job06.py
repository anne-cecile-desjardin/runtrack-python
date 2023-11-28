#Écrire un programme qui échange les valeurs de la première et de la dernière case
#d’une liste quelconque non vide.


def echanger_premiere_et_derniere(liste):
    # Vérification que la liste n'est pas vide (non vide)
    if len(liste) > 0:
        # Échange des valeurs de la première et de la dernière case
        liste[0], liste[-1] = liste[-1], liste[0]

# Exemple
ma_liste = [1, 2, 3, 4, 5]
print("Liste avant l'échange :", ma_liste)

# Appel de la fonction pour échanger les valeurs de la première et de la dernière case
echanger_premiere_et_derniere(ma_liste)

# Affichage de la liste
print("Liste après l'échange :", ma_liste)