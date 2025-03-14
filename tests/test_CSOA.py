import unittest
from main import sumar, restar, multiplicar, dividir  # Importamos las funciones

class TestCalculadoraSOA(unittest.TestCase):

    # Pruebas para la función sumar
    def test_sumar_positivos(self):
        self.assertEqual(sumar(3, 5), 8)
    
    def test_sumar_cero(self):
        self.assertEqual(sumar(0, 10), 10)
    
    def test_sumar_valores_grandes(self):
        self.assertEqual(sumar(1000, 5000), 6000)

    # Pruebas para la función restar
    def test_restar_positivos(self):
        self.assertEqual(restar(10, 5), 5)
    
    def test_restar_cero(self):
        self.assertEqual(restar(10, 0), 10)
    
    def test_restar_a_si_mismo(self):
        self.assertEqual(restar(5, 5), 0)

    # Pruebas para la función multiplicar
    def test_multiplicar_basico(self):
        self.assertEqual(multiplicar(4, 5), 20)
    
    def test_multiplicar_por_cero(self):
        self.assertEqual(multiplicar(0, 10), 0)
    
    def test_multiplicar_por_uno(self):
        self.assertEqual(multiplicar(7, 1), 7)

    # Pruebas para la función dividir
    def test_dividir_basico(self):
        self.assertEqual(dividir(10, 2), 5)
    
    def test_dividir_exacta(self):
        self.assertEqual(dividir(9, 3), 3)
    
    def test_dividir_inexacta(self):
        self.assertEqual(dividir(7, 2), 3)  # División entera, no devuelve decimales
    
    def test_dividir_por_uno(self):
        self.assertEqual(dividir(7, 1), 7)
    
    def test_dividir_por_cero(self):
        self.assertEqual(dividir(10, 0), "Math Error")

if __name__ == '__main__':
    unittest.main()
