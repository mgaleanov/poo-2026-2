class Estudiante:
    """
    Clase Estudiante con atributos de diferentes tipos primitivos/básicos de datos.
    """
    def __init__(self, nombre: str, edad: int, promedio: float, matriculado: bool):
        self.nombre: str = nombre
        self.edad: int = edad
        self.promedio: float = promedio
        self.matriculado: bool = matriculado

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Promedio: {self.promedio}")
        print(f"Matriculado: {'Sí' if self.matriculado else 'No'}")

# Uso de la clase
if __name__ == "__main__":
    estudiante1 = Estudiante("Carlos Gómez", 20, 4.2, True)
    estudiante1.mostrar_informacion()