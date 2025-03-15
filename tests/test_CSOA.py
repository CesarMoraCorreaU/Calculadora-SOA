import unittest

# ✅ Importando funciones desde el paquete operaciones
from operaciones.sumar import sumar
from operaciones.restar import restar
from operaciones.multiplicar import multiplicar
from operaciones.dividir import dividir

class TestCalculadoraSOA(unittest.TestCase):

    # ✅ Pruebas para la función sumar
    def test_sumar_positivos(self):
        self.assertEqual(sumar(3, 5), 8)

    def test_sumar_cero(self):
        self.assertEqual(sumar(0, 10), 10)

    def test_sumar_valores_grandes(self):
        self.assertEqual(sumar(1000, 5000), 6000)

    def test_sumar_negativos(self):
        self.assertEqual(sumar(-3, -7), -10)

    def test_sumar_negativo_positivo(self):
        self.assertEqual(sumar(-5, 3), -2)

    # ✅ Pruebas para la función restar
    def test_restar_positivos(self):
        self.assertEqual(restar(10, 5), 5)

    def test_restar_cero(self):
        self.assertEqual(restar(10, 0), 10)

    def test_restar_a_si_mismo(self):
        self.assertEqual(restar(5, 5), 0)

    def test_restar_negativos(self):
        self.assertEqual(restar(-5, -3), -2)

    def test_restar_menor_menos_mayor(self):
        self.assertEqual(restar(4, 7), -3)

    # ✅ Pruebas para la función multiplicar
    def test_multiplicar_basico(self):
        self.assertEqual(multiplicar(4, 5), 20)

    def test_multiplicar_por_cero(self):
        self.assertEqual(multiplicar(0, 10), 0)

    def test_multiplicar_por_uno(self):
        self.assertEqual(multiplicar(7, 1), 7)

    def test_multiplicar_negativos(self):
        self.assertEqual(multiplicar(-4, -3), 12)

    def test_multiplicar_negativo_por_positivo(self):
        self.assertEqual(multiplicar(-4, 3), -12)

    # ✅ Pruebas para la función dividir
    def test_dividir_basico(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_exacta(self):
        self.assertEqual(dividir(9, 3), 3)

    def test_dividir_inexacta(self):
        self.assertEqual(dividir(7, 2), 3)  # División entera, sin decimales

    def test_dividir_por_uno(self):
        self.assertEqual(dividir(7, 1), 7)

    def test_dividir_por_cero(self):
        self.assertEqual(dividir(10, 0), "Math Error")

    def test_dividir_negativos(self):
        self.assertEqual(dividir(-20, 4), -5)

    def test_dividir_negativo_por_negativo(self):
        self.assertEqual(dividir(-20, -4), 5)

if __name__ == '__main__':
    unittest.main()
