#Créer une fonction qui prend en paramètre un string et qui la retourne inverser. Par
#exemple, « nikana » deviendra « anakin ».reversed

def inverser_chaine(chaine):
    return chaine[::-1]

# Ce code, [::-1] est une notation qui signifie "de la fin à la première avec un pas de -1", ce qui inverse la chaîne de caractères.
chaine_originale = "nikana"
chaine_inverse = inverser_chaine(chaine_originale)

print(f"Chaine originale: {chaine_originale}")
print(f"Chaine inversée: {chaine_inverse}")