class Calculadora:
    def __validar_entrada(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ambos parámetros deben ser números (int o float).")

    def sumar(self, a, b):
        """Devuelve la suma de a y b"""
        print('vamos a validar para poder sumar')
        self.__validar_entrada(a, b)
        return a + b

    def restar(self, a, b):
        """Devuelve la resta de a menos b."""
        print('vamos a validar para poder restar')
        self.__validar_entrada(a, b)
        return a - b

    def multiplicar(self, a, b):
        """Devuelve el producto de a y b."""
        print('vamos a validar para poder multiplicar')
        self.__validar_entrada(a, b)
        return a * b

    def dividir(self, a, b):
        """Devuelve la dividido entre b. se controla la división por 0"""
        print('vamos a validar para poder dividir')
        self.__validar_entrada(a, b)
        if b == 0:
            raise ZeroDivisionError("División por cero")
        return a / b
