from v1 import Ascensor
    
def main():
    ascensor = Ascensor(5)
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
                    print("Cerrando el ascensor. ¡Adiós!")
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
