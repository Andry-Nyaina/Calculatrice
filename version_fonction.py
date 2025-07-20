def addition(a, b):
    return a + b
def soustraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Erreur: Division par zéro"
    return a / b

a = float(input("Entrer le premier nombre: "))
b = float(input("Entrer le deuxième nombre: "))

print("Choisissez une opération:")
op = input("1. Addition\n2. Soustraction\n3. Multiplication\n4. Division\n")
if op == '1':
    result = addition(a, b)
elif op == '2':
    result = soustraction(a, b)
elif op == '3':
    result = multiplication(a, b)
elif op == '4':
    result = division(a, b)
else:
    result = "Opération invalide"
print(f"Le résultat est: {result}") 