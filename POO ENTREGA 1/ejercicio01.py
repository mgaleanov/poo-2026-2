class Empleado:

    def __init__(
        self,
        horas_trabajadas: float = 48,
        valor_hora: float = 5000,
        retencion_pct: float = 0.125,
    ):
        self.horas_trabajadas = horas_trabajadas  # Atributos
        self.valor_hora = valor_hora
        self.retencion_pct = retencion_pct

    def calcular_salario_bruto(self):  # Métodos
        return self.horas_trabajadas * self.valor_hora

    def calcular_retencion(self):
        return self.calcular_salario_bruto() * self.retencion_pct

    def calcular_salario_neto(self):
        return self.calcular_salario_bruto() - self.calcular_retencion()


# Uso
emp = Empleado()
print(f"Salario Bruto: ${emp.calcular_salario_bruto():,.2f}")
print(f"Retención Fuente: ${emp.calcular_retencion():,.2f}")
print(f"Salario Neto: ${emp.calcular_salario_neto():,.2f}")