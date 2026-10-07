class CuentaBancaria:
    """
    Clase que demuestra la encapsulación y la modificación/consulta del estado de un objeto.
    """
    def __init__(self, titular: str, saldo_inicial: float):
        self._titular = titular      # Atributo protegido
        self._saldo = saldo_inicial  # Atributo protegido

    # Getters y Setters para el titular
    def get_titular(self) -> str:
        return self._titular

    def set_titular(self, nuevo_titular: str) -> None:
        if nuevo_titular.strip():
            self._titular = nuevo_titular

    # Getters y Setters para el saldo
    def get_saldo(self) -> float:
        return self._saldo

    def set_saldo(self, nuevo_saldo: float) -> None:
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo
        else:
            print("El saldo no puede ser negativo.")

# Demostración del cambio de estado
if __name__ == "__main__":
    cuenta = CuentaBancaria("Laura Restrepo", 150000.0)
    
    # Consulta de estado inicial
    print(f"Estado inicial - Titular: {cuenta.get_titular()}, Saldo: ${cuenta.get_saldo()}")

    # Modificación del estado (Setters)
    cuenta.set_saldo(200000.0)
    
    # Consulta de nuevo estado
    print(f"Estado modificado - Titular: {cuenta.get_titular()}, Saldo: ${cuenta.get_saldo()}")