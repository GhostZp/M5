virhe = False
luku = int(input("Kerro kokonaisluku: "))

for luvut in range(2, luku):
    if luku % luvut== 0:
        print(f"{luku} ei ole alkuluku.")
        virhe = True
        break

if virhe == False:
    print(f"{luku} on alkuluku.")