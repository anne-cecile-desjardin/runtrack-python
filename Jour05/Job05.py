#Jules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses
#messages. Sa méthode était assez simple : il décalait les lettres de trois rangs dans
#l'alphabet.
#Créer une fonction à laquelle on donne un message et un décalage, et la fonction
#renvoie alors le message décalé dans l'alphabet. Il faudra gérer le dépassement ('z'
#décalé vers la droite












#Caesar Cipher in Cryptography
#The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions, known as the “shift” or “key”.
#The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.
#Thus to cipher a given text we need an integer value, known as a shift which indicates the number of positions each letter of the text has been moved down. 
#The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,…, Z = 25. Encryption of a letter by a shift n can be described mathematically as. 
    #For example, if the shift is 3, then the letter A would be replaced by the letter D, B would become E, C would become F, and so on. The alphabet is wrapped around so that after Z, it starts back at A.
    #Here is an example of how to use the Caesar cipher to encrypt the message “HELLO” with a shift of 3:

    #Write down the plaintext message: HELLO
    #Choose a shift value. In this case, we will use a shift of 3.
    #Replace each letter in the plaintext message with the letter that is three positions to the right in the alphabet.

     #H becomes K (shift 3 from H)

        # E becomes H (shift 3 from E)

        # L becomes O (shift 3 from L)

        # L becomes O (shift 3 from L)
   #O becomes R (shift 3 from O)

      #4.The encrypted message is now “KHOOR”.

    #To decrypt the message, you simply need to shift each letter back by the same number of positions. In this case, you would shift each letter in “KHOOR” back by 3 positions to get the original message, “HELLO”.

 

#E_n(x)=(x+n)mod\ 26
#(Encryption Phase with shift n)

#D_n(x)=(x-n)mod\ 26
#(Decryption Phase with shift n)
#Examples : 

#Text : ABCDEFGHIJKLMNOPQRSTUVWXYZ
#Shift: 23
#Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW

#Text : ATTACKATONCE
#Shift: 4
#Cipher: EXXEGOEXSRGI

#Advantages:

#    Easy to implement and use thus, making suitable for beginners to learn about encryption.
#    Can be physically implemented, such as with a set of rotating disks or a set of cards, known as a scytale, which can be useful in certain situations.
#    Requires only a small set of pre-shared information.
#    Can be modified easily to create a more secure variant, such as by using a multiple shift values or keywords.

#Disadvantages:
#
#    It is not secure against modern decryption methods.
#    Vulnerable to known-plaintext attacks, where an attacker has access to both the encrypted and unencrypted versions of the same messages.
#    The small number of possible keys means that an attacker can easily try all possible keys until the correct one is found, making it vulnerable to a brute force attack.
#    It is not suitable for long text encryption as it would be easy to crack.
#
#    It is not suitable for secure communication as it is easily broken.
#    Does not provide confidentiality, integrity, and authenticity in a message. 
#    in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
#    Fixed key: The Caesar cipher uses a fixed key, which is the number of positions by which the letters are shifted. This key is known to both the sender and the receiver.
#    Symmetric encryption: The Caesar cipher is a symmetric encryption technique, meaning that the same key is used for both encryption and decryption.
#    Limited keyspace: The Caesar cipher has a very limited keyspace of only 26 possible keys, as there are only 26 letters in the English alphabet.
#    Vulnerable to brute force attacks: The Caesar cipher is vulnerable to brute force attacks, as there are only 26 possible keys to try.
#    Easy to implement: The Caesar cipher is very easy to implement and requires only simple arithmetic operations, making it a popular choice for simple encryption tasks.


#Features of caesar cipher:

#    Substitution cipher: The Caesar cipher is a type of substitution cipher, where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
#    Fixed key: The Caesar cipher uses a fixed key, which is the number of positions by which the letters are shifted. This key is known to both the sender and the receiver.
#    Symmetric encryption: The Caesar cipher is a symmetric encryption technique, meaning that the same key is used for both encryption and decryption.#
#    Limited keyspace: The Caesar cipher has a very limited keyspace of only 26 possible keys, as there are only 26 letters in the English alphabet.
#    Vulnerable to brute force attacks: The Caesar cipher is vulnerable to brute force attacks, as there are only 26 possible keys to try.
#    Easy to implement: The Caesar cipher is very easy to implement and requires only simple arithmetic operations, making it a popular choice for simple encryption tasks.

#Rules for the Caesar Cipher:

#    Choose a number between 1 and 25. This will be your “shift” value.
#    Write down the letters of the alphabet in order, from A to Z.
#    Shift each letter of the alphabet by the “shift” value. For example, if the shift value is 3, A would become D, B would become E, C would become F, and so on.
#    Encrypt your message by replacing each letter with the corresponding shifted letter. For example, if the shift value is 3, the word “hello” would become “khoor”.
#    To decrypt the message, simply reverse the process by shifting each letter back by the same amount. For example, if the shift value is 3, the encrypted message “khoor” would become “hello”.

#Algorithm for Caesar Cipher: 
#Input: 

#    Choose a shift value between 1 and 25.
#    Write down the alphabet in order from A to Z.
#    Create a new alphabet by shifting each letter of the original alphabet by the shift value. For example, if the shift value is 3, the new alphabet would be:
#    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#    D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
#    Replace each letter of the message with the corresponding letter from the new alphabet. For example, if the shift value is 3, the word “hello” would become “khoor”.
#    To decrypt the message, shift each letter back by the same amount. For example, if the shift value is 3, the encrypted message “khoor” would become “hello”.

#Procedure: 

#    Traverse the given text one character at a time .
#    For each character, transform the given character as per the rule, depending on whether we’re encrypting or decrypting the text.
#    Return the new string generated.

#A program that receives a Text (string) and Shift value( integer) and returns the encrypted text. 




