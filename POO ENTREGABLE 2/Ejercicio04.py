class Calculadora:
    """
    Clase para ilustrar métodos con y sin valor de retorno.
    """
    def __init__(self):
        pass

    # Método sin valor de retorno (retorna None)
    def saludar(self) -> None:
        print("¡Bienvenido al sistema de cálculo!")

    # Métodos con valor de retorno
    def sumar(self, a: float, b: float) -> float:
        return a + b

    def es_par(self, numero: int) -> bool:
        return numero % 2 == 0

# Prueba de métodos
if __name__ == "__main__":
    calc = Calculadora()
    
    # Llamada a método sin retorno
    calc.saludar()
    
    # Llamada a métodos con retorno
    resultado_suma = calc.sumar(12.5, 7.5)
    print(f"Resultado de la suma: {resultado_suma}")
    
    validacion = calc.es_par(8)
    print(f"¿El número 8 es par?: {validacion}")