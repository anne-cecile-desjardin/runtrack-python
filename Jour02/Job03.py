#Créer un programme qui affiche tous les nombres de 0 à 100 compris SAUF 26, 37, 88

i = 0
while i <= 100:
    if i == 26 or i == 37 or i == 88:
        i = i + 1
        continue
    print(i)
    i = i + 1   