montant_mad = float(input("Entrez le montant en MAD : "))
taux_conversion = float(input("Entrez le taux de conversion (MAD -> EUR) : "))
montant_eur = montant_mad * taux_conversion
print(f"Le montant en euros est : {montant_eur} EUR")