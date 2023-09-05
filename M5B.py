numerot = []

numero = input("Anna ensimmäinen numero tai lopeta painamalla Enter: ")
while numero != "":
    numerot.append(numero)
    numero = input("Anna seuraava numero tai lopeta painamalla Enter: ")

numerot.sort(reverse=True)

print(f"{numerot}")

