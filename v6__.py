import time  # Importa la librería para pausas

class Ascensor:
    def subir(self):
        if self.piso_actual < self.pisos_totales:
            self.piso_actual += 1
            print(f"Subiendo... Ahora estás en el piso {self.piso_actual}.")
            time.sleep(1)  # Pausa de 1 segundo para simular el tiempo de viaje
        else:
            print("Ya estás en el último piso.")

    def bajar(self):
        if self.piso_actual > 1:
            self.piso_actual -= 1
            print(f"Bajando... Ahora estás en el piso {self.piso_actual}.")
            time.sleep(1)  # Pausa de 1 segundo
        else:
            print("Ya estás en la planta baja.")
