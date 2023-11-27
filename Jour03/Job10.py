#Créer une fonction qui vérifie que le nombre est pair ou impair.
#Penser à vérifier si le nombre est bien un chiffre entier et positif. Appeler cette fonction
#plusieurs fois avec des valeurs différentes.

def fonction(num):
    if num % 2 == 0:
        print ("nombre pair")
    else:
        print ("nombre impair")
    
fonction(12)
fonction(3)
fonction(10)