#Écrire un programme qui crée une liste nommée “L” d’au moins 5 entiers puis
#successivement :
#Afficher la deuxième valeur de la liste
#Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] &
#L[4], puis afficher à nouveau le tableau.
#Puis afficher la dernière valeur de la liste.

def main():
    # Liste d'au moins 5 entiers
    L = [1, 2, 3, 4, 5]

    # Deuxième valeur de la liste
    print("Deuxième valeur de la liste :", L[1])

    # Appel de la fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
    remplacer_par_somme(L, 3)

    # Tableau 
    print("Tableau après la modification :", L)

    # Affichage de la dernière valeur de la liste
    print("Dernière valeur de la liste :", L[-1])

def remplacer_par_somme(liste, index):

    # Vérification que l'index est valide
    if 0 <= index < len(liste):
        # Remplacement de L[3] par la somme des cases voisines L[2] & L[4]
        liste[index] = liste[index - 1] + liste[index + 1]
        
main()