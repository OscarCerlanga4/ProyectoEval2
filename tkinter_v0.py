import tkinter as tk
from tkinter import messagebox

class Ascensor:
    def __init__(self, pisos_totales):
        self.pisos_totales = pisos_totales
        self.piso_actual = 1

    def subir(self):
        if self.piso_actual < self.pisos_totales:
            self.piso_actual += 1
            return f"Subiendo... Ahora estás en el piso {self.piso_actual}."
        else:
            return None  # Indica que no se puede subir más

    def bajar(self):
        if self.piso_actual > 1:
            self.piso_actual -= 1
            return f"Bajando... Ahora estás en el piso {self.piso_actual}."
        else:
            return None  # Indica que no se puede bajar más


class AscensorApp:
    def __init__(self, root, ascensor):
        self.root = root
        self.ascensor = ascensor

        self.root.title("Simulador de Ascensor")

        # Etiqueta de estado
        self.estado_label = tk.Label(root, text=f"Estás en el piso {self.ascensor.piso_actual}", font=("Arial", 14))
        self.estado_label.pack(pady=10)

        # Botones para subir, bajar y salir
        self.subir_button = tk.Button(root, text="Subir", command=self.subir, font=("Arial", 12))
        self.subir_button.pack(pady=5)

        self.bajar_button = tk.Button(root, text="Bajar", command=self.bajar, font=("Arial", 12))
        self.bajar_button.pack(pady=5)

        self.salir_button = tk.Button(root, text="Salir del Ascensor", command=self.salir, font=("Arial", 12), fg="red")
        self.salir_button.pack(pady=20)

    def subir(self):
        mensaje = self.ascensor.subir()
        self.actualizar_estado()
        if mensaje is None:  # Si no se puede subir más
            messagebox.showinfo("Información", "Ya estás en el último piso. No puedes subir más.")

    def bajar(self):
        mensaje = self.ascensor.bajar()
        self.actualizar_estado()
        if mensaje is None:  # Si no se puede bajar más
            messagebox.showinfo("Información", "Ya estás en la planta baja. No puedes bajar más.")

    def actualizar_estado(self):
        self.estado_label.config(text=f"Estás en el piso {self.ascensor.piso_actual}")

    def salir(self):
        self.root.destroy()


def main():
    ascensor = Ascensor(5)
    root = tk.Tk()
    app = AscensorApp(root, ascensor)
    root.mainloop()


if __name__ == "__main__":
    main()