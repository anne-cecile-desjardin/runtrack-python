#Créez une fonction nommée "moyenne" qui prend en paramètre trois notes et retourne
#la moyenne de ces notes.Demandez à l'utilisateur de saisir trois notes, puis enregistrez le résultat de la fonction
#"moyenne" dans une variable appelée "moyenne_etudiant".

#Afficher ensuite la phrase suivante en fonction de la moyenne de l’étudiant :
#➔ Très bon élève si la moyenne est comprise entre 20 et 15.
#➔ Bon élève si la moyenne est comprise entre 14 et 11.
#➔ Élève moyen si la moyenne est comprise entre 10 et 8.
#➔ Élève devant faire des efforts si la moyenne est comprise entre 0 et 7.


def moyenne(num1, num2, num3):
    result = (num1 + num2 + num3) / 3
    if 15 <= result <= 20:
        return ("Très bon élève")
    elif 11 <= result <= 14:
        return ("Bon élève")
    elif 13 <= result <= 8:
        return ("Elève moyen")
    elif 0 <= result <= 7:
        return ("Elève devant faire des efforts")

print(moyenne(0, 0, 0))