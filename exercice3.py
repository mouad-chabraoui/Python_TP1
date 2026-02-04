"""
Une agence de location de voitures propose à ses clients les tarifs suivants:
Tarif par jour Tarif par kilomètre
Tarif essence: 150 MAD/jour || 1,20 MAD/km
Tarif diesel : 220 MAD/jour || 0,70 MAD/km
Ecrire un programme python qui produit un état détaillé indiquant le meilleur choix à un client qui
doit donner la distance qu’il doit parcourir et la durée de location (saisie).
"""
# ask the user for the distance and the time he need:
distance = int(input("how many miles do you need: ").strip().replace("km",""))
duree = int(input("how many days do you need: ").strip().replace("day",""))

# calcul des coûts totaux
cout_essence = (duree * 150) + (distance * 1.2)
cout_diesel = (duree * 220) + (distance * 0.7)

mailleur = min(cout_essence, cout_diesel)

print("Coût essence :", cout_essence, "MAD")
print("Coût diesel :", cout_diesel, "MAD")

if mailleur == cout_essence:
    print("le mailleur choix c'est: voiture essence")
    print(mailleur)
elif mailleur == cout_diesel:
    print("le mailleur choix c'est: voiture diesel")
    print("avec un cout de",mailleur,"MAD")
else:
    print("c'est le meme cout!")
