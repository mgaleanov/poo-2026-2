class CalculadoraPotencias:

    def __init__(self, numero: float):
        self.numero = numero  # Atributo

    def obtener_cuadrado(self):  # Métodos
        return self.numero**2

    def obtener_cubo(self):
        return self.numero**3


# Uso
num = float(input("Ingrese un número: "))
calc = CalculadoraPotencias(num)
print(f"Cuadrado: {calc.obtener_cuadrado()}, Cubo: {calc.obtener_cubo()}")