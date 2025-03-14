class Ascensor:
    def __init__(self, pisos_totales, capacidad_maxima, peso_maximo):
        self.piso_actual = 1
        self.peso_actual = 0
        self.peso_maximo = peso_maximo

    def verificar_sobrepeso(self):
        if self.peso_actual > self.peso_maximo:
            print("\n❌ El ascensor está sobrecargado y no puede moverse.")
            return True
        return False

    def subir(self):
        if self.verificar_sobrepeso():
            return  # No sube si está sobrecargado
        self.piso_actual += 1
        print(f"Subiendo... Ahora estás en el piso {self.piso_actual}.")

    def bajar(self):
        if self.verificar_sobrepeso():
            return  # No baja si está sobrecargado
        self.piso_actual -= 1
        print(f"Bajando... Ahora estás en el piso {self.piso_actual}.")
