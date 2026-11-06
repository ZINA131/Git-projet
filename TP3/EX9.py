chaine = input("Entrez une chaîne : ")
chaine_epuree = chaine.replace(" ", "").lower()
if chaine_epuree == chaine_epuree[::-1]:
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")