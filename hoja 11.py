import math
from abc import ABC, abstractmethod

class ExperimentoFisico(ABC):
    @abstractmethod
    def run(self):
        pass

class CaidaLibre(ExperimentoFisico):
    def __init__(self, h, g):
        if h < 0 or g <= 0:
            raise ValueError("La altura debe ser mayor o igual a cero y la gravedad mayor que cero.")
        self.h = h
        self.g = g

    def run(self):
        return math.sqrt(2 * self.h / self.g)

class CalculadoraCientifica:
    def calc(self, x):
        raise NotImplementedError("Este método debe ser implementado por una subclase.")

class Raiz(CalculadoraCientifica):
    def calc(self, x):
        if x < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(x)

class Potencia(CalculadoraCientifica):
    def calc(self, b, e):
        return math.pow(b, e)

class Logaritmo(CalculadoraCientifica):
    def calc(self, x):
        if x <= 0:
            raise ValueError("El logaritmo solo está definido para números positivos.")
        return math.log(x)

class Factorial(CalculadoraCientifica):
    def calc(self, x):
        if not isinstance(x, int) or x < 0:
            raise ValueError("El factorial solo está definido para enteros no negativos.")
        return math.factorial(x)

print("Simulación de Caída Libre")
h = float(input("Ingrese la altura (m): "))
g = float(input("Ingrese la gravedad (m/s²): "))
fall = CaidaLibre(h, g)
print("Tiempo de caída:", fall.run(), "segundos")

print("\nCalculadora Científica")
print("1. Raíz Cuadrada")
print("2. Potencia")
print("3. Logaritmo")
print("4. Factorial")
opt = input("Seleccione una opción: ")

if opt == "1":
    x = float(input("Ingrese el número: "))
    r = Raiz()
    print("Resultado:", r.calc(x))
elif opt == "2":
    b = float(input("Base: "))
    e = float(input("Exponente: "))
    p = Potencia()
    print("Resultado:", p.calc(b, e))
elif opt == "3":
    x = float(input("Ingrese el número: "))
    l = Logaritmo()
    print("Resultado:", l.calc(x))
elif opt == "4":
    x = int(input("Ingrese un número entero: "))
    f = Factorial()
    print("Resultado:", f.calc(x))
else:
    print("Opción no válida.")
