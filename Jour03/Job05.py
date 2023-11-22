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

calcule(10, '*', 10)  
    