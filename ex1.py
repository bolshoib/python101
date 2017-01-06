#### -*-coding:Utf-8 -*
import time
import os
import random

def mtable(nb):
    #nb = 7 # On garde la variable contenant le nombre dont on veut la table de multiplication
    i = -1 # C'est notre variable compteur que nous allons incrémenter dans la boucle
    # Cas particulier du zéro on commence à -1 pour i + 1 = 0 ;-)
    while i < 10: # Tant que i est strictement inférieure à 10
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1 # On incrémente i de 1 à chaque tour de boucle
        time.sleep(1.5)

def mtablerandom(nb):
    i = 0
    cpt_success = 0
    while i < 10:
        randnb = random.randint(0, 10)
        #input(randnb '*' nb '= ?\n')
        print (randnb, '*', nb, '=', end=' ')
        #result1 = int(input ()) #risque erreur si on ne saisi pas un nombre
        result1 = size_input("")
        result2 = randnb * nb
        if result1 == result2:
            print ('Bravo !')
            cpt_success += 1
        else:
            print ('Oups ... c\'est pas bon, le résultat est : ', result2, '\n')
        i += 1
    print ('Note : ', cpt_success, '/ 10' )
    #percent_success = cpt_success * 100 /5
    #print (percent_success)
    print ('Pourcentage de réussite : ', cpt_success * 100 /10, '%')
#fonction pour risque d'erreur si on ne rentre pas un nombre
def size_input(message):
   try:
      ret = int(input(message))
      return ret
   except:
      return size_input("Oups ... Tu dois saisir un nombre ;-)\n")

nb = int(input('Quelle table de multiplication veux-tu réviser ?\n'))
print ('La table de : %s' % nb)
mtable(nb)
clrscr = input('OK ?\n')
os.system('cls' if os.name == 'nt' else 'clear')
mtablerandom(nb)