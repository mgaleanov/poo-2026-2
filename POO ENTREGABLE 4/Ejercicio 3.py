import math


class CalculosNumericos:

    @staticmethod
    def calcular_logaritmo(valor: float) -> float:
        if valor <= 0:
            raise ArithmeticError(
                "Excepción Aritmética: El valor debe ser estrictamente positivo (> 0) para calcular el logaritmo neperiano."
            )
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor: float) -> float:
        if valor <= 0:
            raise ArithmeticError(
                "Excepción Aritmética: El valor debe ser estrictamente positivo (> 0) para calcular la raíz cuadrada real."
            )
        return math.sqrt(valor)


def main():
    print("=== MÓDULO DE CÁLCULOS NUMÉRICOS ===")
    try:
        numero = float(
            input("Ingrese un número double/float para operar: ")
        )

        log_resultado = CalculosNumericos.calcular_logaritmo(numero)
        print(f"✅ Logaritmo Neperiano de {numero}: {log_resultado:.4f}")

        raiz_resultado = CalculosNumericos.calcular_raiz_cuadrada(numero)
        print(f"✅ Raíz Cuadrada de {numero}: {raiz_resultado:.4f}")

    except ArithmeticError as ae:
        print(f"\n⚠️ {ae}")
    except ValueError:
        print(
            "\n⚠️ Error de Entrada: Debe ingresar un número decimal válido."
        )


if __name__ == "__main__":
    main()