

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

print(moyenne(12, 8, 18))