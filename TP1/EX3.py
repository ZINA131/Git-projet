A = int(input("Entrez le nombre de A : "))
T = int(input("Entrez le nombre de T : "))
G = int(input("Entrez le nombre de G : "))
C = int(input("Entrez le nombre de C : "))
total_bases = A + T + G + C
pourcentage_GC = ((G + C) / total_bases) * 100
print(f"Le pourcentage de GC est : {pourcentage_GC}%")