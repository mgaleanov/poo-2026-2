import os


class LeerArchivo:

    def __init__(self, ruta_archivo: str = "prueba.txt"):
        self.ruta_archivo = ruta_archivo

    def crear_archivo_prueba_si_no_existe(self):
        """Genera el archivo con contenido de prueba en caso de que no exista."""
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "wb") as f:
                f.write(
                    b"Universidad Nacional de Colombia - Programacion Orientada a Objetos\nFlujo de bytes leido correctamente desde prueba.txt"
                )

    def leer_y_mostrar_bytes(self):
        print(
            f"=== LECTURA DE ARCHIVO POR FLUJO DE BYTES ({self.ruta_archivo}) ===\n"
        )
        try:
            self.crear_archivo_prueba_si_no_existe()

            # Apertura del archivo mediante flujo de bytes ('rb')
            with open(self.ruta_archivo, "rb") as archivo_flujo:
                contenido_bytes = archivo_flujo.read()
                print("--- CONTENIDO DECODIFICADO (TEXTO) ---")
                print(contenido_bytes.decode("utf-8"))
                print("\n--- REPRESENTACIÓN HEXADECIMAL / RAW BYTES ---")
                print(contenido_bytes)

        except FileNotFoundError:
            print(
                f"⚠️ Error: No se encontró el archivo '{self.ruta_archivo}'."
            )
        except IOError as ioe:
            print(
                f"⚠️ Error de Entrada/Salida al leer el flujo de bytes: {ioe}"
            )


def main():
    lector = LeerArchivo("prueba.txt")
    lector.leer_y_mostrar_bytes()


if __name__ == "__main__":
    main()