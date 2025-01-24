import tkinter as tk
from tkinter import messagebox
import random

class Ascensor:
    def __init__(self, pisos_totales, capacidad_maxima, peso_maximo):
        self.pisos_totales = pisos_totales
        self.piso_actual = 1
        self.capacidad_actual = 0
        self.capacidad_maxima = capacidad_maxima
        self.peso_actual = 0
        self.peso_maximo = peso_maximo

    def subir(self):
        if self.piso_actual < self.pisos_totales:
            self.piso_actual += 1
            return f"Subiendo... Ahora estás en el piso {self.piso_actual}."
        else:
            return None

    def bajar(self):
        if self.piso_actual > 1:
            self.piso_actual -= 1
            return f"Bajando... Ahora estás en el piso {self.piso_actual}."
        else:
            return None

    def entrar_persona(self):
        if self.capacidad_actual < self.capacidad_maxima:
            peso_persona = random.randint(50, 100)
            if self.peso_actual + peso_persona <= self.peso_maximo:
                self.capacidad_actual += 1
                self.peso_actual += peso_persona
                return f"Entró una persona con {peso_persona} kg. Peso actual: {self.peso_actual}/{self.peso_maximo} kg."
            else:
                return f"No puede entrar una persona de {peso_persona} kg. Peso total excede el límite de {self.peso_maximo} kg."
        else:
            return "El ascensor está lleno. No puede entrar más personas."

    def salir_persona(self):
        if self.capacidad_actual > 0:
            peso_persona = random.randint(50, 100)
            self.capacidad_actual -= 1
            self.peso_actual -= peso_persona
            self.peso_actual = max(self.peso_actual, 0)
            return f"Salió una persona con {peso_persona} kg. Peso actual: {self.peso_actual}/{self.peso_maximo} kg."
        else:
            return "El ascensor está vacío. No hay personas para salir."

class AscensorApp:
    def __init__(self, root, ascensor):
        self.root = root
        self.ascensor = ascensor

        self.root.title("Simulador de Ascensor")
        self.center_window(400, 500)

        # Etiqueta de estado
        self.estado_label = tk.Label(root, text=f"Estás en el piso {self.ascensor.piso_actual}", font=("Arial", 14))
        self.estado_label.pack(pady=10)

        # Etiqueta de capacidad
        self.capacidad_label = tk.Label(root, text=f"Capacidad: {self.ascensor.capacidad_actual}/{self.ascensor.capacidad_maxima}", font=("Arial", 12))
        self.capacidad_label.pack(pady=5)

        # Etiqueta de peso
        self.peso_label = tk.Label(root, text=f"Peso: {self.ascensor.peso_actual}/{self.ascensor.peso_maximo} kg", font=("Arial", 12))
        self.peso_label.pack(pady=5)

        # Crear un frame para los botones
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Botones en una sola columna
        self.subir_button = tk.Button(self.button_frame, text="Subir", command=self.subir, font=("Arial", 12))
        self.subir_button.pack(fill=tk.X, pady=5)

        self.bajar_button = tk.Button(self.button_frame, text="Bajar", command=self.bajar, font=("Arial", 12))
        self.bajar_button.pack(fill=tk.X, pady=5)

        self.entrar_button = tk.Button(self.button_frame, text="Entrar persona", command=self.entrar_persona, font=("Arial", 12))
        self.entrar_button.pack(fill=tk.X, pady=5)

        self.salir_persona_button = tk.Button(self.button_frame, text="Salir persona", command=self.salir_persona, font=("Arial", 12))
        self.salir_persona_button.pack(fill=tk.X, pady=5)

        self.salir_button = tk.Button(root, text="Salir del Ascensor", command=self.salir, font=("Arial", 12), fg="red")
        self.salir_button.pack(pady=20)

        # Configuración para navegación con teclado
        self.buttons = [
            self.subir_button,
            self.bajar_button,
            self.entrar_button,
            self.salir_persona_button,
            self.salir_button
        ]
        self.current_button = 0
        self.buttons[self.current_button].focus_set()

        self.root.bind("<Up>", self.focus_previous_button)
        self.root.bind("<Down>", self.focus_next_button)
        self.root.bind("<Return>", self.activate_button)

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def focus_next_button(self, event):
        self.current_button = (self.current_button + 1) % len(self.buttons)
        self.buttons[self.current_button].focus_set()

    def focus_previous_button(self, event):
        self.current_button = (self.current_button - 1) % len(self.buttons)
        self.buttons[self.current_button].focus_set()

    def activate_button(self, event):
        self.buttons[self.current_button].invoke()

    def subir(self):
        mensaje = self.ascensor.subir()
        self.actualizar_estado()
        if mensaje is None:
            messagebox.showinfo("Información", "Ya estás en el último piso. No puedes subir más.")

    def bajar(self):
        mensaje = self.ascensor.bajar()
        self.actualizar_estado()
        if mensaje is None:
            messagebox.showinfo("Información", "Ya estás en la planta baja. No puedes bajar más.")

    def entrar_persona(self):
        mensaje = self.ascensor.entrar_persona()
        self.actualizar_estado()
        if "No puede entrar" in mensaje or "lleno" in mensaje:
            messagebox.showinfo("Información", mensaje)

    def salir_persona(self):
        mensaje = self.ascensor.salir_persona()
        self.actualizar_estado()
        if "vacío" in mensaje:
            messagebox.showinfo("Información", mensaje)

    def actualizar_estado(self):
        self.estado_label.config(text=f"Estás en el piso {self.ascensor.piso_actual}")
        self.capacidad_label.config(text=f"Capacidad: {self.ascensor.capacidad_actual}/{self.ascensor.capacidad_maxima}")
        self.peso_label.config(text=f"Peso: {self.ascensor.peso_actual}/{self.ascensor.peso_maximo} kg")

    def salir(self):
        self.root.destroy()


def main():
    ascensor = Ascensor(10, 10, 450)
    root = tk.Tk()
    app = AscensorApp(root, ascensor)
    root.mainloop()


if __name__ == "__main__":
    main()
