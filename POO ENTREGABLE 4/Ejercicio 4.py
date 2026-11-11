class Programador:

    def __init__(self, nombre: str, apellidos: str):
        self.validar_campo(nombre, "Nombre")
        self.validar_campo(apellidos, "Apellidos")
        self.nombre = nombre
        self.apellidos = apellidos

    @staticmethod
    def validar_campo(valor: str, campo: str):
        # Validación: Solo texto (letras y espacios)
        if not valor.replace(" ", "").isalpha():
            raise ValueError(
                f"Excepción: El campo '{campo}' solo debe contener texto sin caracteres numéricos ni especiales."
            )

        # Validación: Longitud menor a 20 caracteres
        if len(valor) >= 20:
            raise ValueError(
                f"Excepción: El campo '{campo}' debe tener una longitud inferior a 20 caracteres (Actual: {len(valor)})."
            )


class EquipoMaratonProgramacion:

    def __init__(
        self, nombre_equipo: str, universidad: str, lenguaje: str
    ):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.programadores: list[Programador] = []

    def equipo_completo(self) -> bool:
        return len(self.programadores) >= 3

    def anadir_programador(self, programador: Programador):
        if len(self.programadores) >= 3:
            raise OverflowError(
                "Excepción de Capacidad: El equipo ya está lleno (máximo 3 integrantes)."
            )
        self.programadores.append(programador)
        print(
            f"--> Programador {programador.nombre} {programador.apellidos} añadido con éxito."
        )


def main():
    print("=== REGISTRO DE EQUIPO DE MARATÓN DE PROGRAMACIÓN ===")
    try:
        nombre_eq = input("Nombre del Equipo: ").strip()
        universidad = input("Universidad Representada: ").strip()
        lenguaje = input("Lenguaje de Programación a Usar: ").strip()

        equipo = EquipoMaratonProgramacion(
            nombre_eq, universidad, lenguaje
        )

        print("\n--- Registro de Integrantes (Mínimo 2, Máximo 3) ---")
        while not equipo.equipo_completo():
            ingresar_mas = "s"
            if len(equipo.programadores) >= 2:
                ingresar_mas = (
                    input(
                        "\nEl equipo ya cumple el mínimo (2). ¿Desea añadir el 3er integrante? (s/n): "
                    )
                    .strip()
                    .lower()
                )
                if ingresar_mas != "s":
                    break

            print(
                f"\nIntegrante #{len(equipo.programadores) + 1}:"
            )
            nom = input("  Nombre: ").strip()
            ape = input("  Apellidos: ").strip()

            prog = Programador(nom, ape)
            equipo.anadir_programador(prog)

        print("\n=== RESUMEN FINAL DEL EQUIPO ===")
        print(f"Equipo: {equipo.nombre_equipo} | Uni: {equipo.universidad}")
        print(f"Lenguaje: {equipo.lenguaje}")
        print(f"Total Integrantes: {len(equipo.programadores)}")
        for i, p in enumerate(equipo.programadores, 1):
            print(f"  {i}. {p.nombre} {p.apellidos}")

    except (ValueError, OverflowError) as err:
        print(f"\n⚠️ {err}")


if __name__ == "__main__":
    main()