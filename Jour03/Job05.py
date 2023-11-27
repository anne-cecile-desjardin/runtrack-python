#Créer une fonction nommée “calcule” qui prend 3 paramètres :
#➔ Le premier, “num1”, est un nombre,
#➔ Le deuxième, "operator", est un caractère (string) contenant le type d’opération(+,
#-, *, /, %),
#➔ Le troisième, “num2”, est un nombre.
#La fonction doit retourner le résultat de l’opération.

def calcule(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "operation non validée"
    print(f"{num1} {operator} {num2} = {result}")

calcule(99, '*', 10)  
    