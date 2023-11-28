#Écrire un programme qui affiche dans la console un rectangle avec des ‘-’ et des ‘|’ en
#fonction des paramètres d’entrées, (width, height), par exemple :
#draw_rectangle(10, 3)
#

def draw_rectangle(width, height):              #def function      
    for i in range(height):
        if i == 0 or i == height - 1:
                                                  # Fisrt and last line :full line
        else:
                                                  #interior lines : show '|',space (width - 2) multiple, then '|'
            print('|' + ' ' * (width - 2) + '|')

# Use avec draw_rectangle(10, 3)  'example)
draw_rectangle(10, 3)