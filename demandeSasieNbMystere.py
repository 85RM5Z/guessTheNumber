import sys


def demande_saisie_nb_mystere(num):

    #aide = str(input("Voulais vous une aide qui vous facilitera de trouver la réponse?: "))
    #aide = str(aide)

    if num == 1:
        guess = input("Saisissez un nombre entre 1 et 100 :")
        try:
            guess = int(guess)
        except ValueError:
            print("La conversion de ce nombre est mal passée", file=sys.stderr)
            sys.exit()
    elif num == 2:
        guess = input("Saisissez un nombre entre 1 et 1000 :")
        try:
            guess = int(guess)
        except ValueError:
            print("La conversion de ce nombre est mal passée", file=sys.stderr)
            sys.exit()
    elif num == 3:
        guess = input("Saisissez un nombre entre 1 et 1000 000 :")
        try:
            guess = int(guess)
        except ValueError:
            print("La conversion de ce nombre est mal passée", file=sys.stderr)
            sys.exit()
    else:
        guess = input("Saisissez un nombre entre 1 et 1000 000 000 000 :")
        try:
            guess = int(guess)
        except ValueError:
            print("La conversion de ce nombre est mal passée", file=sys.stderr)
            sys.exit()
    return guess
