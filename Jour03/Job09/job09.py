nom_produit = "ananas"
prix_produit = 5
quantite_produit = 50
quantite_utilisateur = int(input("Combien de quantité du produit voulez vous ?"))
quantite_produit = quantite_utilisateur
prix_produit *= 1.10 

# Information sur le produit 
print("Informations sur le produit:")
print("Nom du produit: {}".format(nom_produit))
print("Prix unitaire: {:.2f} euros".format(prix_produit))
print("Quantité en stock: {}".format(quantite_produit))

# Demande la quantité à l'utilisateur  
print("Votre quantité est de : ", quantite_utilisateur)


# Informations du produit mis à jour
print("Informations du produit mis à jour :")
print("Nom du produit: {}".format(nom_produit))
print("Prix unitaire: {:.2f} euros".format(prix_produit))
print("Quantité en stock: {}".format(quantite_produit))