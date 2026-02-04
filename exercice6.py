'''
Contexte: une entreprise produit des produits à un coût unitaire donné et les vend à un prix unitaire.
L'objectif d’écrire un programme en python afin de déterminer si l'entreprise réalise un bénéfice
ou une perte en fonction du nombre de produits produits et vendus.
Les critères sont les suivants :
- Si le revenu total est supérieur au coût total, l'entreprise réalise un bénéfice.
- Si le revenu total est inférieur au coût total, l'entreprise subit une perte.
- Si le revenu total est égal au coût total, l'entreprise atteint le seuil de rentabilité.
'''
c_u = int(input("combien le cout unitaire par produit: "))
q_p = int(input("combien la quantite produit: "))
q_v = int(input("combien la quantite vendue: "))
p_v = int(input("combien le prix vendue par produit:"))

R_T = p_v * q_v
C_T = c_u * q_p

Result = R_T - C_T
if R_T > C_T:
    print("l'entreprise réalise un bénéfice de:",Result, "MAD")
elif R_T < C_T:
    print("l'entreprise subit une perte de:",Result, "MAD")
else:
    print("l'entreprise atteint le seuil de rentabilité.")
