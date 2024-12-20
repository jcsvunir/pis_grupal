# Parte 1: Desarrollo de la calculadora

class Calculadora:
    # Clase Calculadora con las funciones: suma, resta, multiplicación y división.
    def __validar_entrada(self, a, b):

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ambos parámetros deben ser números (int o float).")

    def sumar(self, a, b):
        # Devuelve la suma de a y b
        self.__validar_entrada(a, b)
        return a + b

    def restar(self, a, b):
        # Devuelve la resta de a menos b.
        self.__validar_entrada(a, b)
        return a - b

    def multiplicar(self, a, b):
        # Devuelve el producto de a y b.
        self.__validar_entrada(a, b)
        return a * b

    def dividir(self, a, b):
        # Devuelve la dividido entre b. se controla la división por 0
        self.__validar_entrada(a, b)
        if b == 0:
            raise ZeroDivisionError("División por cero")
        return a / b

# Parte 2: Pruebas Unitarias

import unittest

class TestCalculadora(unittest.TestCase):
    # Clase de pruebas unitarias para la Calculadora usando la librería unittest.
    
    def test_sumar(self):
        self.assertEqual(Calculadora.sumar(10, 12), 22)
        self.assertEqual(Calculadora.sumar(-2, 1), -1)
        self.assertEqual(Calculadora.sumar(0, 7), 7)

    def test_restar(self):
        self.assertEqual(Calculadora.restar(10, 12), -2)
        self.assertEqual(Calculadora.restar(-2, 1), -3)
        self.assertEqual(Calculadora.restar(0, 7), -7)

    def test_multiplicar(self):
        self.assertEqual(Calculadora.multiplicar(10, 12), 120)
        self.assertEqual(Calculadora.multiplicar(-2, 1), -2)
        self.assertEqual(Calculadora.multiplicar(0, 7), 0)

    def test_dividir(self):
        self.assertEqual(Calculadora.dividir(10, 5), 2)
        self.assertEqual(Calculadora.dividir(-2, 1), -2)
        self.assertEqual(Calculadora.dividir(0, 5), 0)
        self.assertEqual(Calculadora.dividir(0, 7), 0)
        with self.assertRaises(ZeroDivisionError):
            Calculadora.dividir(7, 0)
        

if __name__ == "__main__":
    # Ejecutar las pruebas
    result = unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromTestCase(TestCalculadora))

    # Mostrar solo OK o KO
    if result.wasSuccessful():
        print("OK a pruebas")
    else:
        print("KO a pruebas")
