#Écrire un programme qui itère les nombres entiers de 1 à 100. Pour les multiples de trois,
#afficher "Fizz" au lieu du nombre et pour les multiples de cinq afficher "Buzz".
#Pour les nombres qui sont des multiples de trois
#et cinq, afficher "FizzBuzz".

for nombre in range(1, 101):
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    elif nombre % 3 == 0:
        print("Fizz")
    elif nombre % 5 == 0:
        print("Buzz")
    else:
        print(nombre)