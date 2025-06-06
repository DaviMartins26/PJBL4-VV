import unittest
from src.funcoes import filtrar_por_data

class TestFiltroData(unittest.TestCase):
    def test_filtrar_data_0606(self):
        resultado = filtrar_por_data("06/06/2025")
        self.assertEqual(resultado, [])  
