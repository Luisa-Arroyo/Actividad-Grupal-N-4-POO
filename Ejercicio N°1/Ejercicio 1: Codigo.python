import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5

    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = sum((n - prom) ** 2 for n in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("300x400")
        self.resizable(False, False)
        self.notas = Notas()

        self.campos = []
        self._crear_widgets()

    def _crear_widgets(self):
        for i in range(5):
            etiqueta = tk.Label(self, text=f"Nota {i + 1}:")
            etiqueta.place(x=20, y=20 + i * 30)
            campo = tk.Entry(self)
            campo.place(x=100, y=20 + i * 30, width=150)
            self.campos.append(campo)

        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        btn_calcular.place(x=50, y=180)

        btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        btn_limpiar.place(x=160, y=180)

        self.lbl_promedio = tk.Label(self, text="Promedio = ")
        self.lbl_promedio.place(x=20, y=230)

        self.lbl_desviacion = tk.Label(self, text="Desviación = ")
        self.lbl_desviacion.place(x=20, y=260)

        self.lbl_mayor = tk.Label(self, text="Nota mayor = ")
        self.lbl_mayor.place(x=20, y=290)

        self.lbl_menor = tk.Label(self, text="Nota menor = ")
        self.lbl_menor.place(x=20, y=320)

    def calcular(self):
        try:
            for i in range(5):
                texto = self.campos[i].get()
                if texto.strip() == "":
                    raise ValueError(f"Debe ingresar la nota {i + 1}")
                self.notas.lista_notas[i] = float(texto)

            prom = self.notas.calcular_promedio()
            desv = self.notas.calcular_desviacion()
            mayor = self.notas.calcular_mayor()
            menor = self.notas.calcular_menor()

            self.lbl_promedio.config(text=f"Promedio = {prom:.2f}")
            self.lbl_desviacion.config(text=f"Desviación = {desv:.2f}")
            self.lbl_mayor.config(text=f"Nota mayor = {mayor:.2f}")
            self.lbl_menor.config(text=f"Nota menor = {menor:.2f}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación = ")
        self.lbl_mayor.config(text="Nota mayor = ")
        self.lbl_menor.config(text="Nota menor = ")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
