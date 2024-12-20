class Suma:
    def __validar_entrada(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ambos parámetros deben ser números (int o float).")

    def sumar(self, a, b):
        """Devuelve la suma de a y b"""
        print('vamos a validar para poder sumar')
        self.__validar_entrada(a, b)
        return a + b