duree_minutes = int(input("Entrez la durée en minutes : "))
heures = duree_minutes // 60
minutes = duree_minutes % 60
print(f"{duree_minutes} minutes = {heures} heures et {minutes} minutes")