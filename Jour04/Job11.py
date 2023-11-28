#Écrire un programme qui créer la liste d’entiers L = [7, 11, 42, 39, 2], votre programme
#devra pouvoir modifier la liste en augmentant de 1 la valeur de chaque élément de la
#liste.


L = [7, 11, 42, 39, 2]

# La liste avant la modification
print("Liste avant la modification :", L)

# Augmenter de 1 la valeur de chaque élément de la liste
L = [nombre + 1 for nombre in L]

# La liste après la modification
print("Liste après la modification :", L)

Liste avant la modification : [7, 11, 42, 39, 2]
Liste après la modification : [8, 12, 43, 40, 3]
