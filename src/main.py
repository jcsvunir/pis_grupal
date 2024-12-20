# src/main.py
from calculadora import Calculadora

# Códigos ANSI para colores
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
RED = "\033[31m"
CYAN = "\033[36m"
BOLD = "\033[1m"


def mostrar_menu():
    """Función para mostrar el menú interactivo."""
    print(f"\n{BOLD}--- Calculadora Básica ---{RESET}")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("S. Salir")
    print("--------------------------")

def solicitar_numeros():
    """Solicita dos números al usuario y los valida."""
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print(f"{RED}Error: Introduzca valores numéricos válidos.{RESET}")

def main():
    """Función principal para ejecutar el menú de la calculadora."""
    calc = Calculadora()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip().lower()

        if opcion == 's':
            print(f"{CYAN}Saliendo... ¡Hasta pronto!{RESET}")
            break

        elif opcion in ['1', '2', '3', '4']:
            num1, num2 = solicitar_numeros()

            try:
                if opcion == '1':
                    resultado = calc.sumar(num1, num2)
                    print(f"{BOLD}{GREEN}Resultado de la suma: {resultado}{RESET}")
                elif opcion == '2':
                    resultado = calc.restar(num1, num2)
                    print(f"{YELLOW}Resultado de la resta: {resultado}{RESET}")
                elif opcion == '3':
                    resultado = calc.multiplicar(num1, num2)
                    print(f"{BLUE}Resultado de la multiplicación: {resultado}{RESET}")
                elif opcion == '4':
                    resultado = calc.dividir(num1, num2)
                    print(f"{MAGENTA}Resultado de la división: {resultado}{RESET}")
            except Exception as e:
                print(f"{RED}Error: {e}{RESET}")
        else:
            print(f"{RED}Opción no válida. Inténtelo de nuevo.{RESET}")

if __name__ == "__main__":
    main()
