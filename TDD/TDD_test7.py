import unittest
from TDD.funcoes import filtrar_por_data

class TestFiltroData(unittest.TestCase):
    def test_filtrar_data_0606(self):
        resultado = filtrar_por_data("06/06/2025")
        esperado = [
            "108, Carla Dias, Guarda-chuva, 06/06/2025, Shopping, achado",
            "109, Daniel Lima, Relógio Prata, 06/06/2025, Academia, achado"
        ]
        self.assertEqual(resultado, esperado)
