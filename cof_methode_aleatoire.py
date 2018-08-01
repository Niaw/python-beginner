# Créé par Niaw
# Ce script en langage Python permet de simuler les jets de dés
# pour le tirage des caractéristiques par la méthode aléatoire

from random import randint

print(
    'Méthode aléatoire :\n'
    'Pour créer un personnage, lancez quatre dés à six faces et\n'
    'faites la somme des trois meilleurs résultats à 6 reprises.\n'
    'Puis répartissez les valeurs obtenues dans les différentes caractéristiques.\n'
    'Modifiez-les selon la race du PJ et indiquez les Mod. correspondants.\n')

liste_carac = []
num_lancer = 1
while num_lancer <= 6:
    liste_jets = []
    num_jet = 1
    while num_jet <= 4:
        random_d6 = randint(1, 6)
        liste_jets.append(random_d6)
        num_jet = num_jet + 1
    # print(liste_jets) # Décommenter le 1er dièse pour voir les jets de dés
    liste_jets.remove(min(liste_jets))
    liste_carac.append(sum(liste_jets))
    num_lancer = num_lancer + 1
print('Caractéristiques :', liste_carac)
