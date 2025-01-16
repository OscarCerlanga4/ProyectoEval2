class Ascensor:
    def __init__(self, pisos_totales, capacidad_maxima):
        self.pisos_totales = pisos_totales
        self.piso_actual = 1
        self.capacidad_actual = 0
        self.capacidad_maxima = capacidad_maxima
        
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

    def entrar_persona(self):
        if self.capacidad_actual < self.capacidad_maxima:
            self.capacidad_actual += 1
            print(f"Entró una persona. Capacidad actual: {self.capacidad_actual}/{self.capacidad_maxima}.")
        else:
            print("El ascensor está lleno. No puede entrar más personas.")

    def salir_persona(self):
        if self.capacidad_actual > 0:
            self.capacidad_actual -= 1
            print(f"Salió una persona. Capacidad actual: {self.capacidad_actual}/{self.capacidad_maxima}.")
        else:
            print("El ascensor está vacío. No hay personas para salir.")   
    
    
    def menu_principal(self):
        print("1. Subir al ascensor")
        print("2. Subir por las escaleras")
        
    def menu_ascensor(self):
        print("\nOpciones:")
        print("a. Subir de piso")
        print("b. Bajar de piso")
        print("c. Entrar persona")
        print("d. Salir persona")
        print("e. Salir del ascensor")


def main():
# Inicialización con 5 pisos y capacidad máxima de 4 personas
    ascensor = Ascensor(5,4)
    print("¡Bienvenido al simulador de ascensor!\n")
    
    while True:
        ascensor.menu_principal()
        opcion1 = input("\n¿Qué deseas hacer?: ")
        
        if opcion1 == "1": 
            
            while True:
                print(f"\nEstás en el piso {ascensor.piso_actual}.")
                ascensor.menu_ascensor()
                opcion2 = input("¿Qué quieres hacer ahora?: ")
                
                if opcion2 == "a":
                    ascensor.subir()
                elif opcion2 == "b":
                    ascensor.bajar()
                elif opcion2 == "c":
                    ascensor.entrar_persona()
                elif opcion2 == "d":
                    ascensor.salir_persona()
                elif opcion2 == "e":
                    print("Cerrando ascensor, adios")
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
            break
        
        elif opcion1 == "2":
            print("Okey, que vaya bien deportista")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            


if __name__ == "__main__":
    main()