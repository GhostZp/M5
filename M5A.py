import random
nopat = []

arpa = int(input("Kuinka monta noppaa?: "))

for noppa in range(0,arpa):
    numero = (random.randint(1,6))
    nopat.append(numero)

print(f"Nopat {sum(nopat)}.")
