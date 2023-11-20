
montant_initial = 10000  # Montant en euros
taux_rendement_annuel = 5  # Taux en pourcentage

# Print le gain initial
gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Le gain annuel initial est de : {gain_annuel} euros")

# Print chgt
montant_initial += 5000
taux_rendement_annuel += 2

# Print un calcul
nouveau_gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Le nouveau gain annuel est de : {nouveau_gain_annuel} euros")

# Print 2 variables
montant_initial -= montant_initial * 0.10
taux_rendement_annuel -= 1

# Print final
montant_final = montant_initial * (1 + taux_rendement_annuel / 100)
print(f"Le montant final de l'investissement est de : {montant_final} euros")

