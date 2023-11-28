#Écrire un programme qui calcule le produit de toutes les valeurs de la liste comprises
#dans l’intervalle [25, 90]
#L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def produit_dans_intervalle(liste, borne_inf, borne_sup):
    produit = 1
    for nombre in liste:
        if borne_inf <= nombre <= borne_sup:
            produit *= nombre
    return produit

intervalle_inf = 25
intervalle_sup = 90

resultat_produit = produit_dans_intervalle(L, intervalle_inf, intervalle_sup)

print(f"Le produit des valeurs dans l'intervalle [{intervalle_inf}, {intervalle_sup}] est : {resultat_produit}")