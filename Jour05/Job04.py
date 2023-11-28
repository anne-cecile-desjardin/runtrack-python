#Écrire une fonction qui, recevant une taille n en paramètre, affiche un tapis de n+1
#ligne/n+1 colonne traversé par une diagonale.

def afficher_tapis_diagonale(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                print('\\', end='')
            elif i + j == n:
                print('/', end='')
            else:
                print('#', end=' ')
        print()

# How to use the 4 size (example)
afficher_tapis_diagonale(4)
