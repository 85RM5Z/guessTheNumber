import random
import sys


def guessTheNumber():

    mini, maxi = input("Entrer la borne min et la borne max: ").split()
    try:
        mini = int(mini)
        maxi = int(maxi)
    except ValueError:
        print("La conversion de ce nombre est mal passée", file=sys.stderr)
        sys.exit()
    print("Borne minimale : ", mini)
    print("Borne maximale : ", maxi)

    nombre = random.randint(mini, maxi)

    guess = int(input("Saisissez un nombre entre {} et {} :".format(mini, maxi)))
    try:
        guess = int(guess)
    except ValueError:
        print("La conversion de ce nombre est mal passée", file=sys.stderr)
        sys.exit()

    cpt = 0

    while not(guess == nombre):
        if guess > nombre:
            if guess > maxi:
                maxi = maxi
                raise Exception("La valeur que vous avez saisie est supérieur à la borne maximale")
            elif mini+1 != maxi and mini != maxi:
                maxi = guess-1
            else:
                maxi = guess
            print("Le nombre", guess, "est trop grand")
            guess = int(input("Saisissez un nombre entre {} et {} :".format(mini, maxi)))
            try:
                guess = int(guess)
            except ValueError:
                print("La conversion de ce nombre est mal passée", file=sys.stderr)
                sys.exit()
            cpt = cpt + 1
        else:
            if guess < mini:
                mini = mini
                raise Exception("La valeur que vous avez saisie est infèrieur à la borne minimale")
            elif guess+1 == maxi:
                mini = guess
                maxi = maxi+1
            else:
                mini = guess+1
            print("Le nombre", guess, "est trop petit")
            guess = int(input("Saisissez un nombre entre {} et {} :".format(mini, maxi)))
            try:
                guess = int(guess)
            except ValueError:
                print("La conversion de ce nombre est mal passée", file=sys.stderr)
                sys.exit()
            cpt = cpt + 1

    print("Gagné! vous avez trouver le bon nombre au bout de", cpt, "essaye(s).")


guessTheNumber()
