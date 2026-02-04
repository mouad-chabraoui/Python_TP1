'''
Écrire un programme python qui permet uniquement la saisie de nombres positifs en utilisant une
boucle « while ». Le programme doit continuer à demander une saisie tant que l'utilisateur n'entre
pas un nombre positif valide
'''
while True:
    number = int(input("enter a positive number: ").strip().replace(" ",""))
    if number > 0:
        break
# easy one
