#Écrire un programme qui affiche dans la console un triangle avec des ‘_’, des
#
#‘\’ et des ‘/’ en fonction de l’input entré, qui représentera la hauteur.
#Exemple si l’input entré est 5 :

def draw_triangle(height):                                      #Function
    for i in range(height):
                                                                 # Show spaces before the caracteres
        print(' ' * (height - i - 1), end='')

        # Show the caractere '_' for the first line, '\', '/' for the other lines
        if i == 0:
            print('_')
        elif i == height - 1:
            print('/' + '_' * (2 * i - 1) + '\\')
        else:
            print('/' + ' ' * (2 * i - 1) + '\\')

# How can we use draw_triangle(5) (example)
draw_triangle(5)

