
import math
import tkinter as tk
from tkinter import messagebox


class Notas:

    def __init__(self, lista_notas: list[float]):
        self.lista_notas = lista_notas

    def calcular_promedio(self) -> float:
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion_estandar(self) -> float:
        prom = self.calcular_promedio()
        suma_cuadrados = sum((x - prom) ** 2 for x in self.lista_notas)
        return math.sqrt(suma_cuadrados / len(self.lista_notas))

    def calcular_mayor(self) -> float:
        return max(self.lista_notas)

    def calcular_menor(self) -> float:
        return min(self.lista_notas)


class VentanaNotas(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Cálculo de Notas de Estudiante")
        self.geometry("380x420")
        self.resizable(False, False)

        # Frame Entradas (Campos de Texto)
        frame_entradas = tk.LabelFrame(
            self, text="Ingrese las 5 Notas:", padx=10, pady=10
        )
        frame_entradas.pack(fill="x", padx=15, pady=10)

        self.entries_notas = []
        for i in range(5):
            lbl = tk.Label(frame_entradas, text=f"Nota {i+1}:")
            lbl.grid(row=i, column=0, sticky="w", pady=2)
            entry = tk.Entry(frame_entradas)
            entry.grid(row=i, column=1, sticky="ew", pady=2, padx=5)
            self.entries_notas.append(entry)

        # Frame Botones
        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=5)

        btn_calcular = tk.Button(
            frame_botones,
            text="Calcular",
            command=self.calcular,
            bg="#2b6cb0",
            fg="white",
            width=10,
        )
        btn_calcular.pack(side="left", padx=5)

        btn_limpiar = tk.Button(
            frame_botones, text="Limpiar", command=self.limpiar, width=10
        )
        btn_limpiar.pack(side="left", padx=5)

        # Frame Resultados
        frame_resultados = tk.LabelFrame(
            self, text="Resultados:", padx=10, pady=10
        )
        frame_resultados.pack(fill="both", expand=True, padx=15, pady=10)

        self.lbl_promedio = tk.Label(
            frame_resultados, text="Promedio: ", anchor="w"
        )
        self.lbl_promedio.pack(fill="x", pady=2)

        self.lbl_desviacion = tk.Label(
            frame_resultados, text="Desviación Estándar: ", anchor="w"
        )
        self.lbl_desviacion.pack(fill="x", pady=2)

        self.lbl_mayor = tk.Label(
            frame_resultados, text="Nota Mayor: ", anchor="w"
        )
        self.lbl_mayor.pack(fill="x", pady=2)

        self.lbl_menor = tk.Label(
            frame_resultados, text="Nota Menor: ", anchor="w"
        )
        self.lbl_menor.pack(fill="x", pady=2)

    def calcular(self):
        try:
            notas_arr = []
            for entry in self.entries_notas:
                val = float(entry.get())
                if val < 0.0 or val > 5.0:
                    messagebox.showerror(
                        "Error", "Las notas deben estar entre 0.0 y 5.0"
                    )
                    return
                notas_arr.append(val)

            objeto_notas = Notas(notas_arr)
            self.lbl_promedio.config(
                text=f"Promedio: {objeto_notas.calcular_promedio():.2f}"
            )
            self.lbl_desviacion.config(
                text=f"Desviación Estándar: {objeto_notas.calcular_desviacion_estandar():.2f}"
            )
            self.lbl_mayor.config(
                text=f"Nota Mayor: {objeto_notas.calcular_mayor():.2f}"
            )
            self.lbl_menor.config(
                text=f"Nota Menor: {objeto_notas.calcular_menor():.2f}"
            )

        except ValueError:
            messagebox.showerror(
                "Error de Entrada", "Por favor ingrese 5 números válidos."
            )

    def limpiar(self):
        for entry in self.entries_notas:
            entry.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio: ")
        self.lbl_desviacion.config(text="Desviación Estándar: ")
        self.lbl_mayor.config(text="Nota Mayor: ")
        self.lbl_menor.config(text="Nota Menor: ")


if __name__ == "__main__":
    app = VentanaNotas()
    app.mainloop()