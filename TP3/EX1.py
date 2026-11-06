n = int(input("Entrez N : "))
if n > 0:
    s = 0
    for i in range(1, n + 1):
        s += 1 / i
    print(f"Somme = {s}")