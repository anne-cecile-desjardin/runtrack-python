#Écrire un programme qui compte le nombre de multiples de 3 présents dans la liste
#L = [8, 24,48,2,16].



L = [8, 24, 48, 2, 16]

def multiple_de_3(liste):
    count = 0
    for number in liste:
        if number % 3 == 0:
            count += 1
    return count

resultat = multiple_de_3(L)
print(f"Le nombre de multiples de 3 dans la liste est : {resultat}")

L = [8, 24,48,2,16]     #Example How to 23/11/2023

def multiple_de_3():
      count = 0
      for number in list:
        if number % 3 == 0:
            count += 1
        print(count)
            
multiple_de_3(L)

L = [8, 24,48,2,16]

L1 = []


def addition(liste):
    for i in liste:
        i