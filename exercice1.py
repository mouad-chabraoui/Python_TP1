'''
Ecrire un programme python qui permet de lire au clavier 3 valeurs numériques entières. Le script
permet de réaliser les tâches suivantes:
- Calculer et afficher la somme, la moyenne et le produit des 3 valeurs.
- Réafficher les 3 valeurs triées dans l’ordre croissant.
'''
# so the user can input the numbers :
a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxième nombre : "))
c = int(input("Entrez le troisième nombre : "))

# Calculs :
somme = a + b + c
moyenne = somme / 3
produit = a * b * c 

# Affichage des résultats:
print("Somme :", somme)
print("Moyenne :", moyenne)
print("Produit :", produit)

# Tri des valeurs
valeurs = [a, b, c]
valeurs.sort()

print("Valeurs triées (ordre croissant) :", valeurs)
