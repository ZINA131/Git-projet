n = int(input("Entrez un nombre : "))
somme = 0
for i in range(1, n):
    if n % i == 0:
        somme += i
if somme == n:
    print("Nombre parfait")
else:
    print("Nombre non parfait")