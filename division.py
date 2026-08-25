# Lire les nombres à diviser
flt1 = float(input("Quel est le premier nombre de la division : "))
flt2 = float(input("Quel est le deuxième nombre de la division : "))

# Diviser les nombres
quotient = flt1 / flt2

# Retenir seulement l'entier de la division
entier = flt1 // flt2

# Retenir seulement le reste de la division
reste = flt1 % flt2

# Afficher le quotient
print(f"\n{flt1} divisé par {flt2} égal : {quotient:.2f}")

# Afficher l'entier
print(f"L'entier de la division est : {entier:.0f}")

# Afficher le reste
print(f"Le reste de la division est : {reste:.0f}")
