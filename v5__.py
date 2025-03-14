class Ascensor:
    def __init__(self, pisos_totales, capacidad_maxima, peso_maximo):
        self.pisos_totales = pisos_totales
        self.piso_actual = 1
        self.capacidad_actual = 0
        self.capacidad_maxima = capacidad_maxima
        self.peso_actual = 0
        self.peso_maximo = peso_maximo
        self.uso_contador = 0  # Contador de usos
        self.en_mantenimiento = False  # Estado de mantenimiento
    
    def verificar_mantenimiento(self):
        if self.uso_contador >= 20:  # Cada 20 usos requiere mantenimiento
            print("\n⚠️  Mantenimiento requerido. El ascensor no funcionará hasta ser revisado.")
            self.en_mantenimiento = True
            return True
        return False

    def mantenimiento(self):
        print("🔧 Mantenimiento realizado. El ascensor está operativo nuevamente.")
        self.uso_contador = 0
        self.en_mantenimiento = False
