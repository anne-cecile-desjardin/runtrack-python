#Créer un programme qui demande à l’utilisateur trois longueurs a, b, c. À l'aide de ces
#trois longueurs, déterminer s'il est possible de construire un triangle.
#Déterminer ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque.
#Attention : un triangle rectangle peut être isocèle.

def verifier_triangle(a, b, c):
    # Vérifier si les longueurs peuvent former un triangle
    if a + b > c and a + c > b and b + c > a:
        print("Les longueurs peuvent former un triangle.")
        
        # Déterminer le type de triangle
        if a == b == c:
            print("Le triangle est équilatéral.")
        elif a == b or a == c or b == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Le triangle est rectangle et isocèle.")
            else:
                print("Le triangle est isocèle mais non rectangle.")
        else:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Le triangle est rectangle mais non isocèle.")
            else:
                print("Le triangle est quelconque.")
    else:
        print("Les longueurs ne peuvent pas former un triangle.")

# Demander à l'utilisateur les longueurs
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Appeler la fonction pour vérifier le triangle
verifier_triangle(a, b, c)