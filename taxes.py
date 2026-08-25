# Déclaration des variables
taux_TPS = 5 / 100
taux_TVQ = 9.975 / 100
montant_TPS = 0
montant_TVQ = 0
montant_total = 0

# Afficher le but de l'application
print("Les taxes de ventes seront ajoutées au montant entré.")

# Lire le montant avant taxe
montant_avant_taxe = float(input("Quel est le montant avant taxe : "))

# Utilisez les variables à votre disposition et vos connaissances pour faire tous les calculs nécessaires
montant_TPS = montant_avant_taxe * taux_TPS
montant_TVQ = montant_avant_taxe * taux_TVQ
montant_total= montant_avant_taxe + montant_TPS + montant_TVQ

# Afficher la facture
print(f"""
Montant avant taxe      : {montant_avant_taxe:8.2f} $
Montant TPS             : {montant_TPS:8.2f} $
Montant TVQ             : {montant_TVQ:8.2f} $

Montant total           : {montant_total:8.2f} $
""")
