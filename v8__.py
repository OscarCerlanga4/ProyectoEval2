from colorama import Fore, Style

class Ascensor:
    def subir(self):
        print(Fore.GREEN + "Subiendo..." + Style.RESET_ALL)
        print(f"Ahora estás en el piso {self.piso_actual}.")

    def bajar(self):
        print(Fore.BLUE + "Bajando..." + Style.RESET_ALL)
        print(f"Ahora estás en el piso {self.piso_actual}.")

    def fallo_sobrepeso(self):
        print(Fore.RED + "\n❌ El ascensor está sobrecargado y no puede moverse." + Style.RESET_ALL)

    def mantenimiento(self):
        print(Fore.YELLOW + "⚠️  Mantenimiento requerido." + Style.RESET_ALL)
