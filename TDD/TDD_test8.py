import unittest
from funcoes import alterar_local
class TestAlterarLocal(unittest.TestCase):
    def test_alterar_local_item_101(self):
        sucesso = alterar_local(101, "Novo Local Teste")
        self.assertTrue(sucesso)
