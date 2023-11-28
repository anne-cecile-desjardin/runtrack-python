#Écrire une fonction qui contient une liste nommée “fruits” qui contient les strings
#“pomme”, “cerise”, “orange, Melon”. Cette fonction doit à son appel ajouter à la liste
#“fruits” une String “Mangue” à l’index 2.

def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "melon"]
    
    # Ajout de la chaîne "Mangue" à l'index 2 de la liste fruits
    fruits.insert(2, "Mangue")
    
    return fruits

# On appel la fonction
nouvelle_liste = ajouter_mangue()

print(nouvelle_liste)
