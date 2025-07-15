a = b = ""

while not (a.isdigit() and b.isdigit()):
    a = input("Entrer la premier nombre: ")
    b = input("Entre la deuxième nombre: ")
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer un nombre valide")
    else:
        addition = (int(a)+int(b))
print(f"La somme de {a} et {b} est {addition}")