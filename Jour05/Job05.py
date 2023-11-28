#Jules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses
#messages. Sa méthode était assez simple : il décalait les lettres de trois rangs dans
#l'alphabet.
#Créer une fonction à laquelle on donne un message et un décalage, et la fonction
#renvoie alors le message décalé dans l'alphabet. Il faudra gérer le dépassement ('z'
#décalé vers la droite

def numbering_cesar(message, ):                            #Function Definition:
    result = ''
    
    for char in message:                                  #for /char/
        if char.isalpha():                                #isalpha
            majuscule = char.isupper()                    # isupper

                                                          #
            code_decale = (code - ord('a') + decalage) % 26 + ord('a')

                                                         #Check if the Character is a Letter: 
            if majuscule:                                     
                result += chr(code_decale).upper() 
            else:
                result += chr(code_decale)
        else:
            result += char                             # 

    return result

#
message_original = "Bonjour, Cesar!"
decalage = 3
message_chiffre = numbering_cesar(message_original, decalage)

print(f"Message original: {message_original}")
print(f"Message chiffré : {message_chiffre}")




