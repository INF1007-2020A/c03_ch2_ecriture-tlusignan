#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    lettre = mot
    for lettre in mot:
        # TODO completer la fonction ici
        ordlettre = ord(lettre)
        ordlettre = ordlettre-32
        majlettre = chr(ordlettre)

        resultat += majlettre
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
