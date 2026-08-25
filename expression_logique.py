# Déclaration des variables
int1 = 4  # Type integer
int2 = 60  # Type integer
flt1 = 12.5  # Type float
flt2 = 3.3  # Type float
str1 = "Moyen"  # Type string
str2 = "moyen"  # Type string
str3 = "haut"  # Type string

# Section à un opérateur
# Est-ce que int1 et int2 sont égal ?
egalite = int1 == int2
# Afficher l'égalité
print(f"{int1} est égal à {int2} : {egalite}")

# Est-ce que str3 est plus petit que str2 ?
plus_petit = str3 < str2

# Afficher le résultat de la comparaison
print(f"{str3} est plus petit que {str2} : {plus_petit}")

# Est-ce que str1 est différent de str2 ?
different = str1!= str2

# Afficher le résultat de la comparaison
print(f"{str1} est différent de {str2} : {different}")

# Section à multiples opérateurs
# À faire à l'aide des mots clés "and" et "or", voir section Table de vérité des notes de cours

# Comparer l'égalité de int1 et int1 puis l'égalité de int1 et str1, le résultat doit être vrai
comparaison1 = (int1 == int1) or (int1 == str1)

# Afficher le résultat de la comparaison
print(f"La comparaison1 est : {comparaison1}")

# Vérifier si flt1 est plus petit que int1 et que int1 est plus petit que flt2, le résultat doit être faux.
comparaison2 = (flt1 < int1) and (int1 < flt2)

# Afficher le résultat de la comparaison
print(f"La comparaison2 est : {comparaison2}")

# Vérifier si flt1 est plus grand que int1 et que int1 est plus petit que flt2, le résultat doit être vrai.
comparaison3 = (flt1 > int1) or  (int1 < flt2)

# Afficher le résultat de la comparaison
print(f"La comparaison3 est : {comparaison3}")
