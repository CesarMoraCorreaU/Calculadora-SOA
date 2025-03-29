import unittest
from operaciones.dividir import dividir
from operaciones.multiplicar import multiplicar
from operaciones.restar import restar
from operaciones.sumar import sumar

class TestCalculadoraSOA(unittest.TestCase):
    
    def test_sumar_positivos(self):
        self.assertEqual(sumar(3, 7), 10)

    def test_restar_positivos(self):
        self.assertEqual(restar(10, 5), 5)

    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(4, 3), 12)

    def test_dividir_positivos(self):
        self.assertEqual(dividir(20, 4), 5)

    def test_dividir_por_cero(self):
        self.assertEqual(dividir(5, 0), "Math Error")

if __name__ == '__main__':
    unittest.main()
