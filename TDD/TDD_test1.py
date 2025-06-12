import unittest
from TDD.funcoes import login, cadastrar_usuario

class TestLogin(unittest.TestCase):
    def test_login_valido(self):
        cadastrar_usuario("Ana Silva", "ana.silva@email.com", "senha123")
        resultado = login("Ana Silva", "ana.silva@email.com", "senha123")
        self.assertEqual(resultado, "Bem-vindo Ana Silva")
