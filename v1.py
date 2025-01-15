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

    def menu_principal(self):
        print("1. Subir al ascensor")
        print("2. Subir por las escaleras")
        
    def menu_ascensor(self):
        print("\nOpciones:")
        print("a. Subir de piso")
        print("b. Bajar de piso")
        print("c. Bajar aquí")

def main():
    ascensor = Ascensor(5)
    print("¡Bienvenido al simulador de ascensor!, ¿Qué deseas hacer?")
    
    while True:
        ascensor.menu_principal()
        opcion1 = input("\nHola, ¿Qúe deseas hacer?: ")
        
        if opcion1 == "1":
            while True:
                print(f"\nEstás en el piso {ascensor.piso_actual}.")
                ascensor.menu_ascensor()
                if opcion1 == "a":
                    ascensor.subir()
                elif opcion1 == "b":
                    ascensor.bajar()
                elif opcion1 == "c":
                    print("Cerrando el ascensor. ¡Adiós!")
                break
        elif opcion1 == "2":
            print("Okey, que vaya bien deportista")
            break
        else:
            print("Opción no valida")
            
        # print(f"\nEstás en el piso {ascensor.piso_actual}.")
        # ascensor.mostrar_menu()
        # opcion = input("¿Qué deseas hacer?: ")

        # if opcion == "1":
        #     ascensor.subir()
        # elif opcion == "2":
        #     ascensor.bajar()
        # elif opcion == "3":
        #     print("Cerrando el ascensor. ¡Adiós!")
        #     break
        # elif opcion== "5":
        #     print("Okey, que vaya bien deportista")
        #     break
        # else:
        #     print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
