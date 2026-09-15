import math


class Circulo:

    def __init__(self, radio: float):
        self.radio = radio  # Atributo

    def calcular_area(self):  # Métodos
        return math.pi * (self.radio**2)

    def calcular_longitud(self):
        return 2 * math.pi * self.radio


# Uso
r = float(input("Ingrese el radio del círculo: "))
c = Circulo(r)
print(
    f"Área: {c.calcular_area():.2f}, Longitud: {c.calcular_longitud():.2f}"
)