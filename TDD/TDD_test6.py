import unittest
from funcoes import listar_itens_achados

class TestListarItensAchados(unittest.TestCase):
    def test_listar_itens_achados(self):
        print("Itens do tipo 'achado':")
        listar_itens_achados()

if __name__ == "__main__":
    unittest.main()
