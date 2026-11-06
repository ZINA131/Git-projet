x = int(input("Entrez X : "))
n = int(input("Entrez N : "))
resultat = 1
for i in range(n):
    resultat *= x
print(f"{x}^{n} = {resultat}")