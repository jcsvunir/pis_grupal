import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        """Inicializa la clase Calculadora."""
        self.calc = Calculadora()

    def test_sumar(self):
        """Pruebas método suma."""
        print('vamos con sumar')
        self.assertEqual(self.calc.sumar(3, 5), 8)
        self.assertEqual(self.calc.sumar(-3, 5), 2)
        self.assertEqual(self.calc.sumar(-3, -5), -8)
        with self.assertRaises(TypeError):
            self.calc.sumar("a", 5)

    def test_restar(self):
        """Pruebas método resta."""
        print('vamos con restar')
        self.assertEqual(self.calc.restar(10, 5), 5)
        self.assertEqual(self.calc.restar(5, 10), -5)
        with self.assertRaises(TypeError):
            self.calc.restar("a", 5)

    def test_multiplicar(self):
        """Pruebas método multiplicación."""
        print('vamos con multiplicar')
        self.assertEqual(self.calc.multiplicar(4, 3), 12)
        self.assertEqual(self.calc.multiplicar(4, -3), -12)
        with self.assertRaises(TypeError):
            self.calc.multiplicar("a", 5)

    def test_dividir(self):
        """Pruebas método división."""
        print('vamos con dividir')
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(-10,5), -2)
        self.assertEqual(self.calc.dividir(10,-5), -2)
        self.assertEqual(self.calc.dividir(0, 10), 0)
        self.assertEqual(self.calc.dividir(0, -10), 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(10, 0)


    def test_validar_entrada(self):
        """Pruebas de validación de datos de entrada."""
        with self.assertRaises(TypeError):
            self.calc.sumar("a", 5)
        with self.assertRaises(TypeError):
            self.calc.dividir(5, "b")
        with self.assertRaises(TypeError):
            self.calc.restar("c", "d")


if __name__ == "__main__":
    unittest.main()
