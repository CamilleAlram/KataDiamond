def saisirValeur(liste):
    lettre = input('Qu''elle lettre ?')
    while liste.count(lettre) == 0:
        print('Il y a une erreur, vous devez ressaisir')
        lettre = input('Qu''elle lettre ?')
    cote = liste.index(lettre) + 1
    return cote


def afficheDiamant(liste):
    cote = saisirValeur(liste)
    # Haut du diamant
    for i in range(0, cote - 1):
        rendu = ''
        for j in range(i, cote - 2):
            rendu += ' '
        rendu += liste[i]
        for k in range(i, 0):
            rendu += ' '
        for l in range(i, 1):
            rendu += ' '
        if i != 0:
            rendu += liste[i]
        print(rendu)
    # Bas du diamant
    for i in range(cote, 0):
        rendu = ''
        for j in range(1, cote - i):
            rendu += ' '
        rendu += liste[i]
        for k in range(cote, cote - i):
            rendu += ' '
        for l in range(cote, cote - i + 1):
            rendu += ' '
        if i != 0:
            rendu += liste[i]
        print(rendu)

if __name__ == '__main__':
    liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    afficheDiamant(liste)
