#Écrire un programme qui compte le nombre de multiples de 3 présents dans la liste
#L = [8, 24,48,2,16].

#English version
L = [8, 24, 48, 2, 16]                            #L: List containing numbers.

def count_multiples_of_3(lst):                    #Definition of a function named  #(lst) is the parameter list for the function.
    count = 0                                     #that takes a list (lst) as an argument.
    for number in lst:                            # Iterating through each element in the list.
        if number % 3 == 0:                       #Checking if the number is a multiple of 3.
            count += 1                            #Incrementing the count if the condition is met.
    return count                                  # Returning the final count from the function.

result = count_multiples_of_3(L)                  #Calling the function with the list L and storing the result in the variable result.
print(f"The number of multiples of 3 in the list is: {result}")  #Printing the final result.



L = [8, 24,48,2,16]                                 #Example "How to 23/11/2023 avec Pierre"

def multiple_de_3():
      count = 0
      for number in list:
        if number % 3 == 0:
            count += 1
        print(count)
            
multiple_de_3(L)



L = [8, 24, 48, 2, 16]                                         #Version française

def compter_multiples_de_3(ma_liste):                          #Liste définie /(lst) paramètre de la liste de la fonction.
    count = 0                                                  
    for number in ma_liste:
        if number % 3 == 0:
            count += 1
    return count

resultat = compter_multiples_de_3(L)
print(f"Le nombre de multiples de 3 dans la liste est : {resultat}")

def multiple_de_3(liste):
    count = 0
    for number in liste:
        if number % 3 == 0:
            count += 1
    print(count)

def autre_fonction():
    # Faites quelque chose ici
    pass

# Appel des fonctions
multiple_de_3(L)
autre_fonction()
