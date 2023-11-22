#Créer un programme qui affiche en console les tables de multiplication de 1 à N. N étant un entier supérieur à zéro saisi par l’utilisateur.
#N'oubliez pas de vérifier tout ce qui est nécessaire pour assurer la fiabilité de votre programme.

N = int(input("Entrez un entier supérieur à zéro : "))

if N <= 0:
    print("Veuillez entrer un entier supérieur à zéro.")
else:
    # Afficher les tables de multiplication de 1 à N
    for i in range(1, N + 1):
        print(f"\nTable de multiplication de {i} :")
        for j in range(1, 11):
            produit = i * j
            print(f"{i} x {j} = {produit}")