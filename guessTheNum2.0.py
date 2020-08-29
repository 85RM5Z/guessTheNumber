from menu import *
from demandeSasieNbMystere import *
from jeu import *
import random

#Améliorations possible:
#1)Proposer une aide (que l'utilisateur peut refuser ou non) qui montrera un interval plus en plus reduite pour faciliter a trouver le bon nombre.  
#2)Limiter le nombre de coups par manche.
#3)Enregistrer les meilleur score.
#4)Offrir la posibiliter de refaire une partie.

def guessTheNumber():

   choix = menu()
   choix = int(choix)

   if choix == 1:
      nbAdeviner = random.randint(0, 100)
      jeu(demande_saisie_nb_mystere(1),nbAdeviner,0,100)
   elif choix == 2:
      nbAdeviner = random.randint(0, 1000)
      jeu(demande_saisie_nb_mystere(2),nbAdeviner,0,1000)
   elif choix == 3:
   	  nbAdeviner = random.randint(0, 1000000)
   	  jeu(demande_saisie_nb_mystere(3),nbAdeviner,0,1000000)
   else:
   	  nbAdeviner = random.randint(0, 1000000000000)
   	  jeu(demande_saisie_nb_mystere(4),nbAdeviner,0,1000000000000)


guessTheNumber()