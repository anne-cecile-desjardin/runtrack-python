#Créer une fonction nommée “time_to_text” qui prend en paramètre un nombre entier de
#minutes et affiche en console une chaine de caractère sous la forme de “X heures et Y
#minutes”.

def time_to_text(minutes):
    heures = minutes // 60
    minutes = minutes % 60
    print(f"{heures} heures et {minutes} minutes")
    
time_to_text(70)