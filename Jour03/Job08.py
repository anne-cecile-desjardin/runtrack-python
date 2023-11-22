


def fonction(type, saison):
    if type == "fruits" and saison == "hiver":
        print ("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "été":
        print ("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print ("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print ("artichaud, aubergine, navet")
    else:
        print ("Il y'a une erreur")


fonction ("fruits", "hiver")