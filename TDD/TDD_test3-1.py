import unittest
from funcoes import cadastrar_item_perdido

class TestCadastroItemPerdido(unittest.TestCase):
    def test_cadastrar_item_novo(self):
        resposta = cadastrar_item_perdido("111", "Gabriel Vettorazzi", "Carteira preta", "10/06/2025", "Confeitaria Holandesa", "perdido")
        self.assertEqual(resposta, "Cadastro realizado com sucesso")

