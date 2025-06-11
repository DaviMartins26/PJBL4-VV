import unittest
from funcoes import cadastrar_item_achado

class TestRegistrarItemAchado(unittest.TestCase):
    def test_registrar_item_achado(self):
        cadastrar_item_achado(201, "Joshua", "Caderno Preto", "10/06/2025", "Sala 101")

        with open("itens.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        esperado = "201, Joshua, Caderno Preto, 10/06/2025, Sala 101, achado\n"
        self.assertIn(esperado, linhas)

if __name__ == "__main__":
    unittest.main()
