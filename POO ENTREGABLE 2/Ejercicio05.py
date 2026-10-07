class Producto:
    """
    Clase que demuestra la definición y recepción de múltiples parámetros en métodos.
    """
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    # Método con un parámetro que modifica el estado interno
    def aplicar_descuento(self, porcentaje: float) -> None:
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Se aplicó un descuento del {porcentaje}%. Nuevo precio: ${self.precio:.2f}")

    # Método con múltiples parámetros que retorna un valor calculado
    def calcular_precio_total(self, cantidad: int, impuesto_porcentaje: float) -> float:
        subtotal = self.precio * cantidad
        impuesto = subtotal * (impuesto_porcentaje / 100)
        return subtotal + impuesto

# Prueba del objeto con parámetros
if __name__ == "__main__":
    laptop = Producto("Laptop Gamer", 3500000.0)
    
    # Aplicar descuento pasando un argumento
    laptop.aplicar_descuento(10.0)
    
    # Calcular total pasando cantidad e impuesto como argumentos
    total_compra = laptop.calcular_precio_total(cantidad=2, impuesto_porcentaje=19.0)
    print(f"Precio total por 2 unidades con 19% IVA: ${total_compra:.2f}")