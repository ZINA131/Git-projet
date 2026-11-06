quantite = int(input("Entrez la quantité achetée : "))
prix_unitaire = float(input("Entrez le prix unitaire : "))
prix_total_avant = quantite * prix_unitaire
reduction = prix_total_avant * 0.15
prix_final = prix_total_avant - reduction
print(f"Prix total avant réduction : {prix_total_avant} MAD")
print(f"Montant de la réduction (15%) : {reduction} MAD")
print(f"Prix final à payer : {prix_final} MAD")