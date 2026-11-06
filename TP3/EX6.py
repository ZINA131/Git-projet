chaine = input("Entrez une chaîne : ")
inverse = ""
for char in chaine:
    inverse = char + inverse
print(f"Chaîne inversée : {inverse}")