n = int(input("Entrez un nombre : "))
temp = n
somme = 0
while temp > 0:
    chiffre = temp % 10
    fact = 1
    for i in range(1, chiffre + 1):
        fact *= i
    somme += fact
    temp //= 10
if somme == n:
    print("Nombre fort")
else:
    print("Nombre non fort")