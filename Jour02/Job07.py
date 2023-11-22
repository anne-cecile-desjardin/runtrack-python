#À partir de la chaîne "abcdefghijklmnopqrstuvwxyz" *
#10, écrivez un programme qui récupère et affiche autant
#de caractères que possible de cette chaîne sous forme
#de suite pyramidale.

chaine = "abcdefghijklmnopqrstuvwxyz" * 10
longueur = len(chaine) 

for i in range(1, longueur * 2,2):
    if i <= longueur:
        print(chaine[:i])

for i in range (1,10):
    subset = alphabet[:i*2-1]
    repeated_subset = (subset * 2)[:i*2-1]
    print(repeated_subset)
    


