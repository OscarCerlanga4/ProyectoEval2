class Ascensor:
    def __init__(self, pisos_totales):
        self.pisos_totales = pisos_totales
        self.piso_actual = 1

    def subir(self):
        if self.piso_actual < self.pisos_totales:
            self.piso_actual += 1
            print(f"Subiendo... Ahora estás en el piso {self.piso_actual}.")
        else:
            print("Ya estás en el último piso. No puedes subir más.")

    def bajar(self):
        if self.piso_actual > 1:
            self.piso_actual -= 1
            print(f"Bajando... Ahora estás en el piso {self.piso_actual}.")
        else:
            print("Ya estás en la planta baja. No puedes bajar más.")

    def mostrar_menu(self):
        print("\nOpciones:")
        print("1. Subir de piso")
        print("2. Bajar de piso")
        print("3. Cerrar el ascensor")

def main():
    ascensor = Ascensor(5)
    print("¡Bienvenido al simulador de ascensor!")
    
    while True:
        print(f"\nEstás en el piso {ascensor.piso_actual}.")
        ascensor.mostrar_menu()
        opcion = input("Elige una opción (1, 2 o 3): ")

        if opcion == "1":
            ascensor.subir()
        elif opcion == "2":
            ascensor.bajar()
        elif opcion == "3":
            print("Cerrando el ascensor. ¡Adiós!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
