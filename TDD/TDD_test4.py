import unittest
from funcoes import filtrar_itens_perdidos

class TestFiltroItensPerdidos(unittest.TestCase):
    def setUp(self):
        self.itens = [
            {"id": "111", "nome": "Gabriel", "descricao": "Carteira preta", "data": "10/06/2025", "local": "Confeitaria Holandesa", "status": "perdido"},
            {"id": "112", "nome": "Ana", "descricao": "Chave prata", "data": "09/06/2025", "local": "Shopping Curitiba", "status": "encontrado"},
        ]

    def test_filtrar_por_local_e_status(self):
        filtro = {"local": "Confeitaria Holandesa", "status": "perdido"}
        resultado = filtrar_itens_perdidos(self.itens, filtro)
        esperado = [self.itens[0]]
        self.assertEqual(resultado, esperado)

if __name__ == "__main__":
    unittest.main()
