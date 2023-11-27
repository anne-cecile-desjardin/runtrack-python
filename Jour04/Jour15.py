#Écrivez un programme qui arrondi les nombres de la liste [22.4, 4.0, 16.22, 9.10, 11.00,
#12.22, 14.20, 5.20, 17.50]

#Puis retourner la liste dans l’ordre croissant.
#SANS UTILISER DE FONCTION SYSTÈME (len, sort, round.....)

liste_nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres dans la liste
for i in range(len(liste_nombres)):
    # Arrondir chaque nombre à la valeur entière
    liste_nombres[i] = int(liste_nombres[i] + 0.5)  # Arrondi classique, ajout de 0.5 avant conversion en entier

# Tri manuel sans utiliser sort()
n = len(liste_nombres)
for i in range(n):
    for j in range(0, n-i-1):
        if liste_nombres[j] > liste_nombres[j+1]:
            # Échange des éléments si ils sont dans le mauvais ordre
            temp = liste_nombres[j]
            liste_nombres[j] = liste_nombres[j+1]
            liste_nombres[j+1] = temp

# Affichage de la liste triée
print("Liste triée dans l'ordre croissant après arrondi :")
print(liste_nombres)
