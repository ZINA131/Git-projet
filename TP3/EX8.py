chaine = input("Entrez une chaîne : ")
char_cherche = input("Entrez le caractère à chercher : ")
compteur = 0
for char in chaine:
    if char == char_cherche:
        compteur += 1
print(f"Occurrence(s) : {compteur}")