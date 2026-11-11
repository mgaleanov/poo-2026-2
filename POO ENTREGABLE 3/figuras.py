import math
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk, messagebox


# --- CLASE ABSTRACTA PADRE ---
class FiguraGeometrica(ABC):

    def __init__(self):
        self._volumen = 0.0
        self._superficie = 0.0

    @abstractmethod
    def calcular_volumen(self) -> float:
        pass

    @abstractmethod
    def calcular_superficie(self) -> float:
        pass

    @property
    def volumen(self) -> float:
        return self._volumen

    @property
    def superficie(self) -> float:
        return self._superficie


# --- SUBCLASE CILINDRO ---
class Cilindro(FiguraGeometrica):

    def __init__(self, radio: float, altura: float):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self._volumen = self.calcular_volumen()
        self._superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return math.pi * (self.radio**2) * self.altura

    def calcular_superficie(self) -> float:
        area_base = math.pi * (self.radio**2)
        area_lateral = 2 * math.pi * self.radio * self.altura
        return 2 * area_base + area_lateral


# --- SUBCLASE ESFERA ---
class Esfera(FiguraGeometrica):

    def __init__(self, radio: float):
        super().__init__()
        self.radio = radio
        self._volumen = self.calcular_volumen()
        self._superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return (4.0 / 3.0) * math.pi * (self.radio**3)

    def calcular_superficie(self) -> float:
        return 4.0 * math.pi * (self.radio**2)


# --- SUBCLASE PIRÁMIDE ---
class Piramide(FiguraGeometrica):

    def __init__(self, base: float, altura: float, apotema: float):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self._volumen = self.calcular_volumen()
        self._superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return ((self.base**2) * self.altura) / 3.0

    def calcular_superficie(self) -> float:
        area_base = self.base**2
        area_lateral = 2.0 * self.base * self.apotema
        return area_base + area_lateral


# --- INTERFAZ GRÁFICA CON PESTAÑAS (GUI) ---
class VentanaFiguras(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas 3D")
        self.geometry("420x360")
        self.resizable(False, False)

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        notebook.add(self._crear_panel_cilindro(), text="Cilindro")
        notebook.add(self._crear_panel_esfera(), text="Esfera")
        notebook.add(self._crear_panel_piramide(), text="Pirámide")

    def _crear_panel_cilindro(self):
        panel = ttk.Frame(self)

        ttk.Label(panel, text="Radio (cm):").grid(
            row=0, column=0, sticky="w", padx=10, pady=8
        )
        txt_radio = ttk.Entry(panel)
        txt_radio.grid(row=0, column=1, padx=10, pady=8)

        ttk.Label(panel, text="Altura (cm):").grid(
            row=1, column=0, sticky="w", padx=10, pady=8
        )
        txt_altura = ttk.Entry(panel)
        txt_altura.grid(row=1, column=1, padx=10, pady=8)

        lbl_vol = ttk.Label(panel, text="Volumen: ")
        lbl_vol.grid(
            row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5
        )

        lbl_sup = ttk.Label(panel, text="Superficie: ")
        lbl_sup.grid(
            row=4, column=0, columnspan=2, sticky="w", padx=10, pady=5
        )

        def calcular():
            try:
                r = float(txt_radio.get())
                h = float(txt_altura.get())
                cil = Cilindro(r, h)
                lbl_vol.config(text=f"Volumen: {cil.volumen:.2f} cm³")
                lbl_sup.config(text=f"Superficie: {cil.superficie:.2f} cm²")
            except ValueError:
                messagebox.showerror(
                    "Error", "Ingrese valores numéricos válidos."
                )

        btn = ttk.Button(panel, text="Calcular", command=calcular)
        btn.grid(row=2, column=0, columnspan=2, pady=10)

        return panel

    def _crear_panel_esfera(self):
        panel = ttk.Frame(self)

        ttk.Label(panel, text="Radio (cm):").grid(
            row=0, column=0, sticky="w", padx=10, pady=8
        )
        txt_radio = ttk.Entry(panel)
        txt_radio.grid(row=0, column=1, padx=10, pady=8)

        lbl_vol = ttk.Label(panel, text="Volumen: ")
        lbl_vol.grid(
            row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5
        )

        lbl_sup = ttk.Label(panel, text="Superficie: ")
        lbl_sup.grid(
            row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5
        )

        def calcular():
            try:
                r = float(txt_radio.get())
                esf = Esfera(r)
                lbl_vol.config(text=f"Volumen: {esf.volumen:.2f} cm³")
                lbl_sup.config(text=f"Superficie: {esf.superficie:.2f} cm²")
            except ValueError:
                messagebox.showerror(
                    "Error", "Ingrese valores numéricos válidos."
                )

        btn = ttk.Button(panel, text="Calcular", command=calcular)
        btn.grid(row=1, column=0, columnspan=2, pady=10)

        return panel

    def _crear_panel_piramide(self):
        panel = ttk.Frame(self)

        ttk.Label(panel, text="Base (cm):").grid(
            row=0, column=0, sticky="w", padx=10, pady=6
        )
        txt_base = ttk.Entry(panel)
        txt_base.grid(row=0, column=1, padx=10, pady=6)

        ttk.Label(panel, text="Altura (cm):").grid(
            row=1, column=0, sticky="w", padx=10, pady=6
        )
        txt_altura = ttk.Entry(panel)
        txt_altura.grid(row=1, column=1, padx=10, pady=6)

        ttk.Label(panel, text="Apotema (cm):").grid(
            row=2, column=0, sticky="w", padx=10, pady=6
        )
        txt_apotema = ttk.Entry(panel)
        txt_apotema.grid(row=2, column=1, padx=10, pady=6)

        lbl_vol = ttk.Label(panel, text="Volumen: ")
        lbl_vol.grid(
            row=4, column=0, columnspan=2, sticky="w", padx=10, pady=5
        )

        lbl_sup = ttk.Label(panel, text="Superficie: ")
        lbl_sup.grid(
            row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5
        )

        def calcular():
            try:
                b = float(txt_base.get())
                h = float(txt_altura.get())
                a = float(txt_apotema.get())
                pir = Piramide(b, h, a)
                lbl_vol.config(text=f"Volumen: {pir.volumen:.2f} cm³")
                lbl_sup.config(text=f"Superficie: {pir.superficie:.2f} cm²")
            except ValueError:
                messagebox.showerror(
                    "Error", "Ingrese valores numéricos válidos."
                )

        btn = ttk.Button(panel, text="Calcular", command=calcular)
        btn.grid(row=3, column=0, columnspan=2, pady=10)

        return panel


if __name__ == "__main__":
    app = VentanaFiguras()
    app.mainloop()