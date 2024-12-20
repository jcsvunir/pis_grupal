import ipywidgets as widgets
from IPython.display import display, clear_output

class Calculadora:
    def __validar_entrada(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ambos parámetros deben ser números (int o float).")

    def sumar(self, a, b):
        self.__validar_entrada(a, b)
        return a + b

    def restar(self, a, b):
        self.__validar_entrada(a, b)
        return a - b

    def multiplicar(self, a, b):
        self.__validar_entrada(a, b)
        return a * b

    def dividir(self, a, b):
        self.__validar_entrada(a, b)
        if b == 0:
            raise ZeroDivisionError("División por cero")
        return a / b

# Crear una instancia de la calculadora
calc = Calculadora()

def realizar_operacion(operacion, num1, num2):
    try:
        if operacion == "Suma":
            resultado = calc.sumar(num1, num2)
        elif operacion == "Resta":
            resultado = calc.restar(num1, num2)
        elif operacion == "Multiplicación":
            resultado = calc.multiplicar(num1, num2)
        elif operacion == "División":
            resultado = calc.dividir(num1, num2)
        else:
            resultado = "Operación no válida"
        output.clear_output()
        with output:
            print(f"Resultado de {operacion.lower()}: {resultado}")
    except Exception as e:
        output.clear_output()
        with output:
            print(f"Error: {e}")

# Widgets para interactuar
operacion_selector = widgets.Dropdown(
    options=["Suma", "Resta", "Multiplicación", "División"],
    description="Operación:",
    style={'description_width': 'initial'}
)
num1_input = widgets.FloatText(
    description="Número 1:",
    style={'description_width': 'initial'}
)
num2_input = widgets.FloatText(
    description="Número 2:",
    style={'description_width': 'initial'}
)
calcular_button = widgets.Button(
    description="Calcular",
    button_style="success"
)
output = widgets.Output()

# Conectar el botón a la función
calcular_button.on_click(lambda btn: realizar_operacion(
    operacion_selector.value, num1_input.value, num2_input.value
))

# Desplegar widgets
widgets.VBox([
    operacion_selector,
    num1_input,
    num2_input,
    calcular_button,
    output
])
