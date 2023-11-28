#Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont aurez-de-chaussée...
#Écrire une fonction qui reçoit en paramètres, le nombre de marches du
#phare et la hauteur de chaque marche (en cm), cette fonction doit calculer
#combien de mètre le gardien effectué par semaine pour aller aux toilettes.La sortie du code doit être :
#Pour x marches de y cm, le gardien parcourt z.zz m par semaine.

#On n'oubliera pas :
#➔ Qu’une semaine comporte 7 jours ;
#➔ Qu’une fois en bas, le gardien doit remonter ;
#➔ Que le résultat est à exprimer en m.

def distance_toilettes_par_semaine_gardien(nb_marches, hauteur_marche):
    marches_par_jour = 5
    jours_par_semaine = 7

    distance_par_marche = hauteur_marche / 100                              # Convertir en mètres

    distance_par_jour = marches_par_jour * distance_par_marche
    distance_par_semaine = jours_par_semaine * distance_par_jour

    return distance_par_semaine

                                                                            # Exemple 
nb_marches_exemple = 100
hauteur_marche_exemple = 20
distance_totale = distance_toilettes_par_semaine_gardien(nb_marches_exemple, hauteur_marche_exemple)

print(f"Pour {nb_marches_exemple} marches de {hauteur_marche_exemple} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")


