class Calculatrice:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def soutraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Erreur: Division par zéro"
        

a = float(input("Entrer le premier nombre: "))
b = float(input("Entrer le deuxième nombre: "))

op = input("Choisissez une opération (1: Addition, 2: Soustraction, 3: Multiplication, 4: Division): ")
calc = Calculatrice(a, b)
if op == '1':
    result = calc.addition()
elif op == '2':
    result = calc.soustraction()
elif op == '3':
    result = calc.multiplication()
elif op == '4':
    result = calc.division()
else:
    result = "Opération invalide"
print(f"Le résultat est: {result}")
    

    