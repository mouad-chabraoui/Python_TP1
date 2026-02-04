'''
Ecrire un programme python permettant d’afficher la table de multiplication d’un entier saisi par
l’utilisateur en utilisant la boucle « for ».
'''
# i replace space " " by no space "" so that the programe work even if the user put a space in the number
n = int(input("enter a number: ").strip().replace(" ",""))
ne = 1
print("la table de multiplication de",n,":")
for _ in range(10):
    print( n, "*", ne, "=", n * ne)
    ne += 1
