#Écrire un programme qui affiche les nombres premiers jusqu’à 1000.

for n in range(0, 1000):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)