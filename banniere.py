# Afficher le but de l'application
print("Entrez un message puis un caractère pour l'encadré et ils seront transformés en bannière.")

# Lire le message et le caractère
message = input("Entrez votre message : ")
caractere = input("Quel caractère désirez-vous pour l'encadrement : ")

# Calculer la longueur du message
longeur_msg = len(message)

# Créer la bannière
ligne_haut_bas = caractere * (longeur_msg + 4)
ligne_du_milieu = caractere + " " + message + " " + caractere

# Afficher la bannière
print(f"\n{ligne_haut_bas}")
print(ligne_du_milieu)
print(ligne_haut_bas)
