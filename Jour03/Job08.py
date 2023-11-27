#Créer une fonction qui prend 2 paramètres :
#- Le premier reçoit un String nommé “type”
#- Le second reçoit un String nommé “saison”
#Si la valeur de “type” est égale à “fruits” et que celle de saison est égale à “hiver”,
#affichez “orange, mandarine et kiwi”
#Si la valeur de “type” est égale à “fruits” et que celle de saison est égale à “ete”, affichez
#“Poire, fraise, cassis”
#Si la valeur de “type” est égale à “legume” et que celle de saison est égale à “hiver”,
#affichez “carotte, topinambour, endive”
#Si la valeur de “type” est égale à “legume” et que celle de saison est égale à “ete”,
#affichez “artichaut, aubergine,navet”


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


fonction ("fruits", "été")