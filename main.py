#### Fonction secondaire
'''
author : allan.carvalho@edu.esiee.fr
'''

def isprime(p):
    """
    Retourne si le nombre est divisible par 
    autre chose que 1 et lui même

    Argument :
        p: valeur entiere positive

    Return :
        isprime(p) = True / False
    """
    if p == 1 :
        return False
    for i in range (2,p) : #Regarde si divisible par autre chose que 1 et p
        if p % i == 0 :
            return False
        return True

print(isprime(13))

#### Fonction principale

def main():
    """
    Retournes les 100 premiers nombres premiers
    arg : n
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
