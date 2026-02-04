'''
Résolution de l'équation : ax2+bx+c=0
Ecrire un programme en python permettant de vérifier si cette équation possède des racines réelles
et de calculer leurs valeurs si elles existent en utilisant la structure « if ».
Utilisez la fonction sqrt() de la bibliothèque math pour calculer la racine carrée.
'''
a = int(input("Enter a value of a : "))
b = int(input("Enter a value of b : "))
c = int(input("Enter a value of c : "))

# on va determiner la valeur de delta
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    print("donc l'equation admit deux racine carre:")
    print("x1 = ",x1)
    print("x2 = ",x2)
elif delta == 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    print("x1 = ",x1)
else:
    print("l'equation admet pas des racine carre")
