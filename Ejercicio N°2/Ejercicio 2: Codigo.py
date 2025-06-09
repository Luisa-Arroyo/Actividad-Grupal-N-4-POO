import tkinter as tk
from tkinter import ttk, messagebox
import math


# Jerarquía de Clases para Figuras Geometricas


class Figura:
    """
    Clase base para todas las figuras geométricas
    Define la interfaz para calcular volumen y superficie
    """
    def volumen(self):
        raise NotImplementedError("Este metodo debe implementarse en la subclase")


    def superficie(self):
        raise NotImplementedError("Este metodo debe implementarse en la subclase")


class Cilindro(Figura):
    """
    Representa un cilindro dado su radio y altura
    """
    def __init__(self, radio: float, altura: float):
        self.radio = radio
        self.altura = altura


    def volumen(self) -> float:
        return math.pi * (self.radio ** 2) * self.altura


    def superficie(self) -> float:
        return 2 * math.pi * self.radio * (self.radio + self.altura)


class Esfera(Figura):
    """
    Representa una esfera dado su radio
    """
    def __init__(self, radio: float):
        self.radio = radio


    def volumen(self) -> float:
        return (4.0/3.0) * math.pi * (self.radio ** 3)


    def superficie(self) -> float:
        return 4 * math.pi * (self.radio ** 2)


class Piramide(Figura):
    """
    Representa una piramide dada su base 
    Se asume que la piramide tiene base cuadrada
    """
    def __init__(self, base: float, altura: float, apotema: float):
        self.base = base
        self.altura = altura
        self.apotema = apotema


    def volumen(self) -> float:
        return (1.0/3.0) * (self.base ** 2) * self.altura


    def superficie(self) -> float:
        area_base = self.base ** 2
        area_caras = 4 * ((self.base * self.apotema) / 2.0)
        return area_base + area_caras


class AppFiguras:
    """
    Aplicación de ventana única para calcular volumen y superficie
    del Cilindro, la Esfera y la Piramide 
    """


    def __init__(self, root: tk.Tk):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Calculo de Volumen y Superficie de Figuras")       
        self.root.geometry("450x400")                                       
        self.root.resizable(False, False)                                     
        self.root.configure(padx=10, pady=10)


        # Titulo de la aplicación
        titulo = tk.Label(root, text="Tienda de Figuras Geometricas", font=("Helvetica", 16, "bold"))
        titulo.pack(pady=(0, 10))


        # Selector de figura 
        self.tipo_figura = tk.StringVar(value="Cilindro")
        frame_opciones = tk.LabelFrame(root, text="Seleccione Figura")
        frame_opciones.pack(fill="x", pady=(0, 10))


        tk.Radiobutton(frame_opciones, text="Cilindro", variable=self.tipo_figura,
                       value="Cilindro", command=self._mostrar_campos).pack(side="left", padx=5, pady=5)
        tk.Radiobutton(frame_opciones, text="Esfera", variable=self.tipo_figura,
                       value="Esfera", command=self._mostrar_campos).pack(side="left", padx=5, pady=5)
        tk.Radiobutton(frame_opciones, text="Piramide", variable=self.tipo_figura,
                       value="Piramide", command=self._mostrar_campos).pack(side="left", padx=5, pady=5)


        # Contenedor para los campos dinamicos segun figura
        self.frame_campos = tk.Frame(root)
        self.frame_campos.pack(fill="both", expand=True)


        # Boton de Calcular
        btn_calcular = tk.Button(root, text="Calcular", command=self._calcular)  
        btn_calcular.pack(pady=(10, 5))


        # Etiqueta para mostrar resultados
        self.lbl_resultados = tk.Label(root, text="", justify="left", font=("Courier", 10))
        self.lbl_resultados.pack(pady=(10, 0))


        # Inicialmente mostrar campos para Cilindro
        self._mostrar_campos()


    def _limpiar_campos(self):
        "Elimina todos los widgets hijos del frame de campos antes de mostrar otros"
        for widget in self.frame_campos.winfo_children():
            widget.destroy()


    def _mostrar_campos(self):
        """
        Muestra los campos de entrada correspondientes a la figura seleccionada
        Se invoca cada vez que el usuario cambia la selección de figura
        """
        self._limpiar_campos()
        tipo = self.tipo_figura.get()


        if tipo == "Cilindro":
            lbl_radio = tk.Label(self.frame_campos, text="Radio (cm):")
            lbl_radio.grid(row=0, column=0, sticky="e", pady=5)
            self.ent_radio = tk.Entry(self.frame_campos)
            self.ent_radio.grid(row=0, column=1, pady=5)


            lbl_altura = tk.Label(self.frame_campos, text="Altura (cm):")
            lbl_altura.grid(row=1, column=0, sticky="e", pady=5)
            self.ent_altura = tk.Entry(self.frame_campos)
            self.ent_altura.grid(row=1, column=1, pady=5)


        elif tipo == "Esfera":
            lbl_radio = tk.Label(self.frame_campos, text="Radio (cm):")
            lbl_radio.grid(row=0, column=0, sticky="e", pady=5)
            self.ent_radio = tk.Entry(self.frame_campos)
            self.ent_radio.grid(row=0, column=1, pady=5)


        elif tipo == "Piramide":
            lbl_base = tk.Label(self.frame_campos, text="Base (cm):")
            lbl_base.grid(row=0, column=0, sticky="e", pady=5)
            self.ent_base = tk.Entry(self.frame_campos)
            self.ent_base.grid(row=0, column=1, pady=5)


            lbl_altura = tk.Label(self.frame_campos, text="Altura (cm):")
            lbl_altura.grid(row=1, column=0, sticky="e", pady=5)
            self.ent_altura = tk.Entry(self.frame_campos)
            self.ent_altura.grid(row=1, column=1, pady=5)


            lbl_apotema = tk.Label(self.frame_campos, text="Apotema (cm):")
            lbl_apotema.grid(row=2, column=0, sticky="e", pady=5)
            self.ent_apotema = tk.Entry(self.frame_campos)
            self.ent_apotema.grid(row=2, column=1, pady=5)


    def _calcular(self):
        """
        Lee los valores ingresados, crea la instancia de la figura correspondiente,
        calcula volumen, superficie y muestra los resultados
        """
        tipo = self.tipo_figura.get()
        try:
            if tipo == "Cilindro":
                radio = float(self.ent_radio.get())
                altura = float(self.ent_altura.get())
                cilindro = Cilindro(radio, altura)
                vol = cilindro.volumen()
                sup = cilindro.superficie()
                texto = (f"Cilindro (r={radio} cm, h={altura} cm):\n"
                         f"  Volumen: {vol:.2f} cm³\n"
                         f"  Superficie: {sup:.2f} cm²")


            elif tipo == "Esfera":
                radio = float(self.ent_radio.get())
                esfera = Esfera(radio)
                vol = esfera.volumen()
                sup = esfera.superficie()
                texto = (f"Esfera (r={radio} cm):\n"
                         f"  Volumen: {vol:.2f} cm³\n"
                         f"  Superficie: {sup:.2f} cm²")


            else:  # Piramide
                base = float(self.ent_base.get())
                altura = float(self.ent_altura.get())
                apotema = float(self.ent_apotema.get())
                piramide = Piramide(base, altura, apotema)
                vol = piramide.volumen()
                sup = piramide.superficie()
                texto = (f"Piramide (b={base} cm, h={altura} cm, ap={apotema} cm):\n"
                         f"  Volumen: {vol:.2f} cm³\n"
                         f"  Superficie: {sup:.2f} cm²")


            # Mostrar resultados en etiqueta
            self.lbl_resultados.config(text=texto)


        except ValueError:
            # Si el usuario ingresa texto no numerico, mostrar error
            messagebox.showerror("Error de entrada", "Por favor ingresa valores numericos validos")


# Ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()           
    app = AppFiguras(root)
    root.mainloop()
