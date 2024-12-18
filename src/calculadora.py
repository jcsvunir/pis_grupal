class Calculadora:
    """
    Clase que implementa las funciones básicas de una calculadora con validación de entradas.
    """

    def __validar_entrada(self, a, b):
        """
        Valida que las entradas sean numéricas.
        :param a: Dato 1 a validar.
        :param b: Dato 2 a validar.
        :return:
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ambos parámetros deben ser números (int o float).")

    def sumar(self, a, b):
        """
        Función que suma los valores a y b si han sido validados correctamente.
        :param a:
        :param b:
        :return: a + b
        """
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
            raise ZeroDivisionError("División entre cero no permitida.")
        return a / b
