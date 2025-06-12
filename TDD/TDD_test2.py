import unittest
from TDD.funcoes import cadastrar_usuario

class TestCadastro(unittest.TestCase):
    def test_cadastro_sucesso(self):
        resposta = cadastrar_usuario("Joana", "joana@email.com", "abcd")
        self.assertEqual(resposta, "Usuario cadastrado com sucesso")

