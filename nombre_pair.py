# Afficher le but de l'application
print("Le nombre entré sera vérifier pour savoir s'il est pair ou non.")

# Lire le nombre à vérifier
nb_a_verifier = float(input("\nQuel est le nombre à vérifier : "))

# Vérifier si le nombre est pair, le résultat doit être "True" ou "False"
# Utiliser un opérateur arithmétique ET logique
est_pair = nb_a_verifier % 2 == 0
#                0| 1 == 0 --> True | False
# Afficher le résultat de la vérification
print(f"Le nombre est pair : {est_pair}")

