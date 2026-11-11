class Vendedor:

    def __init__(self, nombre: str, apellidos: str, edad: int):
        self.verificar_edad(edad)
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    @staticmethod
    def verificar_edad(edad: int):
        # Evaluación del rango general (0 a 120 años)
        if edad < 0 or edad > 120:
            raise ValueError(
                "La edad no puede ser negativa ni mayor a 120 años."
            )

        # Evaluación de mayoría de edad (mínimo 18 años)
        if edad < 18:
            raise ValueError(
                "El vendedor debe ser mayor de 18 años para laborar."
            )

    def imprimir(self):
        print("\n--- DATOS DEL VENDEDOR ---")
        print(f"Nombre:    {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad:      {self.edad} años")


def main():
    print("=== REGISTRO DE VENDEDOR ===")
    try:
        nombre = input("Ingrese el nombre: ").strip()
        apellidos = input("Ingrese los apellidos: ").strip()
        edad = int(input("Ingrese la edad: "))

        # Instanciación y verificación
        vendedor = Vendedor(nombre, apellidos, edad)
        vendedor.imprimir()

    except ValueError as e:
        print(f"\n⚠️ Error de Validación: {e}")
    except Exception as e:
        print(f"\n⚠️ Error Inesperado: {e}")


if __name__ == "__main__":
    main()