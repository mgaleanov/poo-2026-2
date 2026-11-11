class PruebaExcepciones:

    @staticmethod
    def main():
        print("Inicio del programa")
        try:
            numerador = 10
            denominador = 0
            print("Realizando división...")
            resultado = numerador / denominador
            print(f"El resultado es: {resultado}")
        except ZeroDivisionError:
            print("Error: Excepción de división por cero capturada.")
        else:
            print("La división se realizó con éxito.")
        finally:
            print("Bloque 'finally' ejecutado: Liberación de recursos.")

        print("Fin del programa")


if __name__ == "__main__":
    PruebaExcepciones.main()