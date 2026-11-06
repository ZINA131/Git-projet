chaine = input("Entrez une chaîne : ")
resultat = ""
for char in chaine:
    if char not in resultat:
        resultat += char
print(f"Résultat : {resultat}")