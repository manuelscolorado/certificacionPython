import random
class Calculadora:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def suma(self):
        return self.a + self.b
    
    def resta(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        return self.a / self.b
    
a = random.randint(0,22)
b = random.randint(0,22)

cal = Calculadora(a, b)
print(f"a: {a}, b: {b}")
print("Suma:", cal.suma())
print("Resta:", cal.resta())
print("Multiplicacion:", cal.multiplicar())
print("Division:", cal.dividir())