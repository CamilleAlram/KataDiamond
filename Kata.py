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
    i = 0
    while i < cote:
        j = i
        k = i
        l = i
        rendu = ''
        while j < cote - 1:
            rendu += ' '
            j += 1
        rendu += liste[i]
        while k > 0:
            rendu += ' '
            k -= 1
        while l > 1:
            rendu += ' '
            l -= 1
        if i != 0:
            rendu += liste[i]
        print(rendu)
        i += 1
    # Bas du diamant
    i = cote - 2
    while i >= 0:
        j = 1
        k = cote
        l = cote
        rendu = ''
        while j < cote - i:
            rendu += ' '
            j += 1
        rendu += liste[i]
        while k > cote - i:
            rendu += ' '
            k -= 1
        while l > cote - i + 1:
            rendu += ' '
            l -= 1
        if i != 0:
            rendu += liste[i]
        print(rendu)
        i -= 1

if __name__ == '__main__':
    liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    afficheDiamant(liste)
